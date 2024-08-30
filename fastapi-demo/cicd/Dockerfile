FROM fastapi-demo-base:latest

## suppose the docker build context is the project's root directory
## i.e., inside the `fastapi-demo` folder
COPY . /app/fastapi-demo

WORKDIR /app/fastapi-demo

## install POETRY
RUN python3 cicd/install-poetry.py  --version 1.8.3

ENV PATH="/root/.local/bin:$PATH"

## install to resolve and install the dependencies
RUN poetry install --no-root


# you can verify using command the following
# curl 'http://localhost:8000/items/AAA/128'
ENTRYPOINT ["/bin/bash", "-c", "poetry run fastapi run fastapi_demo/hello.py"]