from dependency_injector import containers, providers
from dataclasses import dataclass

@dataclass
class Photo:
    size: int

    def __init__(self, size: int):
        self.size = size


@dataclass
class User:
    age: int
    photo: Photo

    def __init__(self, age: int, photo: Photo) -> None:
        self.age = age
        self.photo = photo


class Container(containers.DeclarativeContainer):
    photo_factory = providers.Factory(Photo)
    user_factory = providers.Factory(
        User,
        photo=photo_factory
    )

if __name__ == '__main__':
    container = Container()

    # user1: User = container.user_factory(102)
    # print(user1)

    photo = container.photo_factory(1024)
    user2 = container.user_factory(
        age=200,
        photo=photo
    )
    print(user2)