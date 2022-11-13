import tkinter
import numpy
import colorsys



def hex_from_rgb(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


def rgb_to_hls(color):
    r, g, b = [x / 255 for x in color]
    h, l, s = [x * 100 for x in colorsys.rgb_to_hls(r, g, b)]
    return int(round(h)), int(round(l)), int(round(s))


window = tkinter.Tk()
window.title("Лабораторна №3 Марчук Анастасія КН-308")

chartreuse_rgb = (0x7F, 0xFF, 0x00)
chartreuse_hls = rgb_to_hls(chartreuse_rgb)
chartreuse = tkinter.Label(
    text=f"chartreuse\nRGB({chartreuse_rgb[0]}, {chartreuse_rgb[1]}, {chartreuse_rgb[2]})\n"
         f"HLS({chartreuse_hls[0]}, {chartreuse_hls[1]}, {chartreuse_hls[2]})",
    foreground="white",
    background=hex_from_rgb(chartreuse_rgb),
    height=10,
    width=60
)
chartreuse.pack()

chartreuseBrighter_rgb = (0xCC, 0xFF, 0x99)
chartreuseBrighter = tkinter.Label(
    text=f"chartreuseBrighter\nRGB({chartreuseBrighter_rgb[0]}, {chartreuseBrighter_rgb[1]}, {chartreuseBrighter_rgb[2]})\n",
    foreground="white",
    background=hex_from_rgb(chartreuseBrighter_rgb),
    height=10,
    width=60
)
chartreuseBrighter.pack()

goldenrodBrighter_rgb = (0xEE, 0xAD, 0x0E)
goldenrodBrighter = tkinter.Label(
    text=f"goldenrodBrighter\nRGB({goldenrodBrighter_rgb[0]}, {goldenrodBrighter_rgb[1]}, {goldenrodBrighter_rgb[2]})\n",
    foreground="white",
    background=hex_from_rgb(goldenrodBrighter_rgb),
    height=10,
    width=60
)
goldenrodBrighter.pack()

#((138+255)/2, (46+43)/2, (226+255)/2)
mixed = (204, 180, 54)
mixed = tkinter.Label(
    text=f"mixed \nRGB({mixed[0]}, {mixed[1]}, {mixed[2]})",
    foreground="white",
    background=hex_from_rgb(mixed),
    height=10,
    width=60
)
mixed.pack()

window.mainloop()
