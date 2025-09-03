label evening_stroll:
    "You enjoy a calm evening stroll in the park."
    $ gs.change_stat("energy", -1)
    $ advance_minutes(45)
    return
