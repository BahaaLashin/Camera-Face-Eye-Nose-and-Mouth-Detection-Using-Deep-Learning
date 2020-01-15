import cv2
from mtcnn.mtcnn import MTCNN

cap = cv2.VideoCapture(0)

detector = MTCNN()

while True:

    _,frame = cap.read()
    
    result = detector.detect_faces(frame)

    if result != [] :

        for face in result:
            x,y,w,h = face['box']
            cv2.rectangle(frame,(x,y),(x+w,h+y),[255,0,0],3)

            cv2.circle(frame,face['keypoints']['left_eye'],1,[0,255,0],-1)
            cv2.circle(frame,face['keypoints']['right_eye'],1,[0,255,0],-1)

            cv2.circle(frame,face['keypoints']['mouth_left'],1,[0,0,255],-1)
            cv2.circle(frame,face['keypoints']['mouth_right'],1,[0,0,255],-1)

            cv2.circle(frame,face['keypoints']['nose'],1,[255,0,255],-1)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 27:
        break
cap.release
cv2.destroyAllWindows()
