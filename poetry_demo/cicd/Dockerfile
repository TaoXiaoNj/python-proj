FROM python:3.11.6-slim

WORKDIR /app

## install poetry
COPY cicd/install-poetry.py /app
RUN python3 install-poetry.py --version 1.8.3 && \
    export PATH="/root/.local/bin:$PATH"

## download code repo \
RUN apt-get install git --y
git clone https://github.com/TaoXiaoNj/python-proj.git
WORKDIR /app/python-proj/poetry_demo

## build a wheel file "dist/poetry_demo-0.1.0-py3-none-any.whl"
RUN poetry build
COPY dist/*.whl /app

## install the wheel
WORKDIR /app
RUN pip3 install poetry_demo-0.1.0-py3-none-any.whl

## start the application
ENTRYPOINT ["python3", "-m", "poetry_demo.com.cn.tao.HelloWorld"]