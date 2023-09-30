from flask import Flask
from flask import request, send_file
from waitress import serve

from mergeimg import generate_merged_image

import random
import asyncio

from generate_image import turn_by_90_deg

import logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)


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
    nnum = int(nnum,2)
    GOOD_NUMBERS.append(nnum)


async def generate_random_nums():
    chossen = []
    temp_list = GOOD_NUMBERS[:]  # learned from chatgpt
    for _  in range(9):
        random_ele = random.choice(temp_list)
        temp_list.remove(random_ele)
        chossen.append(random_ele) 
        
    for i in range(len(chossen)):
        r = random.randint(0, 3)
        for _ in range(r):
            chossen[i] = turn_by_90_deg(chossen[i])
    
    return {"data":chossen}


def arrify_lbp(lbp):
    
    for i in range(2,10):
        lbp = lbp.replace(str(i),"0"*i)
    
    lbp = lbp.split("/")
    
    if len(lbp) % 2 != 0 or len(lbp[0]) % 2 != 0:
        return False,"Error: Incorrect side of less board position. Try with both sides to be divisible by 2."
    
      # w white, b black, 0 empty
    
    
    print(lbp)
    
    arry = []
    for x in range(0,int(len(lbp)),2):
        a2 = []
    
        upper_row = lbp[x]
        lower_row = lbp[x+1]
        
        print("-")
        print(upper_row,lower_row)
        print("-")
    
        len_row = len(upper_row)
        
        for y in range(0,len_row,2):
            
            print(upper_row, upper_row[y],upper_row[y+1])
            
        
            block=[[upper_row[y],upper_row[y+1]],[lower_row[y],lower_row[y+1]]]
                
            lbp[x] = lbp[x][:-2]
            lbp[x+1] = lbp[x+1][:-2]
            
            
            a2.append(block)
            
        arry.append(a2)
        
    print(arry)
    
    return True,arry
    
        
        

@app.route("/")
def main():
    return "Hello, to my awesome less server :)"


@app.route("/new")
async def new_game():
    data = await generate_random_nums()
    return data

@app.route("/image")
def get_image():
    
    
    nums = request.args.get("nums")
    lbp = request.args.get("lbp")
    
    print(nums,lbp)
    
    nums = nums.split(",")
    nums = list(map(int, nums))

    succes,lbp_arry = arrify_lbp(lbp)
    if not succes:
        return lbp_arry
    

    filename = generate_merged_image(nums,lbp_arry)
    return send_file(filename, mimetype="png")


serve(app, host="0.0.0.0", port=5000)
