app: /Cursor/
-


hello chat:
    key("cmd-l")

hello composer:
    key("cmd-i")


open file:
    key("cmd-p")
    
open file <user.text>:
    user.openFile(text)

open file <user.format_text>:
    user.openFile(format_text)


open two files <user.format_text>:
    user.openFiles(format_text)


open last file:
    key("ctrl-tab")