📌 Aishie – Advanced AI Personal Assistant
A Python-powered intelligent voice and vision assistant designed for automation, communication, and smart interaction.
🔥 Introduction
Aishie is a powerful AI-based personal assistant built using Python.
It integrates face recognition, voice commands, communication APIs, system monitoring, automation, and a custom memory engine to provide a real-time, interactive AI experience.
Aishie can see, listen, think, remember, and perform tasks for you — just like a smart AI companion.
🧠 Key Features
🔐 1. Face Recognition Security
Uses OpenCV for real-time face detection
Unlocks the system only on authorized face match
Prevents unauthorized access
🎤 2. Voice-Based Interaction
Wake words supported:
“Hey Aishie”, “Ok Aishie”, “Aishie”, “Ai”, “Hey Ai”, “Ok Ai”
Converts speech → text
Speaks naturally using Pyttsx3
Understands everyday language
💬 3. Smart Communication Hub
Aishie can manage your communication effortlessly:
📩 Send emails
📖 Read emails
💬 Send WhatsApp messages
👀 Read WhatsApp messages
📞 Make calls
📇 Fetch contact information
All handled securely through custom Python integrations.
🧠 4. Memory System
Aishie remembers:
User preferences
Task history
App changes
Important logs
Saved in:
aishie_memory.json
app_changes.json
This makes Aishie smarter every time you use it.
📱 5. System Awareness (Phase 6.5)
Aishie automatically:
Detects newly installed apps
Tracks uninstalled apps
Updates the stored app list
Notifies the user of system changes
🧰 6. Automation & Utility Commands
Aishie can perform:
Open apps (Chrome, YouTube, Terminal, Notes, etc.)
Take screenshots
Play music
Search Wikipedia
Explain topics
Answer general queries
And much more
🗂️ Project Structure
Aishie-AI-Assistant/
│── Face_scan.py
│── main.py
│── communication_hub.py
│── installed_apps.py
│── first.py
│── aishie_memory.json
│── ai phases.png
│── whatsapp_msgbox.png
│── whatsapp_search.png
│── Known Faces/
│   └── (User face images for recognition)
│── .gitignore
│── README.md
│── venv/ (ignored)
🛠️ Technology Stack
Component	Technology
Face Recognition	OpenCV
Speech Recognition	SpeechRecognition + PyAudio
Text-to-Speech	Pyttsx3
Communication	smtplib, universal links, custom WhatsApp automation
Knowledge Engine	Wikipedia API
OS Interaction	Python OS & subprocess
System Awareness	Custom installed_apps module
⚙️ How It Works
Aishie starts with face recognition
Unlocks on verified face match
Listens continuously for wake words
Converts command → text
Processes intent using the command engine
Executes communication, system tasks, or searches
Stores memory for future improvement
🔮 Future Enhancements
🌐 Cloud sync & multi-device memory
📱 Mobile app + API support
🪟 Full GUI dashboard
🧑‍💼 Multi-user profiles
🔊 Better speech recognition model
🔗 Plugin system for developers
🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss improvements.
📄 License
This project currently has no license.
Ask if you want an MIT or Apache 2.0 license generated.
👤 Author
Ansh Pratap
B.Tech CSE | AI & ML Developer
Creator of Aishie – AI Assistant
🔗 GitHub: AnshPratap2314
🔗 LinkedIn: https://www.linkedin.com/in/ansh-pratap-68156625b/
