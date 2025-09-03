# TRIGGER calendar.hours == 8 and calendar.minutes == 0 and gs.location == "park" and gs.stats.get("energy", 0) > 2
# ONCE False
# PRIORITY 10
# DESCRIPTION Repeatable morning walk every day at 08:00 in the park

label morning_walk:
    "You take a refreshing morning walk in the park."
    $ gs.change_stat("energy", -2)
    $ advance_minutes(30)
    return
