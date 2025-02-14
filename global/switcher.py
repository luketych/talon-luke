from talon import actions, Context, Module

ctx = Context()
mod = Module()


class Switcher:
    def __init__(self):
        self.state = 1

    def toggle(self):
        if self.state == 1:
            actions.key("escape alt-tab")
            self.state = 2
        elif self.state == 2:
            actions.key("escape fn-tab")
            self.state = 1



switcher = Switcher()

@mod.action_class
class Actions:
    def toggle_switcher():
        "docstring"

        switcher.toggle()