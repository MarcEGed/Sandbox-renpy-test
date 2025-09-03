# TRIGGER gs.stats.get("money", 0) >= 100
# ONCE True
# PRIORITY 15
# DESCRIPTION Test event that triggers when you have 100+ money

label test_event:
    "🎉 Test Event Triggered!"
    "You have [gs.stats.get('money', 0)] money, which is enough to trigger this test event!"
    "This event was loaded automatically by the events_loader system."
    $ gs.change_stat("money", -50)
    "You spent 50 money on something fancy!"
    $ advance_minutes(15)
    return
