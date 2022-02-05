# 1060-flask-server
Пошаговое создание Web-сервера на Flask с использованием материалов от HTML Academy.

## ШАГ 0 - Подготовка

### Создать папку проекта
Для проекта нужна отдельная папка, где будут лежать все материалы, связанные с ним.  
Ее можно назвать `flask-server` или любым другим понятным именем.  
Созданную папку нужно открыть как проект в используемой IDE (например, [PyCharm][pycharm-download-link]):  
`Open Folder as PyCharm Project`

### Создать виртуальное окружение
В только что созданной и открытой папке нужно создать виртуальное окружение. Обычно его помещают в папку `venv` в корне проекта:  
```
flask-server  
|-- venv
```

Это можно сделать двумя способами:
1. Средствами IDE (в PyCharm: *File* -> *Settings* -> *Project Interpreter* ->
   <img height="20" src=".\pic\settings-pic.png" width="20"/> -> *Add*)
2. Командой в системном терминале `python -m venv venv`

### Установка пакета Flask
Установить пакет Flask тоже можно двумя способами:
1. Средствами IDE (в PyCharm: *File* -> *Settings* -> *Project Interpreter* ->
   <img height="20" src=".\pic\add-module-pic.png" width="20"/> -> *Flask* -> *Install Package*)
2. Командой в системном терминале `pip install flask`.


[pycharm-download-link]: https://www.jetbrains.com/pycharm/download/ "Скачать PyCharm"