import datetime
import time
import subprocess
import pyautogui


reminder_day = "Friday"
reminder_time = "18:32"
reminder_text = "Submit Assignment"

def waitUntil(day, time_str):
    while True:
        now = datetime.datetime.now()
        current_day = now.strftime("%A")
        current_time = now.strftime("%H:%M")
        if current_day == day and current_time == time_str:
            return
        time.sleep(30)

def show_reminder(text):
    subprocess.Popen("notepad.exe")
    time.sleep(1.5)
    pyautogui.typewrite(text, interval=0.05)

waitUntil(reminder_day, reminder_time)
show_reminder(reminder_text)    