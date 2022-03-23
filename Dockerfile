#---------------------------------------------------------------------------
# Dockefile to build Docker Image of Apache WebServer running on Ubuntu
#
# Made by Denis Astahov ADV-IT  13-March-2019
#---------------------------------------------------------------------------

FROM python:3.10.2

COPY . .
# Переключаем Ubuntu в неинтерактивный режим — чтобы избежать лишних запросов
ENV DEBIAN_FRONTEND noninteractive 
# Устанавливаем локаль
# RUN locale-gen ru_RU.UTF-8 && dpkg-reconfigure locales 

# Добавляем необходимые репозитарии и устанавливаем пакеты
RUN apt-get update
RUN apt-get upgrade -y
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

# run
ENTRYPOINT ["python3"]
CMD ["app.py"]