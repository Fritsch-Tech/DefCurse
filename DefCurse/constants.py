SMCUP = "\x1b[?1049h"  # switches to alternative buffering
CLEAR = "\x1b[2J"     # hard clear
RMCUP = "\x1b[?1049l"  # restore terminal
HIDE_CURSOR = "\x1b[?25l"
SHOW_CURSOR = "\x1b[?25h"

# 7-bit C1 ANSI sequences
ANSII_ESCAPE_REGEX = r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])'
