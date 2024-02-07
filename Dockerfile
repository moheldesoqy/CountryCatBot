FROM python:3

WORKDIR /app

COPY . /app

RUN pip3 install yt-dlp
RUN pip3 install discord
RUN pip3 install PyNaCl

RUN apt-get update && apt-get install -y ffmpeg

EXPOSE 80

CMD ["python3", "main.py"]
