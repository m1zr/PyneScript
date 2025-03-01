# pynescript/color.py


def rgb(red, green, blue, transp=0):
    """
    Constructs a color tuple from red, green, blue values and transparency.
    In Pine Script, transparency is subtracted from 255.
    """
    return (red, green, blue, 255 - transp)


def new(hex_color, transp=0):
    """
    Constructs a color from a hex string and transparency.
    """
    hex_color = hex_color.lstrip("#")
    lv = len(hex_color)
    r, g, b = tuple(int(hex_color[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))
    return (r, g, b, 255 - transp)


def from_gradient(value, low, high, color0, color1):
    """
    Interpolates between two colors based on value.
    """
    t = (value - low) / ((high - low) + 1e-10)
    r = int(color0[0] + t * (color1[0] - color0[0]))
    g = int(color0[1] + t * (color1[1] - color0[1]))
    b = int(color0[2] + t * (color1[2] - color0[2]))
    a = int(color0[3] + t * (color1[3] - color0[3]))
    return (r, g, b, a)
