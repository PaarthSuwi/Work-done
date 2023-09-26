import cv2
import dlib

def detect_facial_features_live():
    # Load the pre-trained face detector from dlib
    detector = dlib.get_frontal_face_detector()

    # Load the pre-trained facial landmark predictor
    predictor = dlib.shape_predictor('"C:\Users\paart\OneDrive\Desktop\Edit\work\faaltu bakwaas\pata nahi\racer\shape_predictor_68_face_landmarks.dat"')  # Replace with the path to the predictor file

    # Open the integrated camera (use camera index, e.g., cv2.VideoCapture(1) for the second camera)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame from BGR to RGB format (required by dlib)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces in the RGB frame
        faces = detector(rgb_frame)

        # Loop over the detected faces
        for face in faces:
            # Predict facial landmarks for each face
            landmarks = predictor(rgb_frame, face)

            # Draw circles around the eyes
            for i in range(36, 48):  # Eye landmarks are from index 36 to 47
                x, y = landmarks.part(i).x, landmarks.part(i).y
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            # Draw circles around the nose
            for i in range(27, 36):  # Nose landmarks are from index 27 to 35
                x, y = landmarks.part(i).x, landmarks.part(i).y
                cv2.circle(frame, (x, y), 2, (0, 0, 255), -1)

            # Draw circles around the lips
            for i in range(48, 68):  # Lip landmarks are from index 48 to 67
                x, y = landmarks.part(i).x, landmarks.part(i).y
                cv2.circle(frame, (x, y), 2, (255, 0, 0), -1)

        # Display the output frame with facial features
        cv2.imshow('Facial Features Detection', frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_facial_features_live()
