# Generated_images
Написать телеграм-бот, определяющий сгенерированы ли картинки нейросетью или созданы человеком.
## Задачи
1. Задачи бинарной классификации - определить класс картинки: сгенерирована ли нейросетью или создана человеком.
2. Написать телеграм-бот, получающий на вход картинку и выдающий прогноз.
3. Собрать проект и запустить на сервере.

### Источники данных
[Датасет](https://www.kaggle.com/competitions/generated-or-not/submissions) из 1012 фотографий двуъ классов: FAKE (сгенерировано нейросетью) и REAL (создано человеком). 
Данный датасет разбалансирован: 667 фотографий REAL и 345 фотографий FAKE. Поэтому в него были добавлены 100 фотографий REAL и 300 фотографий FAKE из датасета [CIFAKE](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images?select=test)

### Метрики
logloss

###  Используемые методы
1. Для решения **Задачи бинарной классификации** была использована библиотека keras. Наиболее подходящая оказалась модель EfficientNet со следующей архитектурой
![image](https://github.com/user-attachments/assets/3922fec2-1df0-4229-9b04-5767ab10cf4f)

На вход модели подаются картинки размером 224*224 батчами размером 16. На валиационном датасете удалось достичь logloss 0.0761.
2. Для написания телеграм-бота использована библиотека aiorgram.
   Структура папок имеет следующий вид:
   ![image](https://github.com/user-attachments/assets/0f0f90b7-1bd7-4d30-b881-ae923d761bf8)
   
   Телеграм-бот написан в файле bot.py. В данный файл включены 3 роутера из папки handlers:
   - start_help.py - ответ бота на команды /start, /help
   - photo.py - обработка отправленного фото
   - different_types.py - ответа бота при отпраке ему других типов файлов, отличных от фото
   В папке keyboards описана инлайн-кнопка Помощь. В файле model/prediction.py выполняется непосредственное предсказание
3. Сервером для телеграм-бота выбран [Amvera](https://cloud.amvera.ru/projects/compute/fake-or-real). Для сборки создан конфигурационный файл amvera.yml.


   

