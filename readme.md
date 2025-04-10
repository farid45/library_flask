# SQLAlchemy ДЗ


## Задание:

1. Создать новый проект Flask.

2. Подключить базу данных к новому проекту. Можно использовать любую реляционную БД.

3. Создать модели Book и Genre.

4. Создать view главной страницы приложения, который выводит 15 последних записей из Book в порядке создания - новые записи вверху списка.

5. Сделать возможность перехода с главной страницы на страницу жанра книги (Genre), где можно увидеть все записи из Book выбранном в жанре.


## Установка:

### Linux - Ubuntu

#### Устанавливаем python, git, и прочии зависимости.

#### Для Debian/Ubuntu
```
sudo apt install python3 git python3-pip
```
#### Для ArchLinux
```
(sudo) pacman -S  python python-pip git
```
или
```
yay -S python python-pip git
```

#### Для Fedora
```
sudo dnf install python3 git
```

### macOS

#### Установить brew, так будет проще.

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```



#### Grab файлы 
```
git clone https://github.com/farid45/library_flask.git
cd library_flask
```

#### Создать venv и установить зависимости
```
python3 -m venv library_flask
source library_flask/bin/activate
pip3 install -r requirements.txt
```

---------------------------------------------------------------------------------------------------------------

### Windows

#### Установить python + git
- Установите Python и git.
- Если вы устанавливаете Python из магазина Microsoft Store, «установка python setup.py» завершится неудачно, но этот шаг не требуется.
- WIN+R ```cmd```

#### Grab файлы и установка
```
git clone https://github.com/farid45/library_flask.git
cd library_flask
pip3 install -r requirements.txt
```

### Запуск приложения:

#### В зависимости от операционной системы, различия по запуску не значительные. (В данном случае показываю пример запуска на MacOs)
```
SQLALCHEMY_DATABASE_URI="sqlite:///project.db" python ./app.py
```

### Запускаем браузер и вставляем следующую ссылку:
```
http://127.0.0.1:5000
```
