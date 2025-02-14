from talon import actions, Context, Module

mod = Module()

mod.tag("key_debug", "description")

ctx = Context()
ctx.matches = r"""
tag: user.key_debug
"""


@mod.action_class
class Actions:
    def quit_save():
        """ Quit vim and save the file. """

        actions.key("ctrl-[")
        actions.sleep("100ms")
        actions.insert(":wq")
        actions.key("ctrl-m") # ctrl-m is the same as enter