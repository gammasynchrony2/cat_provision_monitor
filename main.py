import PySimpleGUI as sg
from functions.send_email import send_email
from functions.capture_image import capture_image
import time
import cv2

# Times To Send Image
send_times = ["09:00", "17:00", "20:22"]

# Initialize Mode State
is_test_mode = True
step_update = 20

sg.theme('Dark Amber')

# Define Components
clock = sg.Text('', key='clock')
app_title = sg.Text('Mode Select', key="title")
video_feed = sg.Image(filename="", key="cam1")
setup_mode_button = sg.Button("Camera Setup", key="test_button", size=[18, 1])
monitor_mode_button = sg.Button("Begin Monitoring", key="monitor_button", size=[19, 1])
exit_button = sg.Exit(size=39)

layout = [[clock],
          [app_title],
          [setup_mode_button, monitor_mode_button],
          [video_feed],
          [exit_button]]

window = sg.Window("Pet Provision Monitoring", layout,
                   no_titlebar=False, alpha_channel=1, grab_anywhere=False,
                   return_keyboard_events=True, location=(100, 100))

while True:
    event, values = window.read(timeout=step_update)
    print(event, values)

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == "test_button":
        is_test_mode = True
    elif event == "monitor_button":
        is_test_mode = False

    if is_test_mode == True:
        step_update = 20
        window['clock'].update(value=time.strftime("%A %b %d, %Y %H:%M:%S"))

        frame = capture_image()
        imgbytes = cv2.imencode(".png", frame)[1].tobytes()
        window['cam1'].update(data=imgbytes)
    elif is_test_mode == False:
        step_update = 1000 * 60
        window['cam1'].update(filename="monitoring.png")
        if time.strftime("%H:%M") in send_times:
            frame = capture_image()
            cv2.imwrite("current_image.png", frame)
            send_email("current_image.png")

cv2.VideoCapture(0).release()
cv2.destroyAllWindows()