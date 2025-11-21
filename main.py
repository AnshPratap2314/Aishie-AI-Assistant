import time
import json
import pyautogui
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import subprocess
import datetime
import difflib
import os
import random
from pathlib import Path
from installed_apps import start_apps_watcher, get_installed_apps, save_apps_to_json
import threading
from pync import Notifier
from communication_hub import (send_email,send_whatsapp_to_contact,send_imessage,read_imessages,call_contact,get_contact_info,)
import smtplib,ssl
pyautogui.position()


print("✅ All key libraries are working perfectly!")
ASSISTANT_NAME = "Aishie"
MEMORY_FILE = "aishie_memory.json"
APP_CHANGE_LOG="app_changes.json"
pending_app_changes=[]
WAKE_WORDS = [f"hey {ASSISTANT_NAME}", f"ok {ASSISTANT_NAME}", ASSISTANT_NAME.lower(), f"hey ic", f"hey i see",
              "aishie", "hey aishie", "ok aishie",
              "ai", "hey ai", "ok ai", "i see", "aic", "ic"
              ]
SUPPORTED_COMMANDS = [
    "open youtube", "open google", "open safari", "open notes", "open terminal",
    "take a screenshot", "type", "stop", "bye", "sleep", "exit",
    "who is", "what is", "tell me about", "define", "explain", "what's",
    "send imessage", "read imessages", "read messages",
    "call", "facetime",
    "send email", "send mail", "send whatsapp message"
]

engine = pyttsx3.init()
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break


def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

memory = load_memory()

def log_app_changes(message):
    global pending_app_changes
    timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry={"time":timestamp,"message":message}
    pending_app_changes.append(entry)

    try:
        data=[]
        if os.path.exists(APP_CHANGE_LOG):
            with open(APP_CHANGE_LOG, "r") as f:
                data=json.load(f)
        data.append(entry)
        with open(APP_CHANGE_LOG, "w") as f:
            json.dump(data,f,indent=2)
    except Exception as e:
        print("⚠️ Couldn't save app change log:", e)

def get_recent_app_changes(limit=5):
    if not os.path.exists(APP_CHANGE_LOG):
        return []
    try:
        with open(APP_CHANGE_LOG, "r")as f:
            data=json.load(f)
            return data[-limit:] if len(data)> limit else data
    except Exception:
        return[]



def start_system_awareness():
    watcher_thread = threading.Thread(target=start_apps_watcher, args=(on_app_change,), daemon=True)
    watcher_thread.start()
    print("👀 Aishie is now monitoring installed applications.")
    try:
        Notifier.notify("Real-time monitoring of installed apps is now active.", title="Aishie System Awareness Active",
                        sound="default",open=Path("/Applications").resolve().as_uri())
    except Exception:
        pass


def time_based_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good Morning ,Sir!️"
    elif 12 <= hour < 17:
        return "Good Afternoon ,Sir!"
    elif 17 <= hour < 21:
        return "Good Evening ,Sir!"
    else:
        return "Hello Sir, Working late I see"


def greet_user():
    greetings = ["Hello Sir! How are you today?", "Hi there! What can I do for you?",
                 "Good to see you, Sir! How Can i assist you?", "Hey Sir! Ready when you are"]
    time_greet = time_based_greeting()
    speak(f"{time_greet} {random.choice(greetings)}", polite=False)


def speak(text, polite=True):
    engine = pyttsx3.init('nsss')
    engine.setProperty('rate', 175)
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    polite_endings = ["", " Sir.", " Hope that helps.", " Anything else you'd like to know?",
                      " Always happy to help, Sir."]
    full_text = text
    if polite:
        full_text += random.choice(polite_endings)
    print(f"Aishie: {full_text}")
    engine.say(full_text)
    engine.runAndWait()
    time.sleep(0.3)


