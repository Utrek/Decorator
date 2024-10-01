import datetime
from template import logger

@logger('log1.log')
def do_cook_book (file):
    file = open(file,'r',encoding='utf-8')
    ingredient_dict = {}
    ingredients = []
    key_list = ['ingredient_name', 'quantity', 'measure']
    dishes_ingredients = []
    quantity_ingredients = []
    cook_book = {}
    cook_ingredients=[]
    cook_book_dishes=[]
    while True:
        line = file.readline()
        if "|" not in line and len(line) > 2:
            key = line.strip()
            cook_book_dishes.append(key)
        elif "|" in line:
            ingredients.append( line.strip().split('|'))   
        elif "|" not in line and len(line.strip()) == 1: 
            quantity_ingredients.append(int(line.strip()) ) 
        elif not line:
            break
    for ingredient in ingredients:
        ingredient_dict = dict(zip(key_list, ingredient))
        dishes_ingredients.append(ingredient_dict)   
    count1 = 0
    count2 = quantity_ingredients[0]
    cook_ingredients.append(dishes_ingredients[0:quantity_ingredients[0]])
    for n in range(1,len(quantity_ingredients)): 
        count1 = count2 
        count2 += quantity_ingredients[n]
        cook_ingredients.append(dishes_ingredients[count1:count2])
    for i in range(0,4):
        for j in range(0,4):
            if i == j:
                cook_book[cook_book_dishes[i]] = cook_ingredients[j]
    return cook_book

do_cook_book ('recipes.txt')







