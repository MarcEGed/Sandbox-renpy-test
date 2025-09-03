screen debug_overlay():
    tag debug_overlay_tag
    frame:
        align (0.98, 0.02)  # top-right corner
        vbox:
            text "=== EVENT DEBUG ==="
            text "Time: [calendar.DaT]  Location: [gs.location]"
            text "Click an event to print details in the developer console."
            for e in events:
                $ ready, err = e.eval_condition_safe()
                $ status = "READY" if ready and (not e.done or not e.once) else ("DONE" if e.done and e.once else "LOCKED")
                textbutton "[e.name] - [status] (prio [e.priority])" action Function(print_event_debug, e)
            textbutton "Close" action Hide("debug_overlay")
