# TRIGGER calendar.hours == 18 and gs.location == "park" and gs.stats.get("energy", 0) >= 3
# ONCE False
# PRIORITY 5
# DESCRIPTION Optional evening stroll in the park at 18:00

label evening_stroll:
    "You enjoy a calm evening stroll in the park."
    $ gs.change_stat("energy", -1)
    $ advance_minutes(45)
    return
