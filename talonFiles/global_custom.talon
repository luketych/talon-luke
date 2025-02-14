find reverse:
     user.find_reverse()

mangle <user.text>:
    mangled_text = user.mangle(text)
    insert(mangled_text)


#mover <user.text>:
#    ret_val = user.mover(text)
#    insert(ret_val)

mover <user.format_text> move <user.format_text>:
    ret_val = user.mover(format_text_1, format_text_2)
    insert(ret_val)


go slashy:
    user.go_slash(1)