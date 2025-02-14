app: /iterm/
win.title: /nvim|tmux/
-

## escape
escape: key("ctrl-[")

scape: key("ctrl-[")


# quit save
quit save: user.quit_save()




## ARGUMENTS

append [args] <user.text>:
    key("ctrl-[")
    insert("/{text}")

    key("ctrl-m")


    # move to the quotes

    "f\""
    "f\""

    key("i")

    "|"

prepend [args] <user.text>:
    key("ctrl-[")
    insert("/{text}")

    key("ctrl-m")


    # move to the quotes

    "f\""

    key("a")

    "|"

    key("ctrl-[")

    "i"


change [args] <user.text>:
    key("ctrl-[")
    insert("/{text}")

    key("ctrl-m")


    # move to the quotes

    "f\""
    "t\""
    "ci\""



head [args] <user.text>:
    key("ctrl-[")
    insert("/{text}")

    key("ctrl-m")


    # move to the quotes

    "f\""

    key("a")


tail [args] <user.text>:
    key("ctrl-[")
    insert("/{text}")

    key("ctrl-m")


    # move to the quotes

    "f\""
    "f\""

    key("i")




## QUOTES

charge in quotes:
    key("ctrl-[")

    "f\""
    "t\""
    "ci\""

select in quotes:
    key("ctrl-[")

    "f\""
    "t\""
    "vi\""


# return
return:
    key("ctrl-m")


## SEARCH

quest <user.text>:
    "?{text}"

# slash
slash <user.text>:
    "/{text}"

search <user.text>:
    key("ctrl-[")
    insert("/{text}")
    key("ctrl-m")

search <user.format_text>:
    key("ctrl-[")
    insert("/{format_text}")
    key("ctrl-m")

back search <user.text>:
    key("ctrl-[")
    "?{text}"
    key("ctrl-m")

back search <user.format_text>:
    key("ctrl-[")
    "?{format_text}"
    key("ctrl-m")



## LINE NUMBERS

go <number>:
    key("ctrl-[")
    ":{number}"
    key("ctrl-m")

# set number (show line numbers)
set number:
    key("ctrl-[")
    ":"
    "set number"
    key("ctrl-m")

# set nonumber (hide line numbers)
set nonumber:
    key("ctrl-[")
    ":"
    "set nonumber"
    key("ctrl-m")




## UNDO / REDO

undo:
    key("ctrl-[")
    key("u")

redo:
    key("ctrl-[")
    key("ctrl-r")
