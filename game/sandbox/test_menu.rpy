label test_menu:
    "🧪 Event Testing Menu"
    "Current: [gs.location], Time: [calendar.DaT]"
    "Money: [gs.stats.get('money', 0)], Energy: [gs.stats.get('energy', 0)]"

    menu:
        "⏰ Time Tests":
            jump time_tests

        "📍 Location Tests":
            jump location_tests

        "💰 Stat Tests":
            jump stat_tests

        "🎯 Event Tests":
            jump event_tests

        "🔍 Debug Events":
            $ debug_events_print_all()
            "Check console for event debug info!"
            jump test_menu

        "🧪 Test Event Loader":
            jump test_event_loader

        "🔄 Reset Game State":
            jump reset_game_state

        "← Back to Game":
            jump location_menu

label time_tests:
    "⏰ Time Testing"
    "Current: [calendar.DaT]"

    menu:
        "Set to Day 0 (Eva Intro)":
            $ set_day(0)
            $ set_hour(8)
            $ set_minute(0)
            "Set to Day 0, 8:00 AM"
            jump test_menu

        "Set to Day 7 (Payday)":
            $ set_day(7)
            $ set_hour(7)
            $ set_minute(0)
            "Set to Day 7, 7:00 AM"
            jump test_menu

        "Set to 8:00 AM (Morning Walk)":
            $ set_hour(8)
            $ set_minute(0)
            "Set to 8:00 AM"
            jump test_menu

        "Set to 6:00 PM (Evening Stroll)":
            $ set_hour(18)
            $ set_minute(0)
            "Set to 6:00 PM"
            jump test_menu

        "← Back":
            jump test_menu

label location_tests:
    "📍 Location Testing"
    "Current: [gs.location]"

    menu:
        "Go to Park":
            $ gs.location = "park"
            "Set location to park"
            jump test_menu

        "Go to Downtown":
            $ gs.location = "downtown"
            "Set location to downtown"
            jump test_menu

        "Go to Home":
            $ gs.location = "home"
            "Set location to home"
            jump test_menu

        "Go to Work":
            $ gs.location = "work"
            "Set location to work"
            jump test_menu

        "← Back":
            jump test_menu

label stat_tests:
    "💰 Stat Testing"
    "Money: [gs.stats.get('money', 0)], Energy: [gs.stats.get('energy', 0)]"

    menu:
        "Set Money to 100":
            $ gs.change_stat("money", 100 - gs.stats.get("money", 0))
            "Money set to 100"
            jump test_menu

        "Set Energy to 10":
            $ gs.change_stat("energy", 10 - gs.stats.get("energy", 0))
            "Energy set to 10"
            jump test_menu

        "Set Money to 0":
            $ gs.change_stat("money", -gs.stats.get("money", 0))
            "Money set to 0"
            jump test_menu

        "Set Energy to 0":
            $ gs.change_stat("energy", -gs.stats.get("energy", 0))
            "Energy set to 0"
            jump test_menu

        "Add 50 Money":
            $ gs.change_stat("money", 50)
            "Added 50 money"
            jump test_menu

        "Add 5 Energy":
            $ gs.change_stat("energy", 5)
            "Added 5 energy"
            jump test_menu

        "← Back":
            jump test_menu

label event_tests:
    "🎯 Event Testing"
    "Test specific event scenarios"

    menu:
        "Test Eva Intro (Day 0, Park)":
            $ set_day(0)
            $ set_hour(8)
            $ set_minute(0)
            $ gs.location = "park"
            "Set up for Eva intro event"
            jump test_menu

        "Test Eva Date (Met Eva, Downtown, 100+ Money)":
            $ gs.set_flag("met_eva", True)
            $ gs.location = "downtown"
            $ gs.change_stat("money", 100 - gs.stats.get("money", 0))
            "Set up for Eva date event"
            jump test_menu

        "Test Payday (Day 7, Home)":
            $ set_day(7)
            $ set_hour(7)
            $ set_minute(0)
            $ gs.location = "home"
            "Set up for payday event"
            jump test_menu

        "Test Morning Walk (8 AM, Park, High Energy)":
            $ set_hour(8)
            $ set_minute(0)
            $ gs.location = "park"
            $ gs.change_stat("energy", 10 - gs.stats.get("energy", 0))
            "Set up for morning walk event"
            jump test_menu

        "Test Evening Stroll (6 PM, Park, High Energy)":
            $ set_hour(18)
            $ set_minute(0)
            $ gs.location = "park"
            $ gs.change_stat("energy", 10 - gs.stats.get("energy", 0))
            "Set up for evening stroll event"
            jump test_menu

        "← Back":
            jump test_menu

label reset_game_state:
    "🔄 Reset Game State"
    "This will reset all flags and stats to default values."

    menu:
        "Yes, Reset Everything":
            $ gs.location = "home"
            $ gs.stats = {"money": 50, "energy": 10, "affection_eva": 0}
            $ gs.flags = {}
            $ set_day(0)
            $ set_hour(8)
            $ set_minute(0)
            "Game state reset to defaults!"
            jump test_menu

        "No, Keep Current State":
            jump test_menu

label test_event_loader:
    "🧪 Testing Event Loader"
    "Let's check if events are being loaded properly..."
    
    python:
        print("=== EVENT LOADER TEST ===")
        print(f"Total events registered: {len(events)}")
        for i, event in enumerate(events):
            print(f"Event {i+1}: {event.name}")
            print(f"  Label: {event.label}")
            print(f"  Once: {event.once}")
            print(f"  Priority: {event.priority}")
            print(f"  Done: {event.done}")
            print(f"  Description: {event.description}")
            
            # Test the condition
            ready, err = event.eval_condition_safe()
            print(f"  Ready: {ready}")
            if err:
                print(f"  Error: {err}")
            print()
    
    "Check the console output above for event details!"
    "If you see 0 events, the events_loader isn't working."
    "If you see events but they're not ready, check the conditions."
    
    menu:
        "Test Simple Event (100+ Money)":
            $ gs.change_stat("money", 100 - gs.stats.get("money", 0))
            "Money set to 100. Try going back to the game now!"
            jump test_menu
            
        "Force Trigger Test Event":
            $ renpy.call("test_event")
            jump test_menu
            
        "← Back":
            jump test_menu
