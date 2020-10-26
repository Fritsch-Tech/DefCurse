
def approximate_rgb(self, r, g, b):
    """WIP function to generate a aproximated terminal color from rgb values

    Args:
        r ([type]): [description]
        g ([type]): [description]
        b ([type]): [description]

    Returns:
        [type]: [description]
    """
    if self.number_of_colors != 256:
        return self.color(7)

    if r == g == b:
        offset = int(r / (256.0 / 24.0))
        index = 232 + offset
    else:
        roundint = lambda n, p: (n + p / 2) / p * p

    # Technically this ought to clamp to 0x5f, 0x87, 0xaf, and 0xd7
    # rather than 0x33, 0x66, 0x99, and 0xcc, but who the hell came
    # up with that? Seriously.
    clamped_r = roundint(r, 0x33)
    clamped_g = roundint(g, 0x33)
    clamped_b = roundint(b, 0x33)

    col = clamped_b / 0x33
    row = clamped_g / 0x33
    face = clamped_r / 0x33
    index = 36 * face + 6 * row + col + 16

    return self.color(index)