def speak_long_text(text):
    """Split long text into smaller sentences and speak each."""
    sentences = text.split(". ")
    for s in sentences:
        if s.strip():
            speak(s.strip(), polite=False)
            time.sleep(0.3)


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            command = recognizer.recognize_google(audio).lower()
            print(f"🗣️ You said: {command}")
            return command
        except sr.WaitTimeoutError:
            return " "
        except sr.UnknownValueError:
            return " "
        except sr.RequestError:
            speak("Network Error, Please Check Your Internet Connection.")
            return " "


def wake_up():
    while True:
        print("Say the wake word...")
        command = listen().lower().strip()

        if any(word in command for word in WAKE_WORDS):
            speak("Yes Sir,I am Listening.", polite=False)
            greet_user()
            return True

        for word in WAKE_WORDS:
            match = difflib.get_close_matches(command, [word], cutoff=0.6)
            if match:
                speak("Yes Sir,I am Listening")
                return True


def main():
    wake_up()
    speak("Sir! Aishie is online and monitoring your system.")
    start_system_awareness()
    while True:
        time.sleep(0.3)
        command = listen()
        if not command:
            continue
        if any(k in command for k in ["stop", "bye", "quit", "sleep", "exit"]):
            speak("Bye Sir, Take care, and see you soon")
            break
        match = difflib.get_close_matches(command, SUPPORTED_COMMANDS, n=1, cutoff=0.6)
        if match:
            corrected_command = match[0]
            speak(f"I understood: {corrected_command}")
            executed_command(corrected_command)
        else:
            executed_command(command)
        time.sleep(0.5)


