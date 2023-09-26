import cv2
import dlib

def detect_facial_landmarks_live():
    # Load the pre-trained face detector from dlib
    detector = dlib.get_frontal_face_detector()

    # Load the pre-trained facial landmark predictor
    predictor = dlib.shape_predictor('path/to/shape_predictor_68_face_landmarks.dat')  # Replace with the path to the predictor file

    # Open the default camera (or you can specify the camera index, e.g., cv2.VideoCapture(0) for the first camera)
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale for faster processing
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = detector(gray_frame)

        # Loop over the detected faces
        for face in faces:
            # Predict facial landmarks for each face
            landmarks = predictor(gray_frame, face)
            for i in range(68):  # Assuming you are using the 68-point facial landmark predictor
                x, y = landmarks.part(i).x, landmarks.part(i).y
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        # Display the frame with facial landmarks
        cv2.imshow('Facial Landmarks Detection', frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect_facial_landmarks_live()
