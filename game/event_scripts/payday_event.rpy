# TRIGGER calendar.total_days % 7 == 0 and gs.location == "home" and not gs.get_flag("payday_day_" + str(calendar.total_days))
# ONCE False
# PRIORITY 20
# DESCRIPTION Payday occurs every 7 days if at home

label payday_event:
    "It's payday! You receive your weekly allowance."
    $ gs.change_stat("money", 50)
    $ gs.set_flag("payday_day_" + str(calendar.total_days))  # Record this payday
    $ advance_minutes(15)
    return
