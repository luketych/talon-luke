from talon import actions, Context, Module

from .constants import load_ls_script, load_ls_call_script

mod = Module()

mod.tag("key_debug", "description")

ctx = Context()
ctx.matches = r"""
tag: user.key_debug
"""




@mod.action_class
class Actions:
    def tmux_hard():
        """ Use tmux to split window into 2 side-by-side panels. Auto resizing, and @TODO: auto-resizing the other pane """
        

        # Check if tmux is already running
        actions.insert("echo $TMUX | grep -q . && echo 'Warning: tmux is already running' | tee ~/.talon/tmp/tmux.log\n")
        actions.sleep("1000ms")


        actions.insert("tmux\n")

        # wait for tmux to start
        actions.sleep("100ms")

        actions.key("ctrl-b")
        actions.sleep("50ms")
        actions.key("%")
        actions.sleep("50ms")
        actions.key("enter")
        actions.sleep("50ms")


        actions.key("ctrl-b")
        actions.insert(": resize-pane -R 25 ")
        actions.sleep("50ms")
        actions.key("enter")
        actions.sleep("50ms")

        # mkdir ~/.talon/tmp
        # luketych@Lukes-MacBook-Air mst % touch ~/.talon/tmp/tmux.log


        actions.insert("touch ~/.talon/tmp.log\n")
        actions.sleep("50ms")

        # tail -f /tmp/log
        actions.insert("tail -f ~/.talon/tmp.log\n")
        actions.sleep("50ms")


        # switch to the left pane
        actions.key("ctrl-b")
        actions.key("left")
        actions.sleep("50ms")


        return 0
    

    def tmux_vim():
        """ Open vim with a predefined function. """

        

        #  rm /tmp/.myscript.sh.swp
       # actions.insert("rm /tmp/.myscript.sh.swp\n")
        actions.sleep("50ms")
        actions.key("enter")
        actions.sleep("50ms")


        #actions.insert("nvim ~/.talon/vim_scripts/ls.sh && chmod +x ~/.talon/vim_scripts/ls.sh && ~/.talon/vim_scripts/ls.sh | tee ~/.talon/tmp.log")

        actions.insert(load_ls_script)  


        actions.sleep("50ms")
        actions.key("enter")

        return 0
    

    def tmux_show():
        """ Show the current directory structure in a tmux pane """
        
        # fd -d 2 -t f --no-hidden -0 |                                              
        # egrep -zv 'test/|tests' |
        # xargs -0 eza --icons --long --grid --color=always |
	    # tee /tmp/log

        actions.insert("fd -d 2 -t f --no-hidden -0 | xargs -0 eza --icons --long --grid --color=always | tee ~/.talon/tmp.log")
        actions.sleep("50ms")
        actions.key("enter")

        return 0
