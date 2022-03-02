import cv2
import random
import time
start = time.time()
def capture():
    img = cv2.VideoCapture(0)
    active = True
    number = random.randint(0,100)
    while active:
        ret,frame = img.read()
        name = "img"+str(number)+".png"
        cv2.imwrite(name,frame)
        start = time.time()
        active = False
    img.release()
    cv2.destroyAllWindows()
    print("Picture taken.")
    return name

import dropbox
def upload(name):
    dbx = dropbox.Dropbox("sl.BDCb-lnvF-8mXQf6_kZEmgKbtj3fKpz6jbhcKeB2esr2ykaeD2AbowFAWv4K3BWDccpqbIER8k77JDG539nqq2n3JW71kru583vR6tCeHwOkfEcLhWcjAhXgxX7V69SkToX8BNU")
    with open(name,"rb")as f:
        dbx.files_upload(f.read(),"/"+name)
        print("Image uploaded.")
while True:
    if((time.time()-start)>=5):
        name = capture()
        upload(name)