import os

# === CONFIG ===
EVENT_FOLDER = "event_scripts"
NUM_EVENTS = 100  # Number of days/events to generate

os.makedirs(EVENT_FOLDER, exist_ok=True)

trigger = f"calendar.total_days == 1"

for i in range(NUM_EVENTS):
    event_name = f"event_{i:04d}"
    filename = os.path.join(EVENT_FOLDER, f"{event_name}.rpy")
    priority = i

    

    content = f"""# AUTO-GENERATED EVENT FILE
# TRIGGER {trigger}
# PRIORITY {priority}
# ONCE True

label {event_name}:
    "This is {event_name}, all are triggered on day 1."

    $ advance_minutes(10)
    return
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Generated {NUM_EVENTS} event files in '{EVENT_FOLDER}' with day-based triggers")