def executed_command(command):
    if "open youtube" in command:
        speak("Opening Youtube", polite=False)
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google", polite=False)
        webbrowser.open("https://www.google.com/?client=safari&channel=iphone_bm")

    elif "safari" in command:
        speak("Opening Safari", polite=False)
        open_app("Safari")

    elif "notes" in command:
        speak("Opening Notes", polite=False)
        open_app("Notes")

    elif "terminal" in command:
        speak("Opening Terminal", polite=False)
        open_app("Terminal")

    elif "increase volume" in command:
        speak("Increasing volume", polite=False)
        pyautogui.press("volumeup")

    elif "decrease volume" in command:
        speak("Decreasing volume", polite=False)
        pyautogui.press("volumedown")

    elif "mute" in command:
        speak("Muting the volume", polite=False)
        pyautogui.press("volumemute")

    elif "shutdown" in command:
        speak("Are you sure you want to shut down?", polite=False)
        confirm = listen()
        if "yes" in confirm:
            speak("Shutting down. Goodbye Sir.")
            os.system("shutdown -h now")

    elif "restart" in command:
        speak("Restarting system. Please wait.", polite=False)
        os.system("shutdown -r now")

    elif "i love you" in command:
        speak("Aww, that's sweet, Sir! I’m just a bunch of code, but I appreciate it!")

    elif "are you single" in command:
        speak("Haha, I’m in a committed relationship with my code!")

    elif "how old are you" in command:
        speak("I was created not too long ago, but I’m learning fast every day!")

    elif "do you sleep" in command:
        speak("I don’t need sleep, Sir. I’m always active for you!")

    elif "remember that" in command:
        key = command.replace("remember that", "").strip()
        if key:
            memory["note"] = key
            save_memory(memory)
            speak(f"Okay,I'll remember that{key}")
        else:
            speak("What should I remember ,Sir?")

    elif "what did you remember" in command:
        if "note" in memory:
            speak(f"You ask me remember that {memory['note']}")
        else:
            speak("I dont have anything stored in my memory right now.")

    elif "forget that" in command:
        if "note" in memory:
            speak(f"Okay Sir, I forgot that you told me {memory['note']}")
            memory.clear()
            save_memory(memory)
        else:
            speak("I dont have anything stored in my memory right now, Sir")

    elif "take a screenshot" in command:
        try:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            filename = f"screenshot_{timestamp}.png"
            filepath = os.path.join(desktop_path, filename)
            screenshot = pyautogui.screenshot()
            screenshot.save(filepath)
            speak(f"Screenshot saved on Desktop as {filename}", polite=False)
        except Exception:
            speak("Sorry Sir, I couldn't take the screenshot.😔")

    elif "type" in command:
        text_to_type = command.replace("type ", " ")
        pyautogui.write(text_to_type)
        speak(f"Typing {text_to_type}", polite=False)

    elif any(kw in command for kw in ["who is", "what is", "tell me about", "define", "explain", "what's"]):
        answer_question(command)

    elif "thank" in command or "thank you" in command or "thanks" in command:
        speak("My pleasure, Sir!")

    elif "how are you" in command:
        speak("I'am doing great,Sir! Thanks for asking.How about you? Everything good on Your side?")

    elif "i am fine" in command or "i am good" in command or "fine" in command or "good" in command:
        speak("That's Great, Sir!")

    elif "who are you" in command or "who is aishie" in command:
        speak(
            "I’m Aishie, your personal AI assistant, Sir! I’m here to help you, answer your questions, and make your tasks easier. 😄")

    elif "what changed" in command or "what apps changed" in command or "show app changes" in command:
        recent_changes = get_recent_app_changes(limit=5)
        if not recent_changes:
            speak("No recent changes detected in your applications, Sir.")
        else:
            speak("Here are the latest application changes, Sir:")
            for change in recent_changes:
                speak(f"{change['message']} at {change['time']}", polite=False)

    elif "clear app log" in command or "delete app log" in command or "forget app changes" in command or "clear app history" in command:
        if os.path.exists(APP_CHANGE_LOG):
            try:
                os.remove(APP_CHANGE_LOG)
                pending_app_changes.clear()
                speak("All logged application changes have been cleared, Sir.")
            except Exception as e:
                print("⚠️ Could not clear app log:", e)
                speak("Sorry Sir, I couldn't clear the app log due to a system error.")
        else:
            speak("There is no app change history to clear, Sir.")




    elif any(word in command for word in ["send email", "send mail", "compose email", "compose mail"]):
        speak("Who should I send the email to?")
        recipient = listen().strip()

        email_spoken = (
            recipient.replace(" at the rate ", "@")
            .replace(" at ", "@")
            .replace(" dot ", ".")
            .replace(" underscore ", "_")
            .replace(" dash ", "-")
            .replace(" space ", "")
            .replace(" ", "")
        )
        if "@" in email_spoken and "." in email_spoken:
            email_address = email_spoken
            speak(f"Got it Sir, sending to {email_address}.")
        else:
            info = get_contact_info(recipient)
            if info and info.get("email"):
                email_address = info["email"]
                speak(f"I found {recipient}'s email as {email_address}.")
            else:
                applescript_lookup = f'''
                tell application "Mail"
                    set allContacts to every recipient
                    repeat with c in allContacts
                        if name of c contains "{recipient}" then
                            return address of c
                        end if
                    end repeat
                end tell
                '''
                result = subprocess.run(["osascript", "-e", applescript_lookup], capture_output=True, text=True)
                email_address = result.stdout.strip()

                if not email_address:
                    speak(f"Sorry Sir, I couldn’t find {recipient} in your contacts or Mail app.")
                    return
                else:
                    speak(f"I found {recipient}'s email in Mail: {email_address}")
        speak("What is the subject?")
        subject = listen().strip()
        speak("What should I say in the email?")
        body = listen().strip()
        speak(f"Sir, here's your email summary:")
        speak(f"To: {email_address}")
        speak(f"Subject: {subject}")
        speak(f"Message: {body}")
        speak("Should I send it, Sir?")
        confirmation = listen().strip()
        if any(word in confirmation for word in ["yes", "send", "sure", "do it", "go ahead"]):
            applescript_send = f'''
                tell application "Mail"
                    set newMessage to make new outgoing message with properties {{subject:"{subject}", content:"{body}", visible:true}}
                    tell newMessage
                        make new to recipient at end of to recipients with properties {{address:"{email_address}"}}
                        send
                    end tell
                end tell
                '''
            try:
                subprocess.run(["osascript", "-e", applescript_send])
                speak(f"Email successfully sent to {email_address}, Sir.")
            except Exception as e:
                print("⚠️ Mail send error:", e)
                speak("Sorry Sir, I couldn’t send the email through Apple Mail.")
        else:
            speak("Alright Sir, I won’t send the email.")

    elif "whatsapp" in command or "send whatsapp message to" in command:
        try:
            if "that" in command:
                parts=command.split("that",1)
                contact_part=parts[0].replace("send whatsapp message to", "").strip()
                msg_part=parts[1].strip()
                contact_name=contact_part
                message=msg_part
                send_whatsapp_to_contact(contact_name, message)
            else:
                contact_name=command.replace("send whatsapp message to", "").strip()
                send_whatsapp_to_contact(contact_name)
        except Exception as e:
            print("⚠️ Error handling WhatsApp message:", e)
            speak("Sorry Sir, I couldn't process that WhatsApp command.")

    elif "send imessage" in command:
        speak("Who should I send the iMessage to?")
        recipient = listen()
        speak("What would you like to say?")
        message = listen()
        if send_imessage(recipient, message):
            speak(f"Message sent to {recipient}")

    elif "read imessages" in command or "read messages" in command:
        messages = read_imessages(limit=5)
        if not messages:
            speak("No new messages, Sir.")
        else:
            for msg in messages:
                speak_long_text(f"From {msg['sender']} in {msg['chat']}: {msg['text']}")


    elif "call" in command or "facetime" in command:
        speak("Who should I call?")
        name = listen().strip()
        info = get_contact_info(name)
        if not info or not info.get("phone"):
            speak(f"Sorry Sir, I couldn’t find a number for {name}.")
            return
        phone = info["phone"]
        subprocess.run(["open", f"facetime-audio://{phone}"])
        speak(f"Calling {name} via FaceTime Audio, Sir.")


    else:
        try:
            answer_question(command)
        except:
            speak("Sorry Sir,I am not sure about that. Let me search on the web for you")
            webbrowser.open(f"https://www.google.com/search?q={command}")





