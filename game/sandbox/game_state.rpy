init python:
    class GameState(object):
        def __init__(self):
            self.location = "home"
            self.stats = {
                "money": 50,
                "affection_eva": 0
            }

            self.flags = {}

        def set_flag(self, name, value=True):
            self.flags[name] = value

        def get_flag(self, name):
            return self.flags.get(name, False)

        def change_stat(self, stat, amount):
            self.stats[stat] = self.stats.get(stat, 0) + amount

    gs = GameState()
