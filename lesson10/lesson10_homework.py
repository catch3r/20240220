import random
import pyinputplus as pyip
import linecache
from pprint import pprint

def getNames(num:int) -> list[str]:
    #1
    #names:list[str] = []
    # for line in open('names.txt', encoding='utf-8'):
    #     line:str = line.rstrip('\n')
    #     names.append(line)

    # random_names:list[str] = random.choices(names, k=num)

    # return random_names
    
    #2
    with open('names.txt', encoding='utf-8') as file:
        #顧慮記憶體的狀況下採取的寫法
        # while True:
        #     line = file.readline()
        #     if not line:
        #         break
        #     pass

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

        items.append(newItem)

    return items

############################

def main():
    num:int = pyip.inputInt('請輸入指定人數(1~50):', min=1, max=50)
    names:list[str] = getNames(num)
    items:list[dict[str:any]] = generateData(names)

    pprint(items, sort_dicts=False)

main()