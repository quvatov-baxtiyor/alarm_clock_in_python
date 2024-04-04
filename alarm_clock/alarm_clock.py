from datetime import datetime
import time
from playsound import playsound

def get_alarm_time():
    """Prompt the user to set a time for the alarm."""
    while True:
        alarm_time = input("Set the alarm time (HH:MM:SS AM/PM): ")
        try:
            # Try to parse the input time
            return datetime.strptime(alarm_time, "%I:%M:%S %p")
        except ValueError:
            print("Invalid time format! Please try again using HH:MM:SS AM/PM format.")

def wait_for_alarm(alarm_time):
    """Wait until the current time matches the alarm time."""
    print("Alarm set for", alarm_time.strftime("%I:%M:%S %p"))
    while True:
        now = datetime.now()
        current_time = now.replace(year=alarm_time.year, month=alarm_time.month, day=alarm_time.day)
        if current_time >= alarm_time:
            print("Wake up!")
            break
        time.sleep(1)

def play_alarm_sound():
    """Play an alarm sound."""
    # Replace 'alarm.mp3' with the path to your alarm sound file
    playsound('alarm.mp3')

if __name__ == "__main__":
    alarm_time = get_alarm_time()
    wait_for_alarm(alarm_time)
    play_alarm_sound()
