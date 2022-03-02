import cv2
def capture():
    img = cv2.VideoCapture(0)
    active = True
    while active:
        ret,frame = img.read()
        cv2.imwrite("img1.png",frame)
        active = False
    img.release()
    cv2.destroyAllWindows()
capture()