label sandbox_loop:
    # Check for the next event
    $ ev = get_next_event()
    if ev:
        "Event triggered: [ev.name]"
        $ renpy.call(ev.label)
        if ev.once:
            $ ev.done = True
        jump location_menu
    else:
        "Nothing special happens."
        $ advance_hours(1)
        jump location_menu
