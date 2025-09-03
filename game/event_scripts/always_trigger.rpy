# TRIGGER True
# ONCE True
# PRIORITY 100
# DESCRIPTION Test event that always triggers

label always_trigger:
    "🎉 ALWAYS TRIGGER EVENT WORKS!"
    "This event should always trigger to test the events_loader system."
    "If you see this, the events_loader is working correctly!"
    $ advance_minutes(5)
    return
