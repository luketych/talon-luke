app: /iterm/
-

tag(): user.generic_unix_shell
tag(): user.git
tag(): user.kubectl
tag(): user.readline



acid:
    "lsd --classify "
    
acid --classify <number> push:
    insert("""lsd --recursive --depth {number or ''} """)
    key(enter)

acid --classify <number>:
    insert("""lsd --recursive --depth {number or ''} """)




ignore glob:
    # go to the end of the line
    key(ctrl-e)

    insert("""--ignore-glob "{}" """)
    key(left left left)

ignore star:
    # go to the end of the line
    key(ctrl-e)

    insert("""--ignore-glob "*{}" """)
    
    key(left left left)

ignore star dot:
    key(ctrl-e)
    insert("""--ignore-glob "*.{}" """)
    key(left left left)



ignore folder <user.format_text>:
    key(ctrl-e)

    ' --ignore-glob '
    '"{'
    '{format_text},'
    '{format_text}/**'
    '}"'

    key(ctrl-e)