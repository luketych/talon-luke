app: /iterm/
-

tag(): user.generic_unix_shell
tag(): user.git
tag(): user.kubectl
tag(): user.readline


reveal under <user.text>:
    "fd -pg "
    " '**/{text}/**/'"
    " | xargs cursor"

    key(alt-left alt-left)
    key(left left left left)

reveal under <user.format_text>:
    "fd -pg "
    " '**/{format_text}/**/'"
    " | xargs cursor"

    key(alt-left alt-left)
    key(left left left left)


reveal under <user.text> pattern <user.text>:
    "fd -pg "
    " '**/{text_1}/**/{text_2}'"
    " | xargs cursor"

    key(alt-left alt-left)
    key(left left left left)

reveal under <user.text> pattern <user.format_text>:
    "fd -pg "
    " '**/{text}/**/{format_text}'"
    " | xargs cursor"

    key(alt-left alt-left)
    key(left left left left)