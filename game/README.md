# How to Add Content to the Game

## 🎯 Adding Events

### 1. Create Event Script
Create a new file in `event_scripts/` folder:

```python
# event_scripts/my_event.rpy
label my_event:
    "Something happens!"
    $ gs.change_stat("money", 50)
    $ advance_minutes(30)
    return
```

### 2. Add Condition Function
In `sandbox/events.rpy`, add a condition function:

```python
def condition_my_event(gs, calendar):
    # Example: Trigger at 2 PM if player has money
    if calendar.hours == 14 and gs.stats.get("money", 0) >= 100:
        return True
    return False
```

### 3. Register the Event
In `sandbox/events.rpy`, add the event registration:

```python
register_event(Event(
    name="my_event",
    label="my_event", 
    condition_func=condition_my_event,
    once=True,
    priority=25,
    description="My custom event at 2 PM."
))
```

## 🏠 Adding Locations

In `sandbox/locations.rpy`, add new menu options:

```python
menu:
    "Go to Library":                    # New location
        $ gs.location = "library"
        $ advance_minutes(20)
        jump sandbox_loop
```

## 📊 Adding Stats

In `sandbox/game_state.rpy`, add new stats:

```python
self.stats = {
    "money": 50,
    "energy": 10,
    "happiness": 5,      # New stat
    "stress": 2          # New stat
}
```

## 🎮 Common Commands

```python
# Change stats
$ gs.change_stat("money", 50)     # Add 50 money
$ gs.change_stat("energy", -2)    # Subtract 2 energy

# Set/get flags
$ gs.set_flag("met_eva")        # Set flag to True
$ gs.get_flag("met_eva")        # Returns True/False

# Change time
$ advance_hours(2)                # Advance 2 hours
$ set_day(7)                      # Jump to day 7
$ set_hour(8)                     # Set to 8:00 AM
```

## 📝 Event Examples

### Simple Event
```python
label simple_event:
    "You find 25 coins!"
    $ gs.change_stat("money", 25)
    return
```

### Event with Choices
```python
label choice_event:
    "A stranger offers you a job."
    
    menu:
        "Accept":
            "You earn 100 coins!"
            $ gs.change_stat("money", 100)
        "Decline":
            "You walk away."
    
    return
```

### Conditional Event
```python
label conditional_event:
    if gs.get_flag("met_eva"):
        "Eva waves at you!"
    else:
        "You see a stranger."
    return
```

## 🧪 Testing

```python
# Jump to specific day/time
$ set_day(7)
$ set_hour(14)
$ gs.location = "home"

# Set stats for testing
$ gs.change_stat("money", 1000)
$ gs.change_stat("energy", 10)
```

That's it! Create your event script, add the condition, register it, and you're done!
