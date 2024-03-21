import random
import pyinputplus as pyip
from pprint import pprint

def getNames(num:int) -> list[str]:
    with open('names.txt', encoding='utf-8') as file:
        rawData:str = file.read()
        names:list[str] = rawData.split('\n')
        random_names:list[str] = random.choices(names, k=num)

        return random_names

############################

def generateData(names:list[str]) -> list[dict[str:any]]:
    items:list[dict] = []

    for name in names:
        newItem:dict[str:any] = {
            'name': name,
            'height': random.randint(150, 220),
            'weight': random.randint(40, 90)
        }

        # newItem['name'] = name
        # newItem['height'] = random.randint(150, 220)
        # newItem['weight'] = random.randint(40, 90)

        items.append(newItem)

    return items

############################

def main():
    num:int = pyip.inputInt('請輸入指定人數(1~30):', min=1, max=50)
    names:list[str] = getNames(num)
    items:list[dict[str:any]] = generateData(names)

    pprint(items, sort_dicts=False)

main()