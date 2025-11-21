import smtplib
import ssl
import time
import webbrowser
from email.message import EmailMessage
import urllib.parse
import speech_recognition as sr
import pyautogui
import pyttsx3
import subprocess
import sys
import json
pyautogui.position()
import os
import cv2

def speak(text):
    engine=pyttsx3.init('nsss')
    engine.setProperty('rate', 175)
    voices=engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower():
            engine.setProperty('voice',voice.id)
            break
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio=recognizer.listen(source,timeout=5,phrase_time_limit=10)
            return recognizer.recognize_google(audio).lower()
        except Exception:
            return ""

def get_contact_info(name):
    applescript = f'''
        set targetName to "{name}"
        set output to ""
        tell application "Contacts"
            repeat with aPerson in people
                if name of aPerson contains targetName then
                    set emailList to value of emails of aPerson
                    set phoneList to value of phones of aPerson
                    set output to (name of aPerson) & "||" & (emailList as text) & "||" & (phoneList as text)
                    exit repeat
                end if
            end repeat
        end tell
        return output
        '''
    result=subprocess.run(["osascript","-e",applescript], capture_output=True, text=True)
    data=result.stdout.strip()
    if not data:
        return None
    try:
        name,email,phone=data.split("||")
        return {"name":name.strip(),"email":email.strip(),"phone":phone.strip()}
    except:
        return None
        
def detect_mac_theme():
    """Detect if macOS is in Light or Dark mode"""
    try:
        theme = subprocess.check_output(
            ["defaults", "read", "-g", "AppleInterfaceStyle"], text=True
        ).strip()
        return theme.lower() == "dark"
    except subprocess.CalledProcessError:
        return False

def preprocess_image(image_path, dark_mode):
    """Auto-adjust brightness & contrast depending on theme"""
    if not os.path.exists(image_path):
        return image_path
    img = cv2.imread(image_path)
    if img is None:
        return image_path


    if dark_mode:
        alpha, beta = 1.4, 50
    else:
        alpha, beta = 1.6, 10

    enhanced = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    temp_path = image_path.replace(".png", "_auto.png")
    cv2.imwrite(temp_path, enhanced)
    return temp_path


def send_whatsapp_to_contact(contact_name, message=None):
    try:
        speak(f"Opening WhatsApp to message {contact_name}, Sir.")
        subprocess.run(["open", "-a", "WhatsApp"])
        time.sleep(3)
        subprocess.run(["osascript", "-e", 'tell application "WhatsApp" to activate'])
        time.sleep(1)

        script = f'''
        tell application "System Events"
            tell application process "WhatsApp"
                try
                    set frontmost to true
                    delay 0.5
                    # Use shortcut CMD + F or CMD + K to open search
                    keystroke "f" using {{command down}}
                    delay 0.7
                    keystroke "{contact_name}"
                    delay 1
                    key code 36 -- Press Enter
                on error errMsg
                    return "error:" & errMsg
                end try
            end tell
        end tell
        '''
        result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
        if "error" in result.stdout.lower():
            print("⚠️ AppleScript search error, falling back to visual detection")

            search_ref = preprocess_image("whatsapp_search.png", False)
            search_box = pyautogui.locateCenterOnScreen(search_ref, confidence=0.6)
            if search_box:
                pyautogui.click(search_box)
                pyautogui.typewrite(contact_name)
                pyautogui.press("enter")
            else:
                speak("Sir, I couldn’t find the WhatsApp search bar. Please make sure it’s visible.")
                return False
        else:
            print("✅ Contact search succeeded via AppleScript")

        time.sleep(1.5)

        if not message:
            speak(f"What message would you like to send to {contact_name}, Sir?")
            message = listen().strip()

        if not message:
            speak("No message detected, cancelling the operation.")
            return False

        speak(f"Sir, you want me to send this message: {message}. Should I send it?")
        confirmation = listen().lower()
        if not any(word in confirmation for word in ["yes", "send", "sure", "do it", "go ahead"]):
            speak("Okay Sir, cancelled sending.")
            return False


        script_send = f'''
        tell application "System Events"
            tell application process "WhatsApp"
                try
                    set frontmost to true
                    delay 0.5
                    keystroke tab -- ensure focus on main message area
                    delay 0.2
                    keystroke "{message}"
                    delay 0.4
                    key code 36 -- Press Enter to send
                on error errMsg
                    return "error:" & errMsg
                end try
            end tell
        end tell
        '''
        result = subprocess.run(["osascript", "-e", script_send], capture_output=True, text=True)
        if "error" in result.stdout.lower():
            speak("Sir, I couldn’t send the message due to a UI focus error.")
            return False

        speak(f"Message successfully sent to {contact_name} on WhatsApp, Sir.")
        return True

    except Exception as e:
        print("⚠️ WhatsApp automation error:", e)
        speak("Sorry Sir, I couldn’t send the WhatsApp message.")
        return False


