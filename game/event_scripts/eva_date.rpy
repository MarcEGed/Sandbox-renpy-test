# TRIGGER gs.get_flag("met_eva") and gs.location == "downtown" and gs.stats.get("money", 0) >= 20
# ONCE True
# PRIORITY 30
# DESCRIPTION Date with Eva when met and in downtown with enough money

label eva_date:
    "You go on a date with Eva downtown."
    $ gs.change_stat("money", -20)
    $ gs.change_stat("affection_eva", 5)
    # Date lasts 3 hours
    $ advance_hours(3)
    return
