# mod.tag("key_debug", "Keep track of which keys are held and not")

# ctx = Context()
# ctx.matches = r"""
# tag: user.key_debug
# """


from talon import Module, actions

mod = Module()


@mod.action_class
class Actions:
    def openFile(text: str):
        "Opens the file in cursor"

        is_push = False

        # if text ends with "push" then pop it
        if text.lower().endswith("push"):
            text = text[:-4]
            is_push = True

        # rm trailing periods, spaces, dashes, underscores, slashes
        text = text.rstrip(". _-/")

        actions.key("cmd-p")

        actions.insert(text)

        if is_push:
            actions.sleep("500ms")

            actions.key("enter")