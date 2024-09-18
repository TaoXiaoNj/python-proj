from fastapi import FastAPI, Depends
from typing import Annotated
from pydantic import BaseModel
import time

app = FastAPI()


class UserOut(BaseModel):
    user: str


class UserIn(UserOut):
    passwd: str

def func(user: UserIn):
    return 'hello'


def mul(x: int):
    return x * 200


class MyParam:
    def __init__(self, q: str, p: int) -> None:
        self.queen = 'queen' + q
        self.plus = p * 100


def get_book():
    print("进入 get_book")
    yield 'Book 1'
    print("离开 get_book")


@app.post("/user/")
def hello(book: Annotated[str, Depends(get_book)]) :
    print(f"第一次：{book}")

    time.sleep(2)
    pass