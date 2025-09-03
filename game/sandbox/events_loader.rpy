init python:

    import os
    import re

    EVENT_FOLDER = os.path.join(renpy.config.basedir, "game", "event_scripts")

    print(f"Event folder (relative): {EVENT_FOLDER}")

    meta_patterns = {
        "TRIGGER": re.compile(r"# TRIGGER (.+)"),
        "ONCE": re.compile(r"# ONCE (.+)"),
        "PRIORITY": re.compile(r"# PRIORITY (.+)"),
        "DESCRIPTION": re.compile(r"# DESCRIPTION (.+)")
    }

    def load_events():
        try:
            if not os.path.exists(EVENT_FOLDER):
                print(f"Warning: Event folder '{EVENT_FOLDER}' not found. No events will be auto-loaded.")
                return
                
            for file in os.listdir(EVENT_FOLDER):
                if not file.endswith(".rpy"):
                    continue

                event_name = file.replace(".rpy", "")
                filepath = os.path.join(EVENT_FOLDER, file)

                # Default values
                trigger_expr = "True"
                once = True
                priority = 10
                description = f"Auto-registered event {event_name}"

                # Read metadata
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        for line in f:
                            line = line.strip()
                            if not line.startswith("#"):
                                break
                            for key, pattern in meta_patterns.items():
                                m = pattern.match(line)
                                if m:
                                    if key == "TRIGGER":
                                        trigger_expr = m.group(1)
                                    elif key == "ONCE":
                                        once = eval(m.group(1))
                                    elif key == "PRIORITY":
                                        priority = int(m.group(1))
                                    elif key == "DESCRIPTION":
                                        description = m.group(1)

                    # Create condition function using gs and calendar
                    def make_condition(expr):
                        return lambda gs, calendar: eval(expr, {"gs": gs, "calendar": calendar})

                    condition_func = make_condition(trigger_expr)

                    # Register event
                    register_event(Event(
                        name = event_name,
                        label = event_name,
                        condition_func = condition_func,
                        once = once,
                        priority = priority,
                        description = description
                    ))
                    print(f"Loaded event: {event_name}")
                    
                except Exception as e:
                    print(f"Error loading event {event_name}: {e}")
                    
        except Exception as e:
            print(f"Error in load_events(): {e}")

    print("=== EVENTS LOADER STARTING ===")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Looking for events in: {EVENT_FOLDER}")
    print(f"Full path: {os.path.abspath(EVENT_FOLDER)}")
    load_events()
    print("=== EVENTS LOADER FINISHED ===")
