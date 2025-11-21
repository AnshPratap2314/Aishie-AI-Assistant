import os
import json
import platform
import subprocess
from pathlib import Path
import time



try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    Observer= None
    FileSystemEventHandler = object

APPS_JSON_PATH = Path(__file__).parent/ "installed-apps.json"
MONITORED_DIRS=["Applications", str(Path.home()/ "Applications")]


def list_apps_macos():
    apps =[]
    dirs=["/Applications", str(Path.home()  / "Applications")]
    for d in dirs:
        if os.path.exists(d):
            for item in os.scandir(d):
                if item.name.endswith("app"):
                    apps.append({"name": item.name, "path": item.path})

    return sorted(list(set(apps)))

def list_apps_windows():
    apps=[]
    dirs=[os.environ.get("ProgramFiles"),os.environ.get("ProgramFiles(x86)")]
    for d in dirs:
        if d and os.path.exists(d):
            for item in os.scandir(d):
                if item.is_dir():
                    apps.append({"name":item.name, "path": item.path})
    return apps

def list_apps_linux():
    apps=[]
    try:
        proc=subprocess.run(["dpkg-query","-W","-f=${Package}\n"],capture_output=True , text= True)
        if proc.returncode==0:
            for line in proc.stdout.splitlines():
                if line.strip():
                    apps.append({"name":line.strip(),"path":""})
    except Exception:
        pass
    return apps

def get_installed_apps():
    system=platform.system().lower()
    if system=="darwin":
        return list_apps_macos()
    elif system=="windows":
        return list_apps_windows()
    elif system=="linux":
        return list_apps_linux()
    else:
        return[]

class AppsFolderEventHandler(FileSystemEventHandler):
    def __init__(self,callback):
        self.callback= callback
    def on_created(self, event):
        self.callback(event)
    def on_deleted(self, event):
        self.callback(event)

def start_apps_watcher(callback):
    if Observer is None:
        print("⚠️ Watchdog not installed")
        return None

    system=platform.system().lower()
    paths_to_watch=[]
    if system=="darwin":
        paths_to_watch=["/Applications",str(Path.home() / "Applications")]
    elif system=="windows" :
        paths_to_watch=[os.environ.get("ProgramFiles"),os.environ.get("ProgramFiles(x86)")]
    elif system=="linux":
        paths_to_watch=["/usr/share/applications"]

    observer= Observer()
    handler=AppsFolderEventHandler(callback)

    for path in paths_to_watch:
        if path and os.path.exists(path):
            observer.schedule(handler,path=path , recursive=False)

    observer.start()
    print("👀 Started monitoring for app changes...")
    return observer

def save_apps_to_json(apps):
    with open(APPS_JSON_PATH,"w") as f:
        json.dump(apps,f,indent=4)

def load_apps_from_json():
    if APPS_JSON_PATH.exists():
        with open(APPS_JSON_PATH,"r") as f:
            return json.load(f)
    return []

if __name__ == "__main__":
    print("🔧 Initializing System Awareness...")
    apps=get_installed_apps()
    save_apps_to_json(apps)
    print(f"{len(apps)} applications detected and saved")

    def on_change(event):
        print(f"Change detected: {event.event_type} - {event.src_path}")
        new_apps=get_installed_apps()
        save_apps_to_json(new_apps)
        print("✅ App list updated.")

    observer=start_apps_watcher(on_change)
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        if observer:
            observer.stop()
        print("Monitor Stopped")
    if observer:
        observer.join()


