# from talon import Module, Context, actions, ctrl

# mod = Module()

# # mod.tag("key_debug", "Keep track of which keys are held and not")

# ctx = Context()

# ctx.matches = r"""
# os: mac
# """

# held = set()

# custom_modifiers = {
#     "alt": "alt",
#     "alter": "alt",
#     "chum": "cmd",
#     "command": "cmd",
    
#     "control": "ctrl",
#     "troll": "ctrl",
    
#     "shift": "shift",
#     "sky": "shift",
    
#     "super": "super",
    
#     "scram": "cmd-shift",
#     "shop": "alt-shift",
#     "sholl": "ctrl-shift",

#     "cot": "alt-ctrl",
#     "salt": "alt-cmd",

#     "cash": "cmd-alt-shift"
# }



# ctx.lists["self.modifier_key"] = custom_modifiers