def send_email(reciever,subject,body,sender_email,app_password):
    try:
        em= EmailMessage()
        em["From"]=sender_email
        em["To"]=reciever
        em["Subject"]=subject
        em.set_content(body)

        context=ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
            smtp.login(sender_email,app_password)
            smtp.send_message(em)
        speak("Email sent succesfully, Sir")
        return True
    except Exception as e:
        print("⚠️ Email error:",e)
        speak("sorry Sir, I couldn't send the email")
        return False

def send_imessage(recipient,message):
    try:
        msg_escaped=message.replace('"','\\"')
        recipient_escaped=recipient.replace('"','\\"')

        applescript=f'''
        tell application "Messages"
        try
            set targetService to 1st service whose service type = iMessage

        on error
            set targetService to first service
        end try
        send "{msg_escaped}" to buddy "{recipient_escaped}" of targetService
        end tell'''
        result=subprocess.run(["osascript","-e",applescript], capture_output=True,  text=True)
        if result.returncode==0:
            print(f"iMessage send to {recipient}")
            return True
        else:
            print(f"iMessage failed to send to {recipient}:",result.stderr or result.stdout)
            return False
    except Exception as e:
        print("⚠️ iMessage send error:", e)
        return False

def read_imessages(limit=5):
    applescript = '''
        set output to ""
        tell application "Messages"
            set recentChats to chats
            set countChats to (count of recentChats)
            repeat with i from countChats to 1 by -1
                set theChat to item i of recentChats
                try
                    set lastMsg to last message of theChat
                    set msgText to content of lastMsg
                    set msgSender to name of sender of lastMsg
                    set chatName to name of theChat
                    set msgTime to time of lastMsg as string
                    set output to output & chatName & "|||" & msgSender & "|||" & msgText & "|||" & msgTime & "<<<END>>>"
                end try
            end repeat
        end tell
        return output
        '''
    try:
        res=subprocess.run(["osascript","-e",applescript], capture_output=True, text=True)
        raw=res.stdout.strip()
        if not raw:
            return []
        parts=raw.split("<<<END>>>")
        messages=[]
        for p in parts:
            p=p.strip()
            if not p:
                continue
            try:
                chat,sender,text_msg,time_str=[x.strip() for x in p.split("|||",3)]
            except Exception:
                continue
            messages.append({"chat":chat,"sender":sender,"text":text_msg,"time":time_str})
            if len(messages)>=limit:
                break
        return messages
    except Exception as e:
        print("⚠️ iMessage read error:", e)
        return []
def call_contact(target,use_facetime_audio=True):
    try:
        scheme= "facetime-audio" if use_facetime_audio else "facetime"
        url=f"{scheme}://{urllib.parse.quote(target, safe='@:+')}"
        subprocess.run(["open",url])
        print(f"Calling {target} via Facetime")
        return True
    except Exception as e:
        print("⚠️ FaceTime call error:", e)
        return False








