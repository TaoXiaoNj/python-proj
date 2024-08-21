import time
from datetime import datetime
from poetry_demo.com.cn.tao import ScoreDisplay
from poetry_demo.com.cn.data.Car import Car


def main():
    _show_info()
    _print_time()


def _show_info():
    ScoreDisplay.show(ScoreDisplay.std0)
    ScoreDisplay.show(ScoreDisplay.std1)

    car = Car("Honda", 22.33)
    print(car)


def _print_time():
    while True:
        now = datetime.now()
        print(now)
        time.sleep(2)


if __name__ == '__main__':
    main()