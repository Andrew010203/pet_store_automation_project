FROM python:3.12.1-alpine3.18

WORKDIR /usr/workspace

COPY ./ /usr/workspace

#RUN pip3 install requests
RUN pip install --no-cache-dir -r requirements.txt


#CMD ["pytest", "-s", "-v"]
CMD ["pytest"]