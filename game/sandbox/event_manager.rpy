init python:

    import traceback

    class Event(object):
        def __init__(self, name, label, condition_func, once=True, priority=0, description=""):
            self.name = name                # Event name
            self.label = label              # Ren'Py label to call
            self.condition_func = condition_func  # Function(gs, calendar) -> True/False
            self.once = once                # True = runs only once
            self.priority = priority        # Higher number = higher priority
            self.description = description  # Optional description
            self.done = False               # Has the event already run?


        def can_trigger(self):
            if self.once and self.done:
                return False
            try:                                    # using try to not break game
                result = self.condition_func(gs, calendar)
                if result:
                    return True
                else:
                    return False
            except Exception:
                # treat as not ready
                return False


        def eval_condition_safe(self):
            # eval for debug
            try:
                result = self.condition_func(gs, calendar)
                if result:
                    return (True, None)
                else:
                    return (False, None)
            except Exception as e:
                return (False, traceback.format_exc())


    events = []

    def register_event(event):
        # remove events with same name ((hopefully as a safety protocol))
        existing = None

        for e in events:
            if e.name == event.name:
                existing = e
                break

        if existing is not None:
            events.remove(existing)

        events.append(event)

    
    def get_next_event():
        # Get the next valid event to run
        valid_events = []

        for e in events:
            if e.can_trigger():
                valid_events.append(e)

        if len(valid_events) == 0:
            return None

        # sort by priority, then by name
        highest = valid_events[0]
        for e in valid_events[1:]:
            if e.priority > highest.priority:
                highest = e
            elif e.priority == highest.priority:
                if e.name < highest.name:  # tiebreaker using names
                    highest = e
        return highest

    
    def debug_events_print_all():
        # Print all events for debugging
        for e in events:
            ready, err = e.eval_condition_safe()
            print("EVENT:", e.name)
            print("  ready =", ready)
            print("  done =", e.done)
            print("  once =", e.once)
            print("  priority =", e.priority)
            print("  description =", e.description)
            if err is not None:
                print("  CONDITION ERROR:\n", err)
