import datetime
import time
import pygame
import os

def alarm_time(target_time):
    pygame.mixer.init()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pygame.mixer.music.load(os.path.join(base_dir, "alarmclock.wav"))
    try:
        alarm = datetime.datetime.strptime(target_time, "%H:%M:%S").time()
        print(f"Alarm set for {alarm}")
    except ValueError:
        print("The format doesn't match!")
        return
    while True:
        now = datetime.datetime.now().replace(microsecond=0).time()
        if now == alarm:
            print("ALARM!!!")
            pygame.mixer.music.play()
            time.sleep(10)
            break
        else:
            time.sleep(1)
            print(now)


if __name__ == "__main__":
    now = datetime.datetime.now().replace(microsecond=0).time()
    print(f"Current time is {now}")
    target_time = input(
        "Enter the targeted time in hour, minute and seconds format: ")
    alarm_time(target_time)
