import cv2
import numpy as np

ac = cv2.VideoCapture('acsend.avi')   # Your Vidie Directory Link
de = cv2.VideoCapture('desend.avi')   # Your Video Directory Link

ac_width = ac.get(cv2.CAP_PROP_FRAME_WIDTH)
ac_height = ac.get(cv2.CAP_PROP_FRAME_HEIGHT)

de_width = de.get(cv2.CAP_PROP_FRAME_WIDTH)
de_height = de.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("size : {0} x {1}".format(ac_width, ac_height))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
ac_writer = cv2.VideoWriter('acsendedge.avi', fourcc, 24.0, (int(ac_width), int(ac_height)))
de_writer = cv2.VideoWriter('desendedge.avi', fourcc, 24.0, (int(de_width) ,int(de_height)))

def write_acsend():
    ret, ac_frame = ac.read()
    if ret:
        ac_gaussian = cv2.GaussianBlur(ac_frame, (5, 5), 1.0)
        ac_canny = cv2.Canny(ac_gaussian, 50, 100)
        #cv2.imshow('ac_canny', ac_canny)
        ac_writer.write(ac_canny)
        return ac_canny
        
def write_desend():
    ret, de_frame = de.read()
    if ret:
        de_gaussian = cv2.GaussianBlur(de_frame, (5, 5), 1.0)
        de_canny = cv2.Canny(de_gaussian, 50, 100)
        #cv2.imshow('de_canny', de_canny)
        de_writer.write(de_canny)
        return de_canny
        
point = ''
while True:
    while ac.isOpened():
        ac_out = write_acsend()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else :
            cv2.imshow('acsend_result', ac_out)
        # PLZ : Press 'q' Until End Saving Video    
         
    while de.isOpened():
        de_out = write_desend()
        cv2.imshow('desend_result', de_out)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        else :
            cv2.imshow('acsend_result', de_out)
    ac.release()
    de.release()
    cv2.destroyAllWindows()
    break
