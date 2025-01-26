# from talon import ctrl, Module, actions

# mod = Module()

# mod.tag("key_debug", "Keep track of which keys are held and not")

# ctx = Context()
# ctx.matches = r"""
# tag: user.key_debug
# """


from talon import Module, actions

mod = Module()


@mod.action_class
class Actions:
    def find_reverse(): 
        "Begins a reverse search."

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