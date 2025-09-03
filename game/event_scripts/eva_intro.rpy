label eva_intro:
    scene black with fade
    "You go to the park and meet Eva for the first time."
    "You have a short chat and feel like you might see her again."
    $ gs.set_flag("met_eva", True)
    $ gs.change_stat("affection_eva", 1)
    # Advance time 1 hour
    $ advance_hours(1)
    return
