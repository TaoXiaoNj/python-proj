FROM python:3.11.6-slim

WORKDIR /app
## suppose the docker build context is the project root directory
COPY . /app

## install poetry
RUN python3 cicd/install-poetry.py --version 1.8.3 && \
    export PATH="/root/.local/bin:$PATH"

WORKDIR /app/poetry_demo


## build a wheel file "dist/poetry_demo-0.1.0-py3-none-any.whl"
RUN poetry build

## install the wheel
RUN pip3 install poetry_demo-0.1.0-py3-none-any.whl

## remove the source code from the image
WORKDIR /
RUN rm -rf /app

## start the application
ENTRYPOINT ["python3", "-m", "poetry_demo.com.cn.tao.HelloWorld"]