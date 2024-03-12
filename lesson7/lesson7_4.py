import random
import pyinputplus as pyip

def play_game():
    min = 1
    max = 100
    count = 0
    target = random.randint(min, max)
    print("===猜數字遊戲===\n")
    print(target)

    while True:
        keyin = pyip.inputInt(f'猜數字範圍: {min}~{max}\n', min=min, max=max)
        count += 1
        if keyin == target:
            print(f'賓果! 猜對了, 答案是{target}')
            break
        elif keyin > target:
            print('再小一點')
            max = keyin - 1
        else:
            print('再大一點')
            min = keyin + 1

        print(f'您猜了{count}次')

def main():
    while True:
        play_game()
        result:str = input('是否要繼續?(y/n)')
        if not result == 'y':
            break

    print(f'遊戲結束!')

#print(__name__)
if __name__ == '__main__':
    main()