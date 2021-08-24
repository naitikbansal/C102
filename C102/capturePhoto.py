import cv2
import dropbox
import time
import random
start_time=time.time()
def takeSnapshot():
    number=random.randint(0,100)

    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        image_name="img"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        start_time=time.time
        result=False

    return image_name
    print("Snapshot taken!!!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFiles(image_name):
    access_token='kbFGpX5ozb8AAAAAAAAAAai49qLOhFO0LX1jWU80gU9lDL6sPJxkwkDCVEtArXrH'
    file=image_name
    file_from=file
    file_to="/testfolder/"+(image_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded!!!")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=takeSnapshot()
            uploadFiles(name)

main()