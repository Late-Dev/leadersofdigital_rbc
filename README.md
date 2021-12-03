# leadersofdigital_rbc
-    Создайте виртуальное окружение `python -m venv venv`
-    Активируйте его `source venv/bin/activate`
-    установите зависимости `pip install -r requirements.txt`, установится pytorch, он весит около 1гб
-    запустите проект `python app.py`


Запустится веб-интерфейс с двумя страницами (ссылки на странице в шапке):
-    NewsFeed - страница с предобработанными видео с извлеченными из них аудио
-    Admin - страница с формой загрузки своего видео


## Реализована функциональность:
-    Веб-интерфейс с возможностью загрузить видео
-    Преобразование видео в аудио 
-    Извлечение текста из аудио
-    Вывод текста в веб-интерфейс
-    Страница с предобработанными видео и примерами распознавания

## Особенности проекта:
-    Очень свежая предобученная модель Speech-to-Text (Меньше месяца)
-    Дообучение на наборе данных заказчика
-    Поддержка нескольких языков (русский, английский)
-    Постобработка текста: исправление ошибок, поиск именованных сущностей, денормализация текста

## Основной стек технологий
-    Pytorch, transformers
-    Dash, Dash bootstrap
-    Docker

## Демо
Доступно (по ссылке)[example.com] 