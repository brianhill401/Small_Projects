
import datetime
from playsound import playsound
alarm_hour = int(input("Enter the hour you want to wake up: "))
alarm_min = int(input("Enter the minute you want to wake up: "))
alarm_am = input("Do you want to wake up in the am or pm? ")

if alarm_am == "pm":
    alarm_hour += 12

while True:
    if alarm_hour == datetime.datetime.now().hour and alarm_min == datetime.datetime.now().minute:
        print("WAKE UP!")
        playsound("C:\\Users\\brian\PycharmProjects\\Exercises\\alarm_sound.wav")
        break

print("Good morning!")
