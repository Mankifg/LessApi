from flask import Flask
from flask import request, send_file

from mergeimg import generate_merged_image

import random
import asyncio

app = Flask(__name__)

NUMBERS = [
    "000000000001", # short under
    "000000000011", # long under
    "000001001000", # L right down 
    "000001001000", # L right down
    "000000001001", # L right middle
    "000000001001", # L right middle
    "000000001001", # L right middle
    "000000001010", # L left middle
    "000000001010", # L left middle
    "000000001011", # short T 
    "000100100100", # snake 
    "000100100100", # snake
    
]

GOOD_NUMBERS = []

for num in NUMBERS:
    nnum = f"0b{num}"
    print(nnum)
    nnum = int(nnum,2)
    GOOD_NUMBERS.append(nnum)


async def generate_random_nums():
    chossen = []
    temp_list = GOOD_NUMBERS[:]  # learned from chatgpt
    for _  in range(9):
        random_ele = random.choice(temp_list)
        temp_list.remove(random_ele)
        chossen.append(random_ele) 
    return {"data":chossen}


@app.route("/")
def main():
    return "Hello, to my awesome less server :)"


@app.route("/new")
async def new_game():
    data = await generate_random_nums()
    return data

@app.route("/image")
def get_image():
    t = request.args.get("nums")
    print(t)

    t = t.split(",")
    t = list(map(int, t))

    filename = generate_merged_image(t)

    return send_file(filename, mimetype="png")


app.run()
