import re
def to_camel_case(text):
    result = re.split('-|_', text)
    for i in range(1, len(result)):
         result[i] = result[i].title()
    new_string = ''
    for word in result:
        new_string += word
    return new_string