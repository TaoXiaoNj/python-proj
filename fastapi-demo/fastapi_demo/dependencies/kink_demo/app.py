from kink import di
from .demo import Group

if __name__ == '__main__':
    group = di[Group]
    group.say()