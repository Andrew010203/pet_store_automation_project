#FROM python:3.12.1-alpine3.18
FROM python:3.12-slim-bookworm

WORKDIR /usr/workspace

COPY ./ /usr/workspace

RUN apk add --no-cache gcc musl-dev libffi-dev
RUN pip install --no-cache-dir -r requirements.txt
COPY . .


CMD ["pytest", "-s", "-v"]