# Watcher of Friends Online

At startup, the script asks for the username and password of the user and displays the names and surnames of those of his friends who are online.

Before the first start, you must register your application at https://vk.com/dev and obtain "Application ID". Change the variable `APP_ID` in the source code.

# Example of usage:

```bash
$ python vk_friends_online.py
Login: mail@mail.com
Password:
Online users:
 User Name
 User2 Name2
```

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
