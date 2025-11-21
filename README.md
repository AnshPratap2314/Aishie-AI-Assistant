<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Aishie — Advanced AI Personal Assistant</title>
  <style>
    :root{
      --bg:#0f1724; --card:#0b1117; --muted:#9aa6b2; --accent:#6ee7b7; --accent-2:#60a5fa;
      --glass: rgba(255,255,255,0.03);
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
    }
    html,body{height:100%; margin:0; background:linear-gradient(180deg,#071029 0%, #081324 100%); color:#e6eef6}
    .container{max-width:980px;margin:40px auto;padding:28px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); border-radius:12px; box-shadow:0 10px 30px rgba(2,6,23,0.6); border:1px solid rgba(255,255,255,0.03)}
    header{display:flex;gap:16px;align-items:center}
    .logo{
      width:86px;height:86px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent-2));display:flex;align-items:center;justify-content:center;font-weight:700;color:#04263b;font-size:20px;
      box-shadow:0 6px 18px rgba(6,22,36,0.6), inset 0 -6px 18px rgba(255,255,255,0.03);
    }
    h1{margin:0;font-size:26px;letter-spacing:-0.4px}
    h2{color:var(--accent-2); margin-top:18px}
    p.lead{color:var(--muted); margin:8px 0 18px}
    .badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
    .badge{background:var(--glass);padding:6px 10px;border-radius:999px;color:var(--muted);font-size:13px;border:1px solid rgba(255,255,255,0.02)}
    .grid{display:grid;grid-template-columns:1fr 320px;gap:22px;margin-top:22px}
    .card{background:rgba(255,255,255,0.02); padding:18px;border-radius:10px;border:1px solid rgba(255,255,255,0.02)}
    ul.features{list-style:none;padding:0;margin:0}
    ul.features li{padding:8px 0;border-bottom:1px dashed rgba(255,255,255,0.03); color:var(--muted)}
    code, pre{background:#071827;padding:6px 8px;border-radius:6px;color:#bfe6d9;font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Courier New", monospace;font-size:13px}
    .section{margin-top:20px}
    .file-tree{font-family:ui-monospace, monospace;color:var(--muted); font-size:13px;background:transparent;padding:12px;border-radius:8px;border:1px dashed rgba(255,255,255,0.02)}
    footer{margin-top:26px;color:var(--muted); font-size:13px; display:flex;justify-content:space-between;align-items:center}
    a { color: var(--accent-2); text-decoration:none }
    .cta { display:inline-block; padding:8px 12px; background:linear-gradient(90deg,var(--accent),var(--accent-2)); color:#04263b; border-radius:8px; font-weight:600; text-decoration:none }
    img.screenshot{width:100%; border-radius:8px; border:1px solid rgba(255,255,255,0.03); margin-top:10px}
    @media (max-width:960px){ .grid{grid-template-columns:1fr; } .logo{width:66px;height:66px} }
  </style>
</head>
<body>
  <main class="container" role="main">
    <header>
      <div class="logo">Aishie</div>
      <div>
        <h1>Aishie — Advanced AI Personal Assistant</h1>
        <p class="lead">A Python-powered intelligent voice & vision assistant for automation, secure access, and smart interactions.</p>
        <div class="badges">
          <span class="badge">Python</span>
          <span class="badge">OpenCV</span>
          <span class="badge">SpeechRecognition</span>
          <span class="badge">Pyttsx3</span>
          <span class="badge">System Automation</span>
        </div>
      </div>
    </header>

    <div class="grid">
      <section class="card">
        <h2>Overview</h2>
        <p style="color:var(--muted)">Aishie integrates face recognition, voice commands, system-awareness, communication APIs and a lightweight memory engine to act as a real-time personal assistant that can see, listen, remember and execute tasks.</p>

        <div class="section">
          <h2>Key features</h2>
          <ul class="features">
            <li><strong>Face Recognition Security</strong> — Real-time detection via OpenCV; unlocks only for authorized faces.</li>
            <li><strong>Voice Interaction</strong> — Wake words (e.g. “Hey Aishie”), speech-to-text and natural TTS using Pyttsx3.</li>
            <li><strong>Smart Communication Hub</strong> — Send/read emails, WhatsApp messages, make calls, fetch contacts (custom Python integrations).</li>
            <li><strong>Memory System</strong> — Persists preferences and history in <code>aishie_memory.json</code> (and <code>app_changes.json</code>).</li>
            <li><strong>System Awareness (Phase 6.5)</strong> — Detects installed/uninstalled apps and notifies user automatically.</li>
            <li><strong>Automation</strong> — Launch apps, take screenshots, search, play media, run utility commands, and more.</li>
          </ul>
        </div>

        <div class="section">
          <h2>Quick start</h2>
          <p style="color:var(--muted)">(macOS, Python 3.9 environment - adjust for your platform)</p>
          <pre>
# create + activate venv
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run the assistant
python main.py
          </pre>
        </div>

        <div class="section">
          <h2>Usage & commands</h2>
          <p style="color:var(--muted)">Aishie listens for wake words and supports natural-language commands such as:</p>
          <ul class="features">
            <li>"Open Chrome", "Open Terminal", "Open YouTube"</li>
            <li>"Send WhatsApp message to [contact]"</li>
            <li>"Read my last email"</li>
            <li>"Take screenshot" / "Play music"</li>
            <li>"What apps were installed recently?"</li>
          </ul>
        </div>
      </section>

      <aside class="card">
        <h2>Project structure</h2>
        <div class="file-tree">
<pre>
Aishie-AI-Assistant/
├─ Face_scan.py
├─ main.py
├─ communication_hub.py
├─ installed_apps.py
├─ first.py
├─ aishie_memory.json
├─ app_changes.json
├─ Known Faces/
│  └─ (face images)
├─ ai phases.png
├─ whatsapp_*/*.png
├─ README.md
└─ venv/ (ignored)
</pre>
        </div>

        <div class="section">
          <h2>Tech stack</h2>
          <ul style="color:var(--muted);padding-left:14px">
            <li><strong>Face:</strong> OpenCV</li>
            <li><strong>Speech recognition:</strong> SpeechRecognition (+ PyAudio / Whisper optional)</li>
            <li><strong>TTS:</strong> pyttsx3</li>
            <li><strong>Communications:</strong> smtplib, custom WhatsApp automation</li>
            <li><strong>OS Integration:</strong> Python os & subprocess</li>
          </ul>
        </div>

        <div class="section">
          <h2>Screenshot</h2>
          <!-- local path provided; when served/converted, your system will map this file -->
          <img class="screenshot" alt="Aishie screenshot" src="file:///mnt/data/Screenshot%202025-11-22%20at%202.36.38%20AM.png" />
        </div>

        <div class="section">
          <h2>License</h2>
          <p style="color:var(--muted)">Currently no license. <a href="#license-options">Click to add a license</a> (MIT recommended for permissive usage).</p>
        </div>
      </aside>
    </div>

    <section class="card section">
      <h2>How it works (high level)</h2>
      <ol style="color:var(--muted); margin-left:16px">
        <li>Face module performs continuous detection; on match it unlocks the assistant.</li>
        <li>Assistant listens for configured wake words and captures audio input.</li>
        <li>Speech → text; command parser maps user intent to actions in the command engine.</li>
        <li>Actions call communication modules, automation scripts or knowledge lookups and then store relevant memory.</li>
      </ol>
    </section>

    <section class="card section">
      <h2>Future roadmap</h2>
      <ul class="features">
        <li>Cloud sync & multi-device memory</li>
        <li>GUI dashboard and multi-user profiles</li>
        <li>Mobile app + API</li>
        <li>Plugin system & developer SDK</li>
      </ul>

      <h2 id="license-options" style="margin-top:12px">Add a license</h2>
      <p style="color:var(--muted)">Choose one and drop into a <code>LICENSE</code> file:</p>
      <pre>
# MIT (recommended for most personal projects)
MIT License

# or Apache 2.0 (stronger patent protections)
Apache License 2.0
      </pre>
    </section>

    <footer>
      <div>
        <strong>Author</strong> — Ansh Pratap • B.Tech CSE • AI & ML Developer
        <br>
        <a href="https://github.com/AnshPratap2314" target="_blank">GitHub: AnshPratap2314</a> •
        <a href="https://www.linkedin.com/in/ansh-pratap-68156625b/" target="_blank">LinkedIn</a>
      </div>
      <div>
        <a class="cta" href="https://github.com/AnshPratap2314/Aishie-AI-Assistant" target="_blank">View on GitHub</a>
      </div>
    </footer>
  </main>
</body>
</html>
