import datetime
import time
import subprocess
import pyautogui

##Initially used to only be able to create one reminder
#reminder_day = "Friday"
#reminder_time = "18:32"
#reminder_text = "Submit Assignment"

#Create an array of reminders
reminders = [
    ["Friday", "22:00", "go to sleep"],
    ["Saturday", "23:00", "SLEEP!!"],
    ["Friday", "19:02", "one"],
    ["Friday", "19:03", "two"],
]

def waitUntil(r):
    while True:
        for reminder in r:
            now = datetime.datetime.now()
            current_day = now.strftime("%A")
            current_time = now.strftime("%H:%M")


            if current_day == reminder[0] and current_time == reminder[1]:
                show_reminder(reminder[2])    
        time.sleep(60)


def show_reminder(text):
    subprocess.Popen("notepad.exe")
    time.sleep(1.5)
    pyautogui.typewrite(text, interval=0.05)

waitUntil(reminders)