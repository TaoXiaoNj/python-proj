FROM python:3.11.6-slim

## suppose the docker build context is the project's root directory
## i.e., inside the `poetry_demo` folder
COPY . /app/poetry_demo

WORKDIR /app/poetry_demo

## install poetry
RUN python3 cicd/install-poetry.py --version 1.8.3

## build a wheel file "dist/poetry_demo-0.1.0-py3-none-any.whl"
## and install the wheel artifact
RUN export PATH="/root/.local/bin:$PATH" && \
    poetry build && \
    pip3 install dist/poetry_demo-0.1.0-py3-none-any.whl


## remove the source code from the image
WORKDIR /
RUN rm -rf /app

## start the application
ENTRYPOINT ["python3", "-m", "poetry_demo.com.cn.tao.HelloWorld"]