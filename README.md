🚀 Aishie – Advanced AI Personal Assistant
A Python-powered intelligent voice and vision assistant designed for automation, communication, and smart interaction.
🔥 Introduction
Aishie is an advanced AI-based personal assistant built using Python.
It integrates:
👁️ Face Recognition
🎤 Voice Commands
💬 Communication Automation
🧠 Memory System
🗂️ System Awareness
⚙️ Utility / OS Controls
Aishie can see, listen, think, remember, and perform actions — just like a smart AI companion.
🧠 Key Features
🔐 1. Face Recognition Security
Real-time detection using OpenCV
Unlocks only on authorized face
Prevents unauthorized usage
🎤 2. Voice-Based Interaction
Wake words supported:
"Hey Aishie"
"Ok Aishie"
"Aishie"
"Ai"
"Hey Ai"
"Ok Ai"
Converts speech → text
Responds naturally using Pyttsx3
Handles real conversational commands
💬 3. Smart Communication Hub
Aishie can:
📩 Send Email
📖 Read Email
💬 Send WhatsApp Messages
👀 Read WhatsApp Chats
📞 Make Calls
📇 Fetch Contact Information
All handled using custom Python automation.
🧠 4. Memory System
Aishie remembers:
User preferences
Task history
App changes
Important logs
Stored in:
aishie_memory.json
app_changes.json
📱 5. System Awareness (Phase 6.5)
Aishie automatically:
Detects new app installations
Detects app removals
Updates stored app list
Notifies user of changes
🧰 6. Automation & Utility Commands
Aishie can:
Open apps (Chrome, YouTube, Terminal, Notes, etc.)
Play music
Take screenshots
Search Wikipedia
Explain topics
Answer general queries
Perform system tasks
🗂️ Project Structure
Aishie-AI-Assistant/
│── Face_scan.py
│── main.py
│── communication_hub.py
│── installed_apps.py
│── first.py
│── aishie_memory.json
│── app_changes.json
│── Known Faces/
│   └── (User face images)
│── whatsapp_msgbox.png
│── whatsapp_search.png
│── ai phases.png
│── README.md
│── .gitignore
│── venv/ (ignored)
🛠️ Technology Stack
Component	Technology
Face Recognition	OpenCV
Speech Recognition	SpeechRecognition + PyAudio
Text-to-Speech	Pyttsx3
Communication	smtplib, custom WhatsApp automation
Knowledge Engine	Wikipedia API
OS Interaction	Python OS + subprocess
System Awareness	Custom installed_apps module
⚙️ How It Works
Performs face recognition
Unlocks on verified match
Listens for wake words
Converts speech → text
Processes intent
Executes communication / automation tasks
Saves memory for continuous improvement
🔮 Future Enhancements
☁ Cloud Sync
🪟 GUI Dashboard
📱 Mobile App + API
🧑‍💼 Multi-user Profiles
🔊 Better Speech Recognition
🔌 Plugin System Support
🤝 Contributing
Pull requests are welcome!
For major changes, open an issue first to discuss improvements
📄 License — MIT License
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
👤 Author
Ansh Pratap
B.Tech CSE | AI & ML Developer
Creator of Aishie – AI Assistant
🔗 GitHub: AnshPratap2314
🔗 LinkedIn: https://www.linkedin.com/in/ansh-pratap-68156625b/
