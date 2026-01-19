from datetime import datetime, timedelta

# Current date and time
now = datetime.now()
print("Current date and time:", now)

# Tomorrow's date
tomorrow = now + timedelta(days=1)
print("Tomorrow's date:", tomorrow.date())

# Countdown example: 1 hour from now
future = now + timedelta(hours=1)
print("1 hour later:", future.time())