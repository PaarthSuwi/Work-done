# This code is designed for a computer vision application using Python's OpenCV library to interact with a webcam and control the mouse cursor. 

import cv2
import numpy as np
import pylance


def main():
    # Initialize the webcam
    camera = cv2.VideoCapture(0)

    # Initialize the frame variable
    frame = None

    # Capture the first frame from the webcam
    success, frame = camera.read()

    # If the frame was successfully captured, continue
    if success:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to the grayscale image
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Threshold the blurred image
        thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)[1]

        # Find the contours in the thresholded image
        contours, hierarchy = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea)

        # Calculate the center of the largest contour
        (x, y, w, h) = cv2.boundingRect(largest_contour)
        center = (x + w // 2, y + h // 2)

        # If the palm is open, move the cursor
        if cv2.contourArea(largest_contour) > 100:
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            pylance.move(center.x, center.y)

        # If the palm is closed, click the cursor
        else:
            cv2.circle(frame, center, 5, (255, 0, 0), -1)
            pylance.click()

        # Display the frame
        cv2.imshow('Frame', frame)

        # Wait for a key press
        key = cv2.waitKey(1)

        # If the key is ESC, quit the program
        if key == 27:
            cv2.destroyAllWindows()
            exit()

    else:
        print("Error: Unable to capture frame from webcam.")

if __name__ == '__main__':
    main()
