import cv2
import time

# Camera Settings
camera_width = 320 # 480 # 640 # 1024 # 1280
camera_height = 240 # 320 # 480 # 780 # 960
frameSize = (camera_width, camera_height)
video_capture = cv2.VideoCapture(0)
time.sleep(2.0)

def capture_image():
    ret, frameOrig = video_capture.read()
    frame = cv2.resize(frameOrig, frameSize)

    return frame