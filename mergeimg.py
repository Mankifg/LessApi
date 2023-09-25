from PIL import Image
from geneate_image import make_tile_and_save_it
import os
from pathlib import Path

IMAGE_WIDTH = 3
IMAGE_HEIGHT = 3
SAVE_PATH = "tmp/merged.png"

# FILE_PATH = "images/{}"

# file_to_open = ["1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png"]


def generate_merged_image(arry_of_dec):
    files_to_open = []

    for dec in arry_of_dec:
        path = make_tile_and_save_it(dec)
        files_to_open.append(path)

    image_arry = []

    for fp in files_to_open:
        image = Image.open(fp)
        image_arry.append(image)

    image_size = image_arry[0].size
    new_image = Image.new(
        "RGB",
        (IMAGE_WIDTH * image_size[0], IMAGE_HEIGHT * image_size[1]),
        (250, 250, 250),
    )

    for x in range(IMAGE_WIDTH):
        for y in range(IMAGE_HEIGHT):
            s = 3 * y + x
            coords = (x * image_size[0], y * image_size[1])

            new_image.paste(image_arry[s], coords)

    new_image.save(SAVE_PATH, "PNG")

    for path in Path("tmp/").rglob("*.png"):

        p = str(path)
        if "merged" not in p:
            os.remove(p)

    return SAVE_PATH
