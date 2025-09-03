label morning_walk:
    "You take a refreshing morning walk in the park."
    $ gs.change_stat("energy", -2)
    $ advance_minutes(30)
    return
