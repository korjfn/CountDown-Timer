import time
def countdowntimer(seconds):
    while seconds >= 0:
        mins = seconds // 60
        secs = seconds % 60
        time_format = f"{mins:02d}:{secs:02d}"
        print(f"⌛ timeleft: {time_format}", end = "\r")
        time.sleep(1)
        seconds -= 1
    print("\n⏰ times up!")
print("⏲️  Countdown timer")
try:
    totalseconds = int(input("Enter the number of seconds to countdown from: \n"))
    countdowntimer(totalseconds)
except ValueError:
    print("Please enter a valid number")
    