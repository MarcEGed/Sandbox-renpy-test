label sandbox_loop:
    # Process all events that trigger at this time
    $ events_processed = 0
    $ ev = get_next_event()
    while ev:
        "Event triggered: [ev.name]"
        $ renpy.call(ev.label)
        if ev.once:
            $ ev.done = True
        $ events_processed += 1
        $ ev = get_next_event()
    
    if events_processed > 0:
        jump location_menu
    else:
        "Nothing special happens."
        $ advance_hours(1)
        jump location_menu
