app: /iterm/
-

tag(): user.generic_unix_shell
tag(): user.git
tag(): user.kubectl
tag(): user.readline



tee mux split basic:
    "tmux\n"
    key(ctrl-b)
    " %"

tee mux go right <number>:
    key(ctrl-b)
    ": resize-pane -R {number} \n"

tee mux go left <number>:
    key(ctrl-b)
    ": resize-pane -L {number} \n"
    

tee mux hard:
    user.tmux_hard()

tee mux vim:
    user.tmux_vim()

tee mux show:
    user.tmux_show()