from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

class Man:
    def __init__(self, age: int, name: str) -> None:
        print(f"Initializing Man with '{name}'")
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


class ManContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    man = providers.Singleton(
        Man,
        name = config.the_name
    )


## 通过 Provide 表示这个参数是被注入的
@inject
def run(the_age: int, man: Man = Provide[ManContainer.man]):
    man(100)
    print(f"name = {man.get_name()}")


## 执行命令
## python -m fastapi_demo.dependencies.single_container.Runner
if __name__ == '__main__':
    man_container = ManContainer()
    man_container.config.the_name.from_value('tao')
    man_container.wire(modules=[__name__])

    # 这里并不需要给 `run` 传入参数
    run()

    print(man_container.man)