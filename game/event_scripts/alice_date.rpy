label alice_date:
    "You go on a date with Alice downtown."
    $ gs.change_stat("money", -20)
    $ gs.change_stat("affection_alice", 5)
    # Date lasts 3 hours
    $ advance_hours(3)
    return
