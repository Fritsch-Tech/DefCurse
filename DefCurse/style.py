def bold(string: str) -> str:
    return  "\x1b[1m"+str(string).replace(
                "\x1b[0m",
                "\x1b[0m\x1b[1m"
                )+"\x1b[0m"
    
    
def underline(string: str) -> str:
    return  "\x1b[4m"+str(string).replace(
                "\x1b[0m",
                "\x1b[0m\x1b[4m"
                )+"\x1b[0m"


def inverse(string: str) -> str:
    return  "\x1b[7m"+str(string).replace(
                "\x1b[0m",
                "\x1b[0m\x1b[7m"
                )+"\x1b[0m"