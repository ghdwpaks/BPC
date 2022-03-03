import cv2
import os
import time
import tkinter 

path = "./imgs"
file_list = os.listdir(path)
print("type(file_list) :",type(file_list))
print ("file_list: {}".format(file_list))




root = tkinter.Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()
print("width x height = %d x %d (pixels)" %(monitor_width, monitor_height))

for i in file_list :
    print("i :",i)
    print("imgs/"+str(i))
    image = cv2.imread("./imgs/"+str(i), cv2.IMREAD_ANYCOLOR)
    h, w, c = image.shape

    '''
    cv2.moveWindow('video3', x3, y3)  # Location of Drone
    cv2.namedWindow('video3', cv2.WINDOW_NORMAL)  # custom size or full size
    cv2.resizeWindow("video3", int(width_3), int(height_3))  # size
    cv2.setWindowProperty('video3', cv2.WND_PROP_FULLSCREEN, 1)
    cv2.imshow('video3', frame3)
    '''
    
    
    '''
    cv2.namedWindow('video3', cv2.WINDOW_NORMAL)  # custom size or full size
    cv2.resizeWindow("video3", int(500), int(500))  # size
    cv2.setWindowProperty('video3', cv2.WND_PROP_FULLSCREEN, 1)
    '''

    cv2.imshow("ghdwpaks", image)
    cv2.moveWindow('ghdwpaks', monitor_width//2-(w//2), monitor_height//2-(h//2))  # Location of Drone
    cv2.setWindowProperty('ghdwpaks', cv2.WND_PROP_FULLSCREEN, 1)

    cv2.waitKey(1000)
    cv2.destroyAllWindows()
    







