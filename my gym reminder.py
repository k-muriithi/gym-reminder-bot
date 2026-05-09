import schedule
import time
from plyer import notification

def send_gym_reminder():
    """
    Triggers the desktop notification.
    """
    notification.notify(
        title="Time to hit the Gym",
        message="It's 6:00 AM.",
        app_name="Gym Reminder",
        timeout=120  # The notification stays for 2 minutes
    )
    print("Notification sent successfully.")

# Schedule the task for 6:00 AM every day
schedule.every().day.at("06:00").do(send_gym_reminder)

print("Gym reminder service is running... (Press Ctrl+C to stop)")

# Keep the script running in the background
while True:
    schedule.run_pending()
    time.sleep(30)  # Check every 30 seconds to save CPU resources