from talon import actions, Context, Module

from .constants import load_ls_call_script

mod = Module()

ctx = Context()
ctx.matches = r"""
tag: user.key_debug
"""


@mod.action_class
class Actions:
    def special__ls():
        """ Open nvim with a predefined function. """
        

        #  rm /tmp/.myscript.sh.swp
       # actions.insert("rm /tmp/.myscript.sh.swp\n")
        actions.sleep("50ms")
        actions.key("enter")
        actions.sleep("50ms")


        actions.auto_insert(load_ls_call_script)  


        actions.sleep("50ms")
        actions.key("enter")

        return 0