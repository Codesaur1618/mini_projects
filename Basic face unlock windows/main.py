import face_recognition
import ctypes
import os
import cv2

def unlock_computer():
    known_faces = []

    # Load known faces from the "faces" folder
    for filename in os.listdir('faces'):
        if filename.endswith(('.jpg', '.png')):
            face_image = face_recognition.load_image_file(os.path.join('faces', filename))
            encoding = face_recognition.face_encodings(face_image)[0]
            known_faces.append(encoding)

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_faces, face_encoding)

            if True in matches:
                # Face recognized, simulate pressing 'Enter' to unlock
                ctypes.windll.user32.keybd_event(0x0D, 0, 0, 0)  # 0x0D is the virtual key code for 'Enter'
                ctypes.windll.user32.keybd_event(0x0D, 0, 2, 0)
                break

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    unlock_computer()
