from talon import Module, actions

mod = Module()


@mod.action_class
class Actions:
    def pray(text: str):
        "Same as say but with a space at the beginning."

        actions.insert(" " + text)

    def spray(text: str):
        "Same as say but with a space at the end."

        actions.insert(text + " ")