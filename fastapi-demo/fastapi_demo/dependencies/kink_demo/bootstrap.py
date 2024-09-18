from kink import di

from .demo import Photo

def bootstrap_di():
    print('注册初始依赖')
    di[Photo] = Photo(1024)
    print('初始依赖注册完毕')