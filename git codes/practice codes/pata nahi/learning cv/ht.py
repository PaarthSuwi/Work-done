import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
    _, image = cap.read()
    image = cv2.flip(image, 1)
    results = hands.process(image)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx,cy = int(lm.x * w), int(lm.y * h)
                if id == 20:
                    cv2.circle(image, (cx, cy), 20, (255, 0, 255), cv2.FILLED)
                    mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
                #cv2.imshow("Output", image)


    cv2.imshow("Output", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()