import re

text = "NE 12544"

def search_in_text(text):

    if re.search(r'(AG|AI|AR|BE|BL|BS|FR|GE|GR|JU|LU|NE|NW,OW|SG|SH|SO|SZ|TG|TI|UR|VD|VS|ZG|ZH|M|A) ([1-9][0-9]{0,4}|[0-9]{1,3} [0-9]{3})', text):
        print ('match')
    else:
        print ('not match')

search_in_text(text)
