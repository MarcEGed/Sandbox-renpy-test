import os

# === CONFIG ===
EVENT_FOLDER = "event_scripts"
NUM_EVENTS = 1000  # Number of days/events to generate

os.makedirs(EVENT_FOLDER, exist_ok=True)

for i in range(NUM_EVENTS):
    event_name = f"event_{i:04d}"
    filename = os.path.join(EVENT_FOLDER, f"{event_name}.rpy")

    trigger = f"calendar.total_days == {i}"

    content = f"""# AUTO-GENERATED EVENT FILE
# TRIGGER {trigger}
# PRIORITY 1
# ONCE True

label {event_name}:
    "This is {event_name}, triggered on day {i}."

    $ advance_days(1)
    $ set_hour(7)
    $ set_minute(0)
    return
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Generated {NUM_EVENTS} event files in '{EVENT_FOLDER}' with day-based triggers")
