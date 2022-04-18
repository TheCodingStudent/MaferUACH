from colorsys import rgb_to_hls, hls_to_rgb

rgb_to_hex = lambda r, g, b: '#%02x%02x%02x' % (int(r), int(g), int(b))
hex_to_rgb = lambda color: tuple(int(color[i:i+2], 16) for i in (1, 3, 5))

def hex_to_hls(color):
    r, g, b = hex_to_rgb(color)
    return rgb_to_hls(r, g, b)

def hls_to_hex(h, l, s):
    r, g, b = hls_to_rgb(h, l, s)
    return int(255*r), int(255*g), int(255*b)

def atenuate(color, light, saturation):
    h, _, _ = rgb_to_hls(*hex_to_rgb(color))
    r, g, b = hls_to_rgb(h, light/240, saturation/240)
    return rgb_to_hex(255*r, 255*g, 255*b)

print(atenuate('#3cfac8', 30, 35))