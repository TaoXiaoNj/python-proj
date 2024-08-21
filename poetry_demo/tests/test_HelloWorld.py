import pytest

def test_should_main_work():
    assert 1 == 1

def func():
    print('正在执行函数 func')
    raise SystemExit(1)

def test_func():
    with pytest.raises(SystemExit):
        func();