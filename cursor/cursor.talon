app: /Cursor/
-


cursor <user.format_text>:
    user.cursorFiles(format_text)

cursor <user.format_text> split <user.format_text>:
    user.cursorFiles(format_text_1, format_text_2)

cursor <user.format_text> split <user.format_text> split <user.format_text>:
    user.cursorFiles(format_text_1, format_text_2, format_text_3)
    
cursor <user.format_text> split <user.format_text> split <user.format_text> split <user.format_text>:
    user.cursorFiles(format_text_1, format_text_2, format_text_3, format_text_4)


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

spray <user.text>:
    user.spray(text)

    
