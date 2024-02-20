FROM python:3.11

# Установка платформы необходима для работы на macbook m1 с архитектурой arm64
RUN dpkg --add-architecture amd64

# Install Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Install allure
RUN apt-get update && apt-get install -y allure


#Создаем папку для дальнейшего копирования в него нашего проекта
RUN mkdir /yadro_test

# Переходим в созданную рабочую директорию
WORKDIR /yadro_test

RUN mkdir /allure-results

COPY requirements.txt .

#устанавливаем библиотеки и сохраняем в кэше т.к эти данные редко меняются
RUN pip install -r requirements.txt

#Копируем все папки все файлы внутрь образа
COPY . .

#Переходим в папку проекта со всеми данными для запуска теста
WORKDIR /yadro_test

#CMD ["pytest", "--tb=line"]
CMD ["pytest", "--alluredir=allure-results"]



# Для ручного запуска:
#1) в терминале нужно собрать образ командой ниже:
# docker build . -t yadro_test:latest
#Для макбук м1
# docker build --platform linux/amd64 --no-cache -t yadro_test .

#2) Запускаем контейнер с автоматическим удалением контейнера после завершения работы:
# docker run --rm -v yadro_test
# или docker run --rm -v yadro_test:/YadroTest yadro_test