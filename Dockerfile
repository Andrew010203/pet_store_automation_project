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

RUN apk add --no-cache openjdk11-jre curl tar bash

# ВАЖНО: Ссылка должна быть полной, до самого конца (.tgz)
ARG ALLURE_URL=https://github.com

RUN curl -Ls ${ALLURE_URL} -o allure.tgz \
    && mkdir -p /opt \
    && tar -zxvf allure.tgz -C /opt/ \
    && ln -s /opt/allure-2.24.1/bin/allure /usr/bin/allure \
    && rm allure.tgz

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["pytest"]