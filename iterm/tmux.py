from talon import actions, Context, Module

from .constants import load_ls_script, load_ls_call_script

mod = Module()

mod.tag("key_debug", "description")

ctx = Context()
ctx.matches = r"""
tag: user.key_debug
"""


SHORT_PAUSE = "20ms"
MEDIUM_PAUSE = "100ms"
LONG_PAUSE = "500ms"



@mod.action_class
class Actions:
    def tmux_hard():
        """ Use tmux to split window into 2 side-by-side panels. Auto resizing, and @TODO: auto-resizing the other pane """
        

        # Check if tmux is already running
        # actions.insert("echo $TMUX | grep -q . && echo 'Warning: tmux is already running' | tee ~/.talon/tmp/tmux.log\n")
        actions.user.paste("echo $TMUX | grep -q . && echo 'Warning: tmux is already running' | tee ~/.talon/tmp/tmux.log\n")
        actions.sleep("250ms")


        actions.insert("tmux\n")

        # wait for tmux to start
        actions.sleep(MEDIUM_PAUSE)

        actions.key("ctrl-b")
        actions.sleep(SHORT_PAUSE)
        #actions.key("%")

        actions.insert(":")

        actions.user.paste("split-window -v")
        actions.key("enter")
        
        actions.sleep(LONG_PAUSE)


        actions.key("ctrl-b")

        actions.sleep(LONG_PAUSE)
        actions.insert(":")
        actions.user.paste("resize-pane -D 12")
        actions.sleep(LONG_PAUSE)
        actions.key("enter")
        actions.sleep(LONG_PAUSE)

        # mkdir ~/.talon/tmp
        # luketych@Lukes-MacBook-Air mst % touch ~/.talon/tmp/tmux.log

        actions.key("ctrl-b up")


        # actions.insert("touch ~/.talon/tmp.log\n")
        actions.user.paste("touch ~/.talon/tmp.log")
        actions.key("enter")
        actions.sleep(MEDIUM_PAUSE)

        # tail -f /tmp/logp
        # actions.insert("tail -f ~/.talon/tmp.log\n")
        actions.user.paste("tail -f ~/.talon/tmp.log")
        actions.key("enter")
        actions.sleep(MEDIUM_PAUSE)


        # switch to the bottom pane
        actions.key("ctrl-b")
        actions.key("down")
        actions.sleep(LONG_PAUSE)


        return 0
    

    def tmux_vim():
        """ Open vim with a predefined function. """

        

        #  rm /tmp/.myscript.sh.swp
       # actions.insert("rm /tmp/.myscript.sh.swp\n")
        actions.sleep(SHORT_PAUSE)
        actions.key("enter")
        actions.sleep(SHORT_PAUSE)


        #actions.insert("nvim ~/.talon/vim_scripts/ls.sh && chmod +x ~/.talon/vim_scripts/ls.sh && ~/.talon/vim_scripts/ls.sh | tee ~/.talon/tmp.log")

        actions.user.paste(load_ls_script)  


        actions.sleep(SHORT_PAUSE)
        actions.key("enter")

        return 0
    

    def tmux_show():
        """ Show the current directory structure in a tmux pane """
        
        # fd -d 2 -t f --no-hidden -0 |                                              
        # egrep -zv 'test/|tests' |
        # xargs -0 eza --icons --long --grid --color=always |
	    # tee /tmp/log

        # actions.insert("fd -d 2 -t f --no-hidden -0 | xargs -0 eza --icons --long --grid --color=always | tee ~/.talon/tmp.log")
        actions.user.paste("fd -d 2 -t f --no-hidden -0 | xargs -0 eza --icons --long --grid --color=always | tee ~/.talon/tmp.log")
        actions.sleep(SHORT_PAUSE)
        actions.key("enter")

        return 0
