# How to Add Content to the Game

## 🎯 Adding Events (Automatic Loading System)

The game now uses an **automatic event loading system**! Just create event files with metadata comments and they'll be loaded automatically.

### 1. Create Event Script with Metadata
Create a new file in `event_scripts/` folder with metadata comments:

```python
# event_scripts/my_event.rpy
# TRIGGER calendar.hours == 14 and gs.stats.get("money", 0) >= 100
# ONCE True
# PRIORITY 25
# DESCRIPTION My custom event at 2 PM

label my_event:
    "Something happens!"
    $ gs.change_stat("money", 50)
    $ advance_minutes(30)
    return
```

### 2. That's It!
The event will be automatically loaded and registered when the game starts. No manual registration needed!

### 📝 Metadata Comments Explained

- **`# TRIGGER`** - The condition expression (uses `gs` and `calendar` variables)
- **`# ONCE`** - `True` for one-time events, `False` for repeatable events
- **`# PRIORITY`** - Higher numbers trigger first (default: 10)
- **`# DESCRIPTION`** - Optional description for debugging

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
# TRIGGER True
# ONCE True
# PRIORITY 10
# DESCRIPTION Simple event that always triggers

label simple_event:
    "You find 25 coins!"
    $ gs.change_stat("money", 25)
    return
```

### Event with Choices
```python
# TRIGGER gs.stats.get("money", 0) >= 50
# ONCE False
# PRIORITY 15
# DESCRIPTION Job offer when you have enough money

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
# TRIGGER gs.get_flag("met_eva")
# ONCE False
# PRIORITY 5
# DESCRIPTION Eva waves when you've met her

label conditional_event:
    if gs.get_flag("met_eva"):
        "Eva waves at you!"
    else:
        "You see a stranger."
    return
```

### Time-Based Event
```python
# TRIGGER calendar.hours == 8 and calendar.minutes == 0
# ONCE False
# PRIORITY 20
# DESCRIPTION Daily morning event at 8 AM

label morning_event:
    "Good morning! Time to start your day."
    $ gs.change_stat("energy", 5)
    return
```

### Location-Based Event
```python
# TRIGGER gs.location == "park" and calendar.hours >= 10
# ONCE False
# PRIORITY 10
# DESCRIPTION Park event during daytime

label park_event:
    "You enjoy the peaceful park atmosphere."
    $ gs.change_stat("happiness", 2)
    return
```

## 🧪 Testing

### Built-in Test Menu
The game includes a comprehensive test menu accessible from the location menu:

- **⏰ Time Tests** - Jump to specific times (Day 0, Day 7, 8 AM, 6 PM)
- **📍 Location Tests** - Switch between all locations instantly
- **💰 Stat Tests** - Set money/energy to specific values
- **🎯 Event Tests** - Pre-configured scenarios for each event
- **🔍 Debug Events** - Print all event states to console
- **🧪 Test Event Loader** - Check if events are loading properly
- **🔄 Reset Game State** - Reset everything to defaults

### Manual Testing Commands
```python
# Jump to specific day/time
$ set_day(7)
$ set_hour(14)
$ gs.location = "home"

# Set stats for testing
$ gs.change_stat("money", 1000)
$ gs.change_stat("energy", 10)

# Debug events
$ debug_events_print_all()
```

## 🚀 Quick Start Checklist

- [ ] Create event script in `event_scripts/` with metadata comments
- [ ] Test the event using the built-in test menu
- [ ] Check console output for event loading confirmation
- [ ] Add any new stats to `GameState` if needed
- [ ] Use flags to prevent duplicate triggers
- [ ] Set appropriate priority for event conflicts

## 🎮 How It Works

1. **Automatic Loading** - Events are loaded from `event_scripts/` folder on game start
2. **Metadata Parsing** - Comments at the top of each file define event behavior
3. **Dynamic Registration** - Events are registered automatically with the event system
4. **Portable** - Works on any system, no hardcoded paths
5. **Git-Friendly** - Perfect for sharing projects with others

That's it! Just create your event script with metadata comments and it's automatically loaded!
