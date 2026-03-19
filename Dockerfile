# From https://docs.microsoft.com/en-us/azure/devops/pipelines/process/container-phases?view=azure-devops#linux-based-containers
# Images based on Alpine Linux, don't satisfy minimum requirements for Azure Devops as container jobs.
FROM python:3.13

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

WORKDIR /app 

RUN uv sync --frozen --no-cache

ENV PORT=8000
EXPOSE ${PORT}

LABEL maintainer="Angel Sevilla Camins"

# Linux based container should not define an ENTRYPOINT
CMD ["uv", "run", "fastapi", "run"]