import drawsvg as draw

BACKGROUND_COLOR = "#FFFFFF"
ONE_COST_STEP_COLOR = "#ADD8E6"
DOUBLE_COST_STEP_COLOR = "#1a4cd6"
BINARY_LEN = 12
HALF = 50
THICK = 10  # double cost step thick
FULL = 100
INT_MAX = 2**BINARY_LEN

PATH_PNG = "tmp/{}.png"


def turn_by_90_deg(num):

    binary = binary_by_12(num)
    bin_arry = list(binary)

    # 000000000001
    # 000010000000
    #  +-+-+
    #  | | |
    #  +-+-+
    #  | | |
    #  +-+-+
    ##
    #  +0+1+
    #  2 3 4
    #  +5+6+
    #  7 8 9
    #  +10+11+

    new_arry = ["0"] * 12

    # left outside
    new_arry[0], new_arry[4], new_arry[11], new_arry[7] = (
        bin_arry[7],
        bin_arry[0],
        bin_arry[4],
        bin_arry[11],
    )
    # right outside
    new_arry[1], new_arry[9], new_arry[10], new_arry[2] = (
        bin_arry[2],
        bin_arry[1],
        bin_arry[9],
        bin_arry[10],
    )
    # inside
    new_arry[3], new_arry[6], new_arry[8], new_arry[5] = (
        bin_arry[5],
        bin_arry[3],
        bin_arry[6],
        bin_arry[8],
    )

    new_n = "".join(new_arry)

    new_n = "0b" + new_n
    new_n = int(new_n, 2)

    return new_n


def binary_by_12(dec):
    b = bin(dec)
    b = str(b)[2::]
    added_0 = (12 - len(b)) * "0"
    b = added_0 + b
    return b


def draw_empty_tile():
    tile = draw.Drawing(100, 100, origin=(0, 0))

    r = draw.Rectangle(
        0,
        0,
        100,
        100,
        fill=BACKGROUND_COLOR,
        stroke=ONE_COST_STEP_COLOR,
        stroke_width=10,
    )
    tile.append(r)

    cross_1 = draw.Rectangle(47.5, 0, 5, 100, fill=ONE_COST_STEP_COLOR)
    cross_2 = draw.Rectangle(0, 47.5, 100, 5, fill=ONE_COST_STEP_COLOR)

    tile.append(cross_1)
    tile.append(cross_2)

    return tile


def offset(wide, total=100):
    return (total - wide) / 2


def update_by_1_move(image, dec):
    if dec > INT_MAX:
        print("big num")
        return image

    binary = binary_by_12(dec)
    print(binary)
    if not len(binary) == 12:
        print("not correnct binary")
        return image

    ROM = [
        (0, 0, HALF, THICK),
        (HALF, 0, HALF, THICK),
        (0, 0, THICK, HALF),
        (offset(THICK), 0, THICK, HALF),
        (FULL - THICK, 0, THICK, HALF),
        (0, offset(THICK), HALF, THICK),
        (HALF, offset(THICK), HALF, 10),
        (0, HALF, 10, 100),
        (offset(THICK), HALF, THICK, HALF * 2),
        (FULL - THICK, HALF, THICK, HALF * 2),
        (0, HALF * 2 - THICK, HALF, THICK),
        (HALF, HALF * 2 - THICK, HALF * 2, THICK),
    ]
    for i in range(len(ROM)):
        if binary[i] == "1":
            x, y, w, h = ROM[i]

            n = draw.Rectangle(x, y, w, h, fill=DOUBLE_COST_STEP_COLOR)
            image.append(n)

    return image


def make_tile_and_save_it(b):
    tile = draw_empty_tile()
    tile = update_by_1_move(tile, b)

    tile.set_pixel_scale(5)
    print(PATH_PNG.format(b))

    tile.save_png(PATH_PNG.format(b))

    return PATH_PNG.format(b)
