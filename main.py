from flask import Flask
from flask import request, send_file


from mergeimg import generate_merged_image

app = Flask(__name__)

"""NUMBERS = [
    "000101000000",
    "000101000000",
]

GOOD_NUMBERS = []

for num in range(len(GOOD_NUMBERS)):
    nnum = "0b" + str(num)
    nnum = int(nnum, 2)
    NUMBERS.append(nnum)
"""


@app.route("/")
def main():
    return "Hello, to my awesome less server :)"


@app.route("/new")
def new_game():
    chossen = []
    return chossen


@app.route("/image")
def get_image():
    t = request.args.get("nums")
    print(t)

    t = t.split(",")
    t = list(map(int, t))

    filename = generate_merged_image(t)

    return send_file(filename, mimetype="png")


app.run()
