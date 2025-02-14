from talon import actions, ctrl, Context, Module

mod = Module()

mod.tag("key_debug", "description")

ctx = Context()
ctx.matches = r"""
tag: user.key_debug
"""




@mod.action_class
class Actions:
    def go_slash(num_slashes: int = 1):
        """
        Moves cursor to the nth slash on the current line.
        
        Args:
            num_slashes: The nth slash to move to (default: 1)
            
        Returns:
            0 on success
        """

        # print("num_slashes: ", num_slashes)
        
        # # # start at the beginning of the line
        # actions.key("ctrl-a")

        num_slashes_found = 0

        # #while num_slashes_found < num_slashes:
        # actions.key("right")

        #res = actions.user.dictation_peek(True, False)
        #print("res: ", res)

        # clip = ImageGrab.grabclipboard()

        # if clip:
        #     print("*****")
        #     print(clip)
        #     print("*****")

        print("go_slash()")

        return 0
    


    


    def mangle(s: str) -> str:
        "Mangles the input string in the appropriate manner."
        return "__" + s
    
    def mover(s1: str, s2: str) -> str:
        "Moves the input string in the appropriate manner."

        print("s1: ", s1)
        print("s2: ", s2)
        
        # # Try each delimiter and use the first one that splits successfully
        # for delimiter in ["move"]:
        #     parts = s.split(delimiter, 1)  # Split on first occurrence only
        #     if len(parts) > 1:
        #         break

        # print("parts: ", parts)
        
        # if len(parts) == 1:
        #     # No "mover" found, treat entire string as s2
        #     s1 = ""
        #     s2 = parts[0].strip(" _-")
        # else:
        #     s1, s2 = parts
        #     # remove the spaces, dashes, underscores at the end of s1, and beginning of s2
        #     s1 = s1.rstrip(" _-") 
        #     s2 = s2.lstrip(" _-")

        print("s1: ", s1)
        print("s2: ", s2)
        
        return "mv " + s1 + " " + s2