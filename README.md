# leadersofdigital_rbc

## Требования
Установленный Docker и nvidia-docker для запуска на gpu

-    Загрузить подготовленный docker образ `docker pull electriclizard/rbc:latest`
-    Запустить контейнер на цпу `docker run -p 8050:8050 electriclizard/rbc:latest` и приложение откроется на порту 8050
-    Для запуска на gpu `docker run --runtime nvidia -p 8050:8050 electriclizard/rbc:latest`

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
-    Pytorch, transformers, DeepPavlov
-    Dash, Dash bootstrap
-    Docker

## Демо
Доступно [по ссылке](http://89.248.193.164:8050/admin)
