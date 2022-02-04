# 这是一个示例 Python 脚本。
# 猜数字游戏

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from random import randint


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


def play():
    random_int = randint(0, 100)

    while True:
        user_guess = int(input('what number did we guess (0-100)?'))

        if user_guess == random_int:
            print(f'You found the number ({random_int}). Congrats!')
            break

        if user_guess < random_int:
            print(f'Your number is less than the number we guessed.')
            continue

        if user_guess > random_int:
            print(f'Your number is more than the number we guessed.')
            continue


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    play()


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
