app: /iterm/
-

tag(): user.generic_unix_shell
tag(): user.git
tag(): user.kubectl
tag(): user.readline




can | cancel:
    key(ctrl-c)


# cd
see dee: "cd "


clear:
    key(ctrl-l)
    "lsd\n"

clear all:
    key(ctrl-l)



exit:
    "exit\n"


fish:
    "fish\n"


git:
    "git "


go dev:
    "cd ~/Dev\n"
    "lsd\n"


jujitsu:
    "jj "

jj:
    "jj "


# ls

else | else push:
    "ls\n"

else pull:
    "ls"

else all:
    "ls -A\n"


flat <user.text>:
    "_{text}"


history:
    "history\n"


open file <user.format_text>:
    "open {format_text}"



talon home:
    "cd ~/.talon\n"
    "ls\n"


touch:
    "touch "


touch <user.text>:
    "touch {text}"



# tree commands

tree:
    insert("""tree""")
    key("enter")

tree all:
    insert("""tree -a""")
    key("enter")

tree dirs:
    insert("""tree -d\n""")

tree <number>:
    insert("""tree -L {number or ''}\n""")



zee <user.text>:
    "z {text}"

zee <user.text> slap:
    "z {text}\n"
    "ls\n"
