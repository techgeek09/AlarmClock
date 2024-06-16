import tkinter as tk
import time
import winsound  # For playing a simple beep sound


def set_alarm():

    alarm_time = entry.get()
    try:
        # Parse the alarm time in HH:MM format
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
        if 0 <= alarm_hour <= 23 and 0 <= alarm_minute <= 59:
            return alarm_hour, alarm_minute
        else:
            raise ValueError
    except ValueError:
        return None


def check_alarm():
    alarm = set_alarm()
    if alarm is None:
        status_label.config(text="Invalid time format (HH:MM)")
        return

    status_label.config(text=f"Alarm set for {alarm[0]:02d}:{alarm[1]:02d}")

    while True:
        current_time = time.localtime()
        if current_time.tm_hour == alarm[0] and current_time.tm_min == alarm[1]:
            status_label.config(text="Time to wake up!")
            winsound.Beep(1000, 1000)  # Beep for 1 second
            break
        else:
            time.sleep(60)  # Check every minute


# Create the main window
root = tk.Tk()
root.title("Alarm Clock")

# Create and configure widgets
label = tk.Label(root, text="Enter alarm time (HH:MM):")
entry = tk.Entry(root)
set_button = tk.Button(root, text="Set Alarm", command=check_alarm)
status_label = tk.Label(root, text="")

# Place widgets in the window
label.pack()
entry.pack()
set_button.pack()
status_label.pack()

root.mainloop()

