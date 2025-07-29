# ⏲️ Countdown Timer in Python

A simple command-line countdown timer written in Python. Just input the number of seconds you'd like to count down from, and watch the timer tick down to zero!

## 🔧 Features

- Clean and minimalistic CLI interface
- Displays countdown in `MM:SS` format
- Uses `time.sleep()` to simulate real-time countdown
- Shows final message when time is up

## 📦 Requirements

- Python 3.x

No external libraries are needed — everything is handled with Python’s built-in `time` module.

## 🚀 How to Run

1. Clone the repository or download the script:

   ```bash
   git clone https://github.com/your-username/countdown-timer.git
   cd countdown-timer
````

2. Run the script:

   ```bash
   python countdown_timer.py
   ```

3. Enter the number of seconds to count down from when prompted.

## 🧪 Example

```text
⏲️  Countdown timer
Enter the number of seconds to countdown from: 
30
⌛ timeleft: 00:30
⌛ timeleft: 00:29
...
⏰ times up!
```

## ❗ Error Handling

* If you enter a non-integer value, the script will display an error message and exit gracefully.

## 🛠️ Code Overview

```python
def countdowntimer(seconds):
    while seconds >= 0:
        mins = seconds // 60
        secs = seconds % 60
        time_format = f"{mins:02d}:{secs:02d}"
        print(f"⌛ timeleft: {time_format}", end = "\r")
        time.sleep(1)
        seconds -= 1
    print("\n⏰ times up!")
```

## 📄 License

This project is licensed under the MIT License.

---

Feel free to contribute or modify the script to include features like sound alerts or GUI!
