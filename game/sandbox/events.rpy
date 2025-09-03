init python:

    # #==============EVENT CONDITION FUNCTIONS==============

    # Event: First meeting with Alice
    def condition_meet_alice(gs, calendar):
        # Trigger on first day if player is at the park
        if calendar.total_days == 0 and gs.location == "park":
            return True
        return False

    # Event: Morning walk (repeatable)
    def condition_morning_walk(gs, calendar):
        if calendar.hours == 8 and calendar.minutes == 0 and gs.location == "park" and gs.stats.get("energy", 0) > 2:
            return True
        return False

    # Event: Alice date (requires meeting Alice and enough money)
    def condition_alice_date(gs, calendar):
        if gs.get_flag("met_alice") and gs.location == "downtown" and gs.stats.get("money", 0) >= 20:
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

    #==============REGISTER EVENTS==============

    register_event(Event(
        name="meet_alice_first",
        label="alice_intro",
        condition_func=condition_meet_alice,
        once=True,
        priority=50,
        description="First-time meeting with Alice on day 0 if at the park."
    ))

    register_event(Event(
        name="morning_walk",
        label="morning_walk",
        condition_func=condition_morning_walk,
        once=False,
        priority=10,
        description="Repeatable morning walk every day at 08:00 in the park."
    ))

    register_event(Event(
        name="alice_date_unlock",
        label="alice_date",
        condition_func=condition_alice_date,
        once=True,
        priority=30,
        description="Date with Alice when met and in downtown with enough money."
    ))

    register_event(Event(
        name="evening_stroll",
        label="evening_stroll",
        condition_func=condition_evening_stroll,
        once=False,
        priority=5,
        description="Optional evening stroll in the park at 18:00."
    ))

    register_event(Event(
        name="payday",
        label="payday_event",
        condition_func=condition_payday,
        once=False,
        priority=20,
        description="Payday occurs every 7 days if at home."
    ))
