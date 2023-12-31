### Структура приложения
#### v.0.1.

<pre>
📁 <b>Social_Network</b> | <i>Корневой каталог.</i>
|   📁 <b>app</b> | <i>Каталог приложения.</i>
|   |  📁 <b>models</b> | <i>Модели SQLAlchemy.</i>
|   |   |   | __init__.py
|   |   |   | user.py | <i>Модель User с атрибутами и методами, связанными с пользователями.</i>
|   |   |   | post.py | <i>Модель Post, описывающую записи в блоге или обновления статуса.</i>
|   |   |   | comment.py | <i>Модель Comment, описывающую комментарии к сообщениям.</i>
|   |   |   | like.py | <i>Модель Like, предназначенную для "лайка" сообщений или комментариев.</i>
|   |   |   | relationship.py | <i>Модель Relationship для представления отношений "последователь-последователь" или дружеских отношений.</i>
|   |  📁 <b>templates</b> | <i>HTML-шаблоны.</i>
|   |   |   | base.html
|   |   |   | index.html
|   |   |   | login.html
|   |   |   | register.html
|   |   |   | profile.html
|   |   |   | post.html
|   |  📁 <b>static</b> | <i>Статические файлы</i>
|   |   |  📁 <b>css</b>
|   |   |  📁 <b>js</b>
|   |   |  📁 <b>images</b>
|   |  📁 <b>blueprints</b> | <i>Модульные компоненты приложения Flask.</i>
|   |   |   | __init__.py
|   |   |   | auth.py | <i>Обработка аутентификации.</i>
|   |   |   | main.py | <i>План основных / общих частей сайта.</i>
|   |  📁 <b>utils</b> | <i>Функции и классы полезности.</i>
|   |   |   | helpers.py | <i>Различные вспомогательные функции, которые не всегда вписываются в логику или модели приложения.</i>
|   |   | __init__.py | <i>Файл, в котором инициализируется приложение Flask и его расширения.</i>
|   |   | routes.py | <i>Здесь определяются маршруты приложения, если не используются чертежи.</i>
|  📁 <b>migrations</b> | <i>Каталог для хранения файлов SQLAlchemy-migrate.</i>
|  📁 <b>tests</b> | <i>Каталог для хранения модульных тестов.</i>
|   | config.py | <i>Конфигурации приложения</i>
|   | my_key.py | <i>Установка в окружение SECRET_KEY</i>
|   | run.py | ▶️ ТОЧКА <i>входа в приложение</i>
|   | requirements.txt | <i>Зависимости проекта</i>
</pre>

<hr>

