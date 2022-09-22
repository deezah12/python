import colorgram

rgb_colors = []
colors = colorgram.extract('img.png', 8)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)


color_list = [(254, 253, 252), (232, 254, 243), (253, 234, 245), (43, 2, 176), (79, 253, 174), (226, 149, 109),
              (230, 225, 253), (160, 3, 82)]

