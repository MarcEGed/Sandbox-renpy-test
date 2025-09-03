label location_menu:
    "Where do you want to go? (Current: [gs.location], Time: [calendar.DaT])"

    menu:
        "Stay Home":
            $ gs.location = "home"
            $ advance_hours(1)
            jump sandbox_loop

        "Go to Park":
            $ gs.location = "park"
            $ advance_minutes(30)
            jump sandbox_loop

        "Go to Downtown":
            $ gs.location = "downtown"
            $ advance_minutes(45)
            jump sandbox_loop

        "Go to Work":
            $ gs.location = "work"
            $ gs.change_stat("money", 10)
            $ advance_hours(4)
            jump sandbox_loop

        "Rest at Home":
            $ gs.location = "home"
            $ gs.change_stat("energy", 5)
            $ advance_days(1)
            $ set_hour(7)
            $ set_minute(0)
            jump sandbox_loop

        "🧪 Test Menu":
            jump test_menu
