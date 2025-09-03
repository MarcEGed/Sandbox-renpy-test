init python:

    # #==============EVENT CONDITION FUNCTIONS==============

    # Event: First meeting with Eva
    def condition_meet_eva(gs, calendar):
        # Trigger on first day if player is at the park
        if calendar.total_days == 0 and gs.location == "park":
            return True
        return False

    # Event: Morning walk (repeatable)
    def condition_morning_walk(gs, calendar):
        if calendar.hours == 8 and calendar.minutes == 0 and gs.location == "park" and gs.stats.get("energy", 0) > 2:
            return True
        return False

    # Event: Eva date (requires meeting Eva and enough money)
    def condition_eva_date(gs, calendar):
        if gs.get_flag("met_eva") and gs.location == "downtown" and gs.stats.get("money", 0) >= 20:
            return True
        return False

    # Add more events here with named functions
    # Example: evening stroll
    def condition_evening_stroll(gs, calendar):
        if calendar.hours == 18 and gs.location == "park" and gs.stats.get("energy",0) >= 3:
            return True
        return False

    # Example: payday event
    def condition_payday(gs, calendar):
        # Every 7 days at home, but only once per payday
        payday_flag = "payday_day_" + str(calendar.total_days)
        if (calendar.total_days % 7 == 0 and 
            gs.location == "home" and 
            not gs.get_flag(payday_flag)):
            return True
        return False

    #==============MANUAL EVENT REGISTRATION DISABLED==============
    # Events are now loaded automatically by events_loader.rpy
    # See event_scripts/ folder for event definitions with metadata
