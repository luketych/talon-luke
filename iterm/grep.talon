app: /iterm/
-

tag(): user.generic_unix_shell
tag(): user.git
tag(): user.kubectl
tag(): user.readline


grep no dirs:
    key(ctrl-e)
    "|"
    key(space)

    "grep -v '/$' "


grep dirs:
    key(ctrl-e)
    "|"
    key(space)

    "grep '/$' "


grep ex:
    key(ctrl-e)
    "|"
    key(space)
    "egrep '\.(placeholder)$'"
    key(left left left)


grep un ex:
    key(ctrl-e)
    "|"
    key(space)
    "egrep -v '\.(placeholder)$'"
    key(left left left)