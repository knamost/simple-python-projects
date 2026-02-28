"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""


import time

while True:
    try:
        seconds = int(input("⏰ Enter the time in second(s): "))
        if seconds < 1:
            print("Please enter a number greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input, please enter a whole number..")
        
print("\n🔔 Timer started....")        
for remaining in range(seconds, 0, -1):     # stop: 0, step: -1, so we go backwards, if seconds is 10, then 9, 8, 7...
    mins, secs = divmod(remaining, 60)
    time_format = f"{mins:02}:{secs:02}"    # 
    print(f"⌚ Time left: {time_format}", end="\r")
    time.sleep(1)
    
print("\nTime's up! Take a break or move to next tasks..")
print("\a") # optional; makes a beep sound