def open_app(app_name):
    try:
        subprocess.run(["open", "-a", app_name])
        speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"Sorry, I couldn't open {app_name}")


def search_web_fallback(query):
    speak(f"Sorry Sir, I couldn't find exact info. I am searching on Google for {query}.")
    webbrowser.open(f"https://www.google.com/search?q={query}")


def answer_question(command):
    triggers = ["who is", "what is", "tell me about", "define", "explain", "what's"]
    query = None
    for t in triggers:
        if t in command:
            query = command.split(t, 1)[1].strip()
            break
    if not query:
        query = command.strip()
    if not query:
        speak("Sorry Sir,I didn't catch the Subject.Could you repeat?")
        return
    wikipedia.set_lang('en')
    try:
        summary = wikipedia.summary(query, sentences=2, auto_suggest=True, redirect=True)
        speak_long_text(summary)
    except wikipedia.DisambiguationError as e:
        first_choice = e.options[0] if e.options else None
        if first_choice:
            try:
                summary = wikipedia.summary(first_choice, sentences=2)
                speak(f"I found multiple results.Here is a short result for {first_choice}: {summary}")
            except Exception:
                search_web_fallback(query)
        else:
            search_web_fallback(query)
    except wikipedia.PageError:
        search_web_fallback(query)
    except Exception as ex:
        print("WIKIPEDIA ERROR", ex)
        search_web_fallback(query)

def log_app_change(msg):
    pass

def on_app_change(event):
    msg = ""
    src_path = getattr(event, "src_path", None)
    if event.event_type == "created":
        msg = f"New application installed: {Path(event.src_path).name}"

    elif event.event_type == "deleted":
        msg = f"Application deleted:{Path(event.src_path).name}"

    else:
        msg = f"Application folder updated:{Path(event.src_path).name}"

    print(f"🔍 Logged change: {msg}")
    log_app_change(msg)

    try:
        apps=get_installed_apps()
        save_apps_to_json(apps)
    except Exception as e:
        print("⚠️ Could not update app list:", e)

if __name__ == "__main__":
    main()
