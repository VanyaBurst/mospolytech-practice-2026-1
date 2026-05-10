import telebot
from datetime import datetime

TOKEN = '8027534318:AAHW_zjesdQfmlufMw2O5-3HY8dR9H6eSNs'

bot = telebot.TeleBot(TOKEN)

# База традиций (можно сохранять в файл)
traditions = {
    
}


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     '👨‍👩‍👧‍👦 *Семейный архив традиций*\n\n'
                     '📋 /traditions — список традиций\n'
                     '➕ /add — добавить традицию\n'
                     '📅 /today — что сегодня?\n'
                     '📖 /help — помощь',
                     parse_mode='Markdown')


@bot.message_handler(commands=['traditions'])
def show_traditions(message):
    if not traditions:
        bot.send_message(message.chat.id, 'Пока нет традиций. Добавьте через /add')
        return

    text = '📚 *Ваши семейные традиции:*\n\n'
    for i, (name, info) in enumerate(traditions.items(), 1):
        text += f'{i}. 🎯 *{name}*\n   📅 {info["date"]}\n   📝 {info["desc"]}\n\n'

    bot.send_message(message.chat.id, text, parse_mode='Markdown')


@bot.message_handler(commands=['today'])
def today(message):
    today_str = datetime.now().strftime('%d.%m')
    text = f'📅 *Сегодня {datetime.now().strftime("%d.%m")}*\n\n'

    found = False
    for name, info in traditions.items():
        if info['date'] == today_str:
            text += f'🎉 Сегодня {name}!\n   {info["desc"]}'
            found = True
            break

    if not found:
        text += 'Сегодня нет запланированных традиций.\nЗато можно создать новую — /add'

    bot.send_message(message.chat.id, text, parse_mode='Markdown')


@bot.message_handler(commands=['add'])
def add_start(message):
    bot.send_message(message.chat.id,
                     '➕ *Как добавить традицию:*\n\n'
                     'Отправь сообщение в формате:\n'
                     '`Название | Дата | Описание`\n\n'
                     'Пример:\n'
                     '`Пикник | 01.05 | Едем на природу всей семьёй`',
                     parse_mode='Markdown')


@bot.message_handler(func=lambda m: '|' in m.text)
def add_save(message):
    parts = message.text.split('|')
    if len(parts) >= 2:
        name = parts[0].strip()
        date = parts[1].strip()
        desc = parts[2].strip() if len(parts) > 2 else ''

        traditions[name] = {'date': date, 'desc': desc}
        bot.send_message(message.chat.id, f'✅ Традиция "{name}" добавлена!')
    else:
        bot.send_message(message.chat.id, '❌ Неправильный формат. Используй: Название | Дата | Описание')


@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.send_message(message.chat.id,
                     '📖 *Команды бота:*\n\n'
                     '/start — Главное меню\n'
                     '/traditions — Все традиции\n'
                     '/add — Добавить традицию\n'
                     '/today — Что сегодня\n'
                     '/help — Эта справка')


print('Бот запущен! 🎉')
bot.infinity_polling()