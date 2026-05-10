# Техническое руководство по созданию Telegram-бота «Семейные традиции»

## Для кого это руководство

Это руководство для начинающих, которые хотят создать своего первого Telegram-бота на Python. Вам не нужны специальные знания — достаточно уметь пользоваться компьютером и Telegram.

## Что вы создадите

Вы создадите бота, который хранит семейные традиции, показывает список всех традиций, добавляет новые традиции, напоминает о традициях по дате и присылает случайные напоминания.

## Содержание

1. Подготовка компьютера
2. Создание бота в Telegram
3. Написание кода
4. Запуск бота
5. Проверка работы
6. Возможные проблемы и решения
7. Как улучшить бота

## 1. Подготовка компьютера

### Шаг 1.1. Установите Python

Python — это язык программирования, на котором мы будем писать бота.

Откройте браузер и перейдите на сайт https://www.python.org/downloads/ . Нажмите на жёлтую кнопку "Download Python" для самой последней версии. Запустите скачанный файл. В самом начале установки обязательно поставьте галочку "Add Python to PATH". Затем нажмите "Install Now" и дождитесь окончания установки.

Чтобы проверить, что Python установлен правильно, откройте командную строку. Для этого нажмите Win + R, введите cmd и нажмите Enter. В чёрном окне командной строки напечатайте python --version и нажмите Enter. Вы должны увидеть что-то вроде Python 3.11.5.

### Шаг 1.2. Установите библиотеку для бота

Библиотека — это готовый набор кода, который упрощает создание бота. В той же командной строке напечатайте pip install pyTelegramBotAPI и нажмите Enter. Вы увидите процесс установки. Если появились слова Successfully installed — библиотека установлена.

### Шаг 1.3. Создайте папку для проекта

Создайте на рабочем столе новую папку. Назовите её family_bot. Для этого нажмите правой кнопкой мыши на рабочем столе, выберите "Создать" — "Папку" и введите имя family_bot.

## 2. Создание бота в Telegram

### Шаг 2.1. Найдите BotFather

BotFather — это официальный бот, который создаёт других ботов. Откройте Telegram на телефоне или компьютере. Нажмите на строку поиска вверху и введите @BotFather. Выберите бота с синей галочкой.

### Шаг 2.2. Создайте нового бота

Отправьте BotFather команду /newbot. BotFather попросит вас придумать имя бота. Напишите любое имя, например "Семейные традиции". Затем BotFather попросит придумать username — уникальное имя, которое заканчивается на _bot. Например, family_traditions_bot или sem_trad_bot. Если имя уже занято, BotFather попросит придумать другое.

### Шаг 2.3. Получите токен

После успешного создания BotFather отправит вам сообщение с токеном. Токен выглядит как длинная строка букв и цифр, например 1234567890:ABCdefGHIJKlmNOPqRsTUVwxyz. Это ключ доступа к вашему боту. Скопируйте его и сохраните в надёжном месте. Никому не показывайте этот токен.

## 3. Написание кода

### Шаг 3.1. Откройте редактор кода

Вы можете использовать любой текстовый редактор. Подойдёт обычный Блокнот, который есть в каждой Windows. Также можно использовать VS Code, PyCharm или IDLE, который устанавливается вместе с Python.

### Шаг 3.2. Создайте файл bot.py

В папке family_bot создайте новый файл. Назовите его bot.py. Важно, чтобы расширение было .py, а не .txt. Если вы используете Блокнот, при сохранении выберите "Все файлы" и напишите имя bot.py.

### Шаг 3.3. Скопируйте код

Скопируйте следующий код и вставьте его в файл bot.py:

```python
import telebot
import json
import os
from datetime import datetime
import random

TOKEN = 'ВАШ_ТОКЕН'
DATA_FILE = 'traditions.json'

bot = telebot.TeleBot(TOKEN)

def load_traditions():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_traditions(traditions):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(traditions, f, ensure_ascii=False, indent=2)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Семейный архив традиций\n\n'
        'Доступные команды:\n'
        '/traditions — показать все традиции\n'
        '/add — добавить новую традицию\n'
        '/today — что сегодня?\n'
        '/remind — случайное напоминание\n'
        '/help — помощь'
    )

@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        'Справка по командам\n\n'
        '/start — главное меню\n'
        '/traditions — список всех традиций\n'
        '/add — добавить традицию в формате:\n'
        'Название | ДД.ММ | Описание\n\n'
        'Пример:\n'
        'Новый год | 31.12 | Украшаем ёлку всей семьёй'
    )

@bot.message_handler(commands=['traditions'])
def show_traditions(message):
    traditions = load_traditions()
    
    if not traditions:
        bot.send_message(
            message.chat.id,
            'У вас пока нет традиций. Добавьте первую традицию через команду /add'
        )
        return
    
    text = 'Ваши семейные традиции:\n\n'
    for i, (name, info) in enumerate(traditions.items(), 1):
        text += str(i) + '. ' + name + '\n'
        text += '   Дата: ' + info['date'] + '\n'
        text += '   Описание: ' + info['desc'] + '\n\n'
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['today'])
def today_tradition(message):
    traditions = load_traditions()
    today_str = datetime.now().strftime('%d.%m')
    
    found = None
    for name, info in traditions.items():
        if info['date'] == today_str:
            found = (name, info)
            break
    
    if found:
        name, info = found
        text = 'Сегодня ' + name + '!\n\n' + info['desc']
    else:
        text = 'Сегодня (' + today_str + ') нет запланированных традиций.\n\nВы можете добавить новую через /add'
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['add'])
def add_start(message):
    bot.send_message(
        message.chat.id,
        'Как добавить традицию:\n\n'
        'Отправьте сообщение в формате:\n'
        'Название | ДД.ММ | Описание\n\n'
        'Пример:\n'
        'День рождения бабушки | 15.03 | Позвонить и поздравить'
    )

@bot.message_handler(commands=['remind'])
def random_remind(message):
    traditions = load_traditions()
    
    if not traditions:
        bot.send_message(
            message.chat.id,
            'Нет традиций для напоминания. Добавьте их через /add'
        )
        return
    
    name, info = random.choice(list(traditions.items()))
    text = 'Напоминание о традиции!\n\n'
    text += name + '\n'
    text += 'Дата: ' + info['date'] + '\n'
    text += 'Описание: ' + info['desc']
    
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda message: '|' in message.text)
def add_save(message):
    parts = message.text.split('|')
    
    if len(parts) < 2:
        bot.send_message(
            message.chat.id,
            'Неправильный формат. Используйте: Название | ДД.ММ | Описание'
        )
        return
    
    name = parts[0].strip()
    date = parts[1].strip()
    desc = parts[2].strip() if len(parts) > 2 else ''
    
    if not name or not date:
        bot.send_message(message.chat.id, 'Название и дата обязательны')
        return
    
    traditions = load_traditions()
    traditions[name] = {'date': date, 'desc': desc}
    save_traditions(traditions)
    
    bot.send_message(
        message.chat.id,
        'Традиция "' + name + '" добавлена!\n'
        'Дата: ' + date + '\n'
        'Описание: ' + desc
    )

if __name__ == '__main__':
    print('Бот "Семейные традиции" запущен')
    print('Жду команд в Telegram')
    bot.infinity_polling()
