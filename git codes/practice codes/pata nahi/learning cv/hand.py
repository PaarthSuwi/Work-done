import cv2,sys
import mediapipe as mp
import pygame

pygame.init()
w,h = 1000,800
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("hand tracker")
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

def main():
    run = True
    index = 0
    x1,y1=0,0
    cam = cv2.VideoCapture(index)
    points=[]
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5, max_num_hands=1)
    while run:
        ret,frame = cam.read()
        frame = cv2.resize(frame,(1000,800))
        frame = cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
        results = hands.process(frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Getting all hand points coordinates
                points = []
                for lm in hand_landmarks.landmark:
                    points.append((int(lm.x*1000 ), int(lm.y*800 )))
        if len(points) !=0 :
            x1, y1 = points[8]  # Index finger

        frame = pygame.surfarray.make_surface(frame)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(frame,(0,0))
        pygame.draw.rect(screen,(255,0,0),(y1,x1,10,10))
        pygame.display.update()

if __name__ == "__main__":
    main()