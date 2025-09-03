label eva_date:
    "You go on a date with Eva downtown."
    $ gs.change_stat("money", -20)
    $ gs.change_stat("affection_eva", 5)
    # Date lasts 3 hours
    $ advance_hours(3)
    return
