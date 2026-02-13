#FROM python:3.12.1-alpine3.18
#
#WORKDIR /usr/workspace
#
#COPY ./ /usr/workspace
#
##RUN pip3 install requests
#RUN pip install --no-cache-dir -r requirements.txt
#
##CMD ["pytest", "-s", "-v"]
#CMD ["pytest"]

FROM python:3.12.1-alpine3.18

WORKDIR /usr/workspace

# Устанавливаем зависимости
RUN apk add --no-cache openjdk11-jre curl tar bash

# Скачиваем и устанавливаем Allure (исправленная ссылка)
RUN curl -o allure-2.24.1.tgz -Ls https://github.com \
    && mkdir -p /opt \
    && tar -zxvf allure-2.24.1.tgz -C /opt/ \
    && ln -s /opt/allure-2.24.1/bin/allure /usr/bin/allure \
    && rm allure-2.24.1.tgz

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]