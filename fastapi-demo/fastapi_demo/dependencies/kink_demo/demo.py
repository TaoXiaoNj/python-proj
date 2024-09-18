from dataclasses import dataclass
from kink import inject

@dataclass
class Photo:
    size: int

    def __init__(self, size: int):
        print(f"创建 Photo 实例: size = {size}")
        self.size = size


@inject
@dataclass
class User:
    photo: Photo

    def __init__(self, photo: Photo) -> None:
        print(f"创建 User 实例: photo = {photo}")
        self.photo = photo

    def get_photo_size(self):
        return self.photo.size
    
@inject
@dataclass
class Group:
    users: list[User]

    def __init__(self, user: User):
        print(f"创建 Group 实例: user = {user}")
        self.users = [user]

    def say(self):
        print(f"调用 Group.say() 方法： users = {self.users}")

