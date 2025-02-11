<div style="text-align: center;">
<img src="./images_readme/logo.jpg" width="650" alt="logo"/>
<h1 style="text-align: center">Витрина для онлайн продажи из социальных сетей ВКонтакте.</h1>
</div>

### <img src="images_readme/instruc.jpg" width="70"/> Описание приложения.
Этот проект представляет собой чат-бот для социальной сети ВКонтакте, 
который помогает пользователям просматривать различные 
продукты и услуги. 

Бот может использоваться как платформа для демонстрации и продажи 
различных цифровых товаров, таких как скрипты, плагины, веб-сайты 
и другие не только.

Проект разделён на бекэнд, реализован на связке сервера FastApi и
базы данных Postgres. Фронтэнд реализован с помощью VK_API.
Фронт и бек не завязаны, есть возможность масштабирования
и подключение к серверу сторонних приложений. Общение фронт и бека
происходить по средствам HTTP запросов.

---

### <img src="images_readme/docker.svg" width="40" alt="docker"/> Запуск.
Запуск через Docker-compose:
Открываем терминал, переходим в корневую папку с проектом:

1. Создаём образ командой ```docker-compose build```
2. Поднимаем контейнер ```docker-compose up```

---

### <img src="images_readme/swagger_logo.png" width="40" alt="swagger"/> Swagger.
<img src="./images_readme/swagger.png" style="display:block" width=auto alt="web_enterface"/>

* categories - действия с категориями.
  * get /api/categories/ - получение всех категорий.
  * get /api/categories/<str> - получение всех товаров выбранной категорий.
* products - действия с продуктом.
  * get /api/products/<str> - полная информация о продукте.

---

### <img src="images_readme/tests.jpg" width="50"/> Тестирование.
Тесты запускаются в терминале 
для бекэнда
```
pytest app/tests/
```

для бота
```
pytest vk_api_bot/tests/
```

---

<h2>Лицензия</h2>
Проект распространяется под лицензией MIT.


