import re

from talon import Module, actions

mod = Module()


@mod.action_class
class Actions:
    def cursorFiles(text_1: str, text_2: str = "", text_3: str = "", text_4: str = ""):
        """
        Opens 1-4 files in cursor
        """

        file_names = [text_1, text_2, text_3, text_4]

        # Remove any empty strings from the list
        file_names = [f for f in file_names if f]

        # move cursor to terminal
        actions.key("cmd-down")

        actions.sleep("200ms")

        # clear the terminal
        actions.key("ctrl-c")

        ## insert command
        command = "fd -g '{"
        command += ",".join(file_names)
        command += ",_" # add one final trailing comma and a placeholder, to make using alt+left / alt+right easier
        command += "}' | xargs cursor"

        actions.insert(command)

        actions.sleep("100ms")

        # move cursor back 2 words
        actions.key("alt-left " * 2)

        # move cursor back 6 spaces
        actions.key("left " * 6)