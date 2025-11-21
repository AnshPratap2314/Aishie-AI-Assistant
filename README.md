# 🚀 Aishie – Advanced AI Personal Assistant <br>
A Python-powered intelligent voice and vision assistant designed for automation, communication, and smart interaction.<br>
# 🔥 Introduction <br>
Aishie is an advanced AI-based personal assistant built using Python. <br>
## It integrates: <br>
👁️ Face Recognition <br>
🎤 Voice Commands <br>
💬 Communication Automation <br>
🧠 Memory System <br>
🗂️ System Awareness <br>
⚙️ Utility / OS Controls <br>
Aishie can see, listen, think, remember, and perform actions — just like a smart AI companion. <br>
# 🧠 Key Features <br>
🔐 1. Face Recognition Security <br>
Real-time detection using OpenCV 
Unlocks only on authorized face
Prevents unauthorized usage <br>
🎤 2. Voice-Based Interaction  <br>
Wake words supported: <br>
"Hey Aishie" <br>
"Ok Aishie" <br>
"Aishie" <br>
"Ai" <br>
"Hey Ai" <br>
"Ok Ai" <br>
Converts speech → text <br>
Responds naturally using Pyttsx3 <br>
Handles real conversational commands <br>
# 💬 3. Smart Communication Hub <br>
Aishie can: <br>
📩 Send Email <br>
📖 Read Email <br>
💬 Send WhatsApp Messages <br>
👀 Read WhatsApp Chats <br>
📞 Make Calls <br>
📇 Fetch Contact Information <br>
All handled using custom Python automation. <br>
# 🧠 4. Memory System 
Aishie remembers: <br>
User preferences <br>
Task history <br>
App changes <br>
Important logs <br>
Stored in: <br>
aishie_memory.json <br>
app_changes.json <br>
# 📱 5. System Awareness (Phase 6.5) <br>
Aishie automatically: <br>
Detects new app installations <br>
Detects app removals <br>
Updates stored app list <br>
Notifies user of changes <br>
# 🧰 6. Automation & Utility Commands <br>
Aishie can: <br>
Open apps (Chrome, YouTube, Terminal, Notes, etc.) <br>
Play music <br>
Take screenshots <br>
Search Wikipedia <br>
Explain topics <br>
Answer general queries <br>
Perform system tasks <br>
🗂️ Project Structure <br>
Aishie-AI-Assistant/ <br>
│── Face_scan.py <br>
│── main.py <br>
│── communication_hub.py <br>
│── installed_apps.py <br>
│── first.py <br>
│── aishie_memory.json <br>
│── app_changes.json  <br>
│── Known Faces/ <br>
│   └── (User face images) <br>
│── whatsapp_msgbox.png <br>
│── whatsapp_search.png <br>
│── ai phases.png <br>
│── README.md <br>
│── .gitignore <br>
│── venv/ (ignored) <br>
# 🛠️ Technology Stack <br>
<!-- Copy & paste this HTML into your README.md -->
<h2>⚙️ Component — Technology</h2>

<table style="border-collapse:collapse; width:100%; max-width:800px;">
  <thead>
    <tr>
      <th style="text-align:left; padding:8px; border-bottom:2px solid #e1e4e8;">Component</th>
      <th style="text-align:left; padding:8px; border-bottom:2px solid #e1e4e8;">Technology</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">Face Recognition</td>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">OpenCV</td>
    </tr>
    <tr>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">Speech Recognition</td>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">SpeechRecognition + PyAudio</td>
    </tr>
    <tr>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">Text-to-Speech</td>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">Pyttsx3</td>
    </tr>
    <tr>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">Communication</td>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">smtplib, custom WhatsApp automation</td>
    </tr>
    <tr>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">Knowledge Engine</td>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">Wikipedia API</td>
    </tr>
    <tr>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">OS Interaction</td>
      <td style="padding:8px; border-bottom:1px solid #f1f1f1;">Python <code>os</code> + <code>subprocess</code></td>
    </tr>
    <tr>
      <td style="padding:8px;">System Awareness</td>
      <td style="padding:8px;">Custom <code>installed_apps</code> module</td>
    </tr>
  </tbody>
</table>

<h2>⚙️ How It Works</h2>
<ol>
  <li>Performs face recognition</li>
  <li>Unlocks on verified match</li>
  <li>Listens for wake words</li>
  <li>Converts speech → text</li>
  <li>Processes intent</li>
  <li>Executes communication / automation tasks</li>
  <li>Saves memory for continuous improvement</li>
</ol>

# 🔮 Future Enhancements <br>
☁ Cloud Sync <br>
🪟 GUI Dashboard <br>
📱 Mobile App + API <br>
🧑‍💼 Multi-user Profiles  <br>
🔊 Better Speech Recognition <br>
🔌 Plugin System Support <br>
# 🤝 Contributing <br>
Pull requests are welcome! <br>
For major changes, open an issue first to discuss improvements <br>
# 📄 License — MIT License <br>
MIT License

Copyright (c) 2025 Ansh Pratap

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
# 👤 Author <br>
Ansh Pratap <br>
B.Tech CSE | AI & ML Developer <br>
Creator of Aishie – AI Assistant <br>
🔗 GitHub: AnshPratap2314 
🔗 LinkedIn: https://www.linkedin.com/in/ansh-pratap-68156625b/
