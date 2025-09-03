label payday_event:
    "It's payday! You receive your weekly allowance."
    $ gs.change_stat("money", 50)
    $ gs.set_flag("payday_day_" + str(calendar.total_days))  # Record this payday
    $ advance_minutes(15)
    return
