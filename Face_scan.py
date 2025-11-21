import cv2
import face_recognition
import os
import numpy as np
import time


KNOWN_FACES_DIR="known Faces"
TOLERANCE=0.45
FRAME_THICKNESS=3
FONT_THICKNESS=2
MODEL="hog"
print("🔍 Loading known faces...")

known_faces= []
known_names= []

for name in os.listdir(KNOWN_FACES_DIR):
    if name.startswith("."):
        continue
    for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
        if filename.startswith("."):
            continue
        filepath=f"{KNOWN_FACES_DIR}/{name}/{filename}"
        image=face_recognition.load_image_file(filepath)
        encodings=face_recognition.face_encodings(image)
        if len(encodings)==0:
            print(f"⚠️ No face found in {filename},skipping.")
            continue

        known_faces.append(encodings[0])
        known_names.append(name)
        print(f"✅ Face encoding added for {name}")

print("✅ Known faces loaded successfully!")
print("🎥 Starting camera...")

video=cv2.VideoCapture(0)
recognized_person=None
recognized=False
unknown_detected= False

while True:
    ret, frame=video.read()
    if not ret:
        break
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(rgb_frame,model=MODEL)
    encodings= face_recognition.face_encodings(rgb_frame, locations)

    for face_encoding, face_location in zip(encodings,locations):
        distances= face_recognition.face_distance(known_faces, face_encoding)
        name="UNKNOWN"

        if len(distances) == 0:
            continue

        best_match_index = np.argmin(distances)
        best_distance=distances[best_match_index]
        print(f"📏 Distance for {name}: {distances[best_match_index]:.3f}")

        if best_distance<=TOLERANCE:
            name=known_names[best_match_index]
            print("f📏 Match confidence for {name}: {1 - best_distance:.2f")
        else:
            print(f"⚠️ Face not recognized (distance {best_distance:.2f})")

        top_left = (face_location[3], face_location[0])
        bottom_right = (face_location[1], face_location[2])

        if name!="UNKNOWN":
            color=(0,255,0)
            cv2.rectangle(frame,top_left,bottom_right,color,FRAME_THICKNESS)
            cv2.putText(frame, name, (face_location[3], face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color,FONT_THICKNESS)

            if recognized_person != name:
                recognized_person = name
                recognized=True
                print(f"✅ Match Found: {name}")
                time.sleep(1)
                break






        else:
            print("⚠️ Unknown face detected!")
            color=(0,0,225)
            cv2.rectangle(frame, top_left,bottom_right,color , FRAME_THICKNESS)
            cv2.putText(frame,"Unknown",(face_location[3],face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6,color , FONT_THICKNESS)
            unknown_detected=True
            time.sleep(1)
            break

    if recognized or unknown_detected:
        break
    cv2.imshow("Aishie - Face Scan", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break

video.release()
cv2.destroyAllWindows()

if recognized:
    print("🧠 Face recognized successfully! Proceeding to main assistant...")
else:
    print("❌ No known faces recognized.")
