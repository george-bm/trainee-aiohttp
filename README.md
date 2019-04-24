# Проект Pitter Auth (aiohttp)


##### Переменные окружения
 - `DEBUG` - Дебаг-режим (0 или 1)
 - `SPEECH_KEY` - ключ от API Google SpeechToText
 
 ### Настройка сервисного аккаунта
Для распознания текста сервис использует Google Cloud Speech-To-Text API
- Создать проект на https://console.cloud.google.com
- Включить Google Speech-to-Text API для этого проекта на https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries
- Создать сервисный аккаунт на https://console.cloud.google.com/iam-admin/serviceaccounts
- Сохранить ключ API
 
##### Запуск проекта в виртальном окружении

 - Создать окружение c Python 3.7, активировать его
 - Установить python-зависимости из `config/requirements.txt` (`pip install -r config/requirements.txt`)
 - Добавить переменные окружения
 - Выполнить `python src/main.py`