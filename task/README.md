# Исследование и создание Telegram-бота «Семейные традиции»

## Оглавление

1. Введение
2. Последовательность исследования предметной области
3. Проектирование команд бота
4. Разработка и тестирование
5. Техническое руководство по созданию Telegram-бота «Семейные традиции»
6. Написание кода

---

## 1. Введение

**Цель работы** — исследовать возможности Telegram Bot API и создать простого бота для хранения и отображения семейных традиций.

**Задачи:**
- Изучить принципы работы Telegram-ботов
- Выбрать подходящую библиотеку Python
- Спроектировать команды бота
- Реализовать хранение данных
- Протестировать и модифицировать бота

**Актуальность:** семейные традиции укрепляют связи между родственниками, но часто забываются. Бот помогает хранить их в удобном виде и напоминать о важных датах.

---

## 2. Последовательность исследования предметной области

### Этап 1. Изучение Telegram Bot API

| Действие | Результат |
|----------|-----------|
| Прочитана документация Telegram Bot API | Поняты принципы: токен бота, команды, обновления |
| Сравнены библиотеки Python | Выбрана `pyTelegramBotAPI` из-за простоты |
| Изучены типы сообщений и клавиатур | Определён набор команд |

**Основные понятия:**
- **Токен бота** — уникальный ключ для доступа к API
- **Polling** — метод получения обновлений (бот сам спрашивает Telegram)
- **Команды** — сообщения, начинающиеся с `/`

### Этап 2. Изучение хранения данных

| Вариант | Плюсы | Минусы | Решение |
|---------|-------|--------|---------|
| JSON | Простой, читаемый | Не для больших объёмов | ✅ Выбран |
| SQLite | Быстрый, надёжный | Требует знаний SQL | ❌ Отложен |
| Текстовый файл | Очень простой | Сложно парсить | ❌ Не подходит |

**Итог:** выбран JSON как самый простой для начинающих.

### Этап 3. Проектирование команд бота

| Команда | Назначение | Обязательность |
|---------|------------|----------------|
| `/start` | Приветствие и список команд | ✅ Обязательна |
| `/traditions` | Показать все традиции | ✅ Обязательна |
| `/add` | Добавить новую традицию | ✅ Обязательна |
| `/today` | Какая традиция сегодня | ✅ Обязательна |
| `/remind` | Случайное напоминание | Дополнительно |
| `/help` | Помощь | Рекомендуется |

### Этап 4. Разработка и тестирование

| Действие | Результат |
|----------|-----------|
| Написан базовый код | Бот отвечает на команды |
| Проведено ручное тестирование | Все команды работают |
| Исправлены ошибки ввода | Добавлена обработка формата |
| Добавлена модификация `/remind` | Бот отправляет напоминания |

### Итог исследования

- ✅ Telegram Bot API доступен для начинающих
- ✅ `pyTelegramBotAPI` — надёжная библиотека
- ✅ JSON подходит для небольших проектов
- ✅ Бота можно легко расширять

---

# Этап 5. Техническое руководство по созданию Telegram-бота «Семейные традиции»

## 5. Подготовка компьютера

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

## 6. Написание кода

### Шаг 1.1. Откройте редактор кода

Вы можете использовать любой текстовый редактор. Подойдёт обычный Блокнот, который есть в каждой Windows. Также можно использовать VS Code, PyCharm или IDLE, который устанавливается вместе с Python.

### Шаг 1.2. Создайте файл bot.py

В папке family_bot создайте новый файл. Назовите его bot.py. Важно, чтобы расширение было .py, а не .txt. Если вы используете Блокнот, при сохранении выберите "Все файлы" и напишите имя bot.py.

### Шаг 1.3. Скопируйте код

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
