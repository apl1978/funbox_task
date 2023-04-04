FROM python:3.10-alpine

WORKDIR /fb_task_api
COPY ./requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

EXPOSE 8000