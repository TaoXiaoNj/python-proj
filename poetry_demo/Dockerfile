FROM python:3.11.6-slim

WORKDIR /app

COPY dist/*.whl /app

RUN pip3 install poetry_demo-0.1.0-py3-none-any.whl

ENTRYPOINT ["python3", "-m", "poetry_demo.com.cn.tao.HelloWorld"]