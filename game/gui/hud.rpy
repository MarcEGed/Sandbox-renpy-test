screen hud():
    frame:
        align (0.01, 0.01)
        xmaximum 360
        vbox:
            text "Time: [calendar.DaT]"
            text "Location: [gs.location]"
            text "Energy: [gs.stats.get('energy',0)]  Money: [gs.stats.get('money',0)]"
            text "Affection (Alice): [gs.stats.get('affection_alice',0)]"
            textbutton "Debug" action ShowMenu("debug_overlay")

init python:
    try:
        config.overlay_screens.append("hud")
    except Exception:
        pass
