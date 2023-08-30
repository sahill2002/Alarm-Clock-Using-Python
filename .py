import time
import pytz
from datetime import datetime

print("Welcome to the Alarm Clock!")
def get_current_time():
    return datetime.now(india_timezone)


india_timezone = pytz.timezone('Asia/Kolkata')
current_time = get_current_time()
formatted_time = current_time.strftime("%H:%M")
print("CURRENT TIME:",formatted_time)


def set_alarm():
    alarm_time = input("Enter the alarm time in HH:MM format: ")
    return alarm_time

def main():
    alarm_time = set_alarm()

    while True:
        current_time = get_current_time()
        formatted_time = current_time.strftime("%H:%M")

        if formatted_time == alarm_time:
            print("Time to wake up!")
            break

        time.sleep(10)  

    print("Alarm stopped.")

if __name__ == "__main__":
    main()

