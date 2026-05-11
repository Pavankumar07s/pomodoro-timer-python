from datetime import datetime
import time
import csv

def pomodoro_timer(work_minutes=25, break_minutes=5, log_file='pomodoro_log.csv'):
    """
    A Pomodoro timer that logs sessions to a CSV file.

    Args:
        work_minutes (int): Duration of the work session in minutes.
        break_minutes (int): Duration of the break session in minutes.
        log_file (str): Path to the CSV file for logging sessions.
    """

    def log_session(session_type, start_time, end_time):
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            if f.tell() == 0:  # Write header only if file is empty
                writer.writerow(['Session Type', 'Start Time', 'End Time'])
            writer.writerow([session_type, start_time.isoformat(), end_time.isoformat()])
        print(f"Logged {session_type} from {start_time.strftime('%H:%M:%S')} to {end_time.strftime('%H:%M:%S')}")

    while True:
        # Work session
        print(f"Starting {work_minutes}-minute work session...")
        start_time = datetime.now()
        time.sleep(work_minutes * 60) # Simulate work
        end_time = datetime.now()
        log_session('Work', start_time, end_time)
        print("Work session finished!")

        # Break session
        print(f"Starting {break_minutes}-minute break session...")
        start_time = datetime.now()
        time.sleep(break_minutes * 60) # Simulate break
        end_time = datetime.now()
        log_session('Break', start_time, end_time)
        print("Break session finished!")

        input("Press Enter to start the next Pomodoro or Ctrl+C to exit.")

if __name__ == '__main__':
    pomodoro_timer()