import sys

import ScoreDisplay
from poetry_demo.com.cn.data.Car import Car
from poetry_demo.com.cn.data.Student import Student


def main():
    print('开始运行 Hello World 程序')

    args = sys.argv

    print('共有 %s 个参数，分别是' % len(args))
    for x in args:
        print(x)

    ScoreDisplay.show(ScoreDisplay.std0)
    ScoreDisplay.show(ScoreDisplay.std1)

    student0 = Student('张三', 100)
    student0.print()

    student1 = Student('李四', 78)
    student1.age = 12
    student1.print()

    print(student1.age)

    car = Car('TOYOTA', 11.2)
    print(car)

    print(car.brand)

    car.brand = 'HONDA'
    print(car)



if __name__ == '__main__':
    main()