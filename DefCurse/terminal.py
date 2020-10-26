import sys
import termios
import tty
import os


from DefCurse import constants


def get_max_row_col() -> (int,int):
    return reversed(os.get_terminal_size())


def get_colors() -> int:
    return 


def _init_terminal() -> list:
    sys.stdout.write(constants.SMCUP+constants.CLEAR+constants.HIDE_CURSOR+"\n")

    fd = sys.stdin.fileno()
    prev_terminal_state = termios.tcgetattr(fd)
    new_terminal_state = termios.tcgetattr(fd)
    # lflags
    new_terminal_state[3] = new_terminal_state[3] & ~termios.ECHO & ~termios.ICANON
    tty.setcbreak(fd, when=termios.TCSAFLUSH)
    termios.tcsetattr(fd, termios.TCSADRAIN, new_terminal_state)
    return prev_terminal_state


def _restore_terminal(prev_terminal_state:list) -> None:
    sys.stdout.write(constants.RMCUP)
    sys.stdout.write(constants.SHOW_CURSOR)
    fd = sys.stdin.fileno()
    termios.tcsetattr(fd, termios.TCSADRAIN, prev_terminal_state)


def _move_cursor(row: int, col: int) -> None:
    sys.stdout.write("\x1b[{row};{col}H".format(row=row+1, col=col))

def _clear_terminal() -> None:
    sys.stdout.write(constants.CLEAR + "\n")


def _add_str(row: int, col: int, string: str) -> None:
    _move_cursor(row, col+1)
    sys.stdout.write(str(string) + "\x1b[0m")


def _get_key() -> str:
    key = sys.stdin.read(1)
    # check for modifiers
    if key == "\x1b":
        key += sys.stdin.read(1)
        # check for arrow keys
        if key[1] == "[":
            key += sys.stdin.read(1)
    return key


def _draw() -> None:
    sys.stdout.write("\n")

