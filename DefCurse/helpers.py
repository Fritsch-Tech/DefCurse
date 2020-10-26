import re
from typing import List


from DefCurse import constants


# strip ansi escape sequences from string
def strip_esc(string: str) -> str:
    return re.sub(constants.ANSII_ESCAPE_REGEX,'',string)


def add_line_numbers(list: List[str]) -> List[str]:
    line_number_length = len(str(len(list))) + 2
    return [(str(idx)+": ").rjust(line_number_length)+e for idx, e in enumerate(list)]


# WIP
# shorten the string while ignoring all ansi escape sequences
def shorten_str_pure(string: str,len: int) -> str:
    return string[:len]
    return_str = ""
    counter = 0
    for element in re.split("(" + constants.ANSII_ESCAPE_REGEX + ")",string):
        if element.startswith(r'\x1b'):
            return_str += element
            counter +=1
        else:
            for char in element:
                return_str += char
                counter += 1
                if counter >= len:
                    break

    return return_str+"\x1b[0m"

