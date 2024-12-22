import telebot
from telebot import types

# Токен бота
TOKEN = '7796014729:AAFf2Ae-9kPGtcR5qS0VmG6aGR73OZWhEX8'
bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('🚚 Гузоштани заявка барои доставка')
    item2 = types.KeyboardButton('🔍 Тафтиш кардани трек-код')
    item4 = types.KeyboardButton('📍 Нишони складҳо')
    item5 = types.KeyboardButton('💰 Нархҳо')
    item6 = types.KeyboardButton('📚 Курсҳои ройгон')
    item7 = types.KeyboardButton('🔴 Маҳсулотҳои маншуда')
    item8 = types.KeyboardButton('📞 Бо оператор ба тамос бромадан')
    markup.add(item1, item2, item4, item5, item6, item7, item8, )

    bot.send_message(
        message.chat.id,
        f'Салом, {message.from_user.first_name}🖐',
        reply_markup=markup
    )


# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '💰 Нархҳо':
            bot.send_message(
                message.chat.id,
                '👨‍🏫 Аз 1 То 50 кг \n 1кг : 2.5доллар\n 1куб : 250 доллар\n\n'
                '👨‍🏫 Аз 50 То 100 кг\n1 кг : 2.4 доллар\n1 куб : 240 доллар\n\n'
                '👨‍🏫 Аз 100 То 200 кг\n1 кг : 2.3 доллар\n1 куб : 230 доллар\n\n'
                '👨‍🏫 Аз 200 То 300 кг\n1 кг : 2.2 доллар\n1 куб : 220 доллар\n\n'
            )
        elif message.text == '📞 Бо оператор ба тамос бромадан':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️Баромад')
            markup.add(back)
            bot.send_message(
                message.chat.id,
                'Instagram: https://www.instagram.com/barodar_cargo\n'
                'WhatsApp: https://api.whatsapp.com/phone=992000208746',
                reply_markup=markup
            )
        elif message.text == '🚚 Гузоштани заявка барои доставка':
            bot.send_message(
                message.chat.id,
                '🚫 Оператор машғул аст \n'
                '☎️ Шумо метавонед бо чунин роҳҳо ба мо тамос бароед.\n'
                '📞 Телефон барои даставка: +992780310909\n'
                '📞 Телефон барои ёри: +992000208746'
            )
        elif message.text == '📚 Курсҳои ройгон':
            bot.send_message(
                message.chat.id,
                '📚 Курсҳои ройгон: https://t.me/barodarkargo'
            )
        elif message.text == '📍 Нишони складҳо':
            bot.send_message(
                message.chat.id,
                '🏪 Суроғаи анбори ш. Душанбе \n'
                'Nekruz 13579266474 新疆维吾尔自治区乌鲁木齐市新市区 北京南路科学二接学生公寓快递柜'
            )
        elif message.text == '🔴 Маҳсулотҳои маншуда':
            bot.send_message(
                message.chat.id,
                '• Ашёҳои шишагӣ\n'
                '• Яроқ ва ашёҳои ҳарбӣ (кордҳ хуланда)\n'
                '• Маводҳои хатарнок\n'
                '• Маводҳои наркотикӣ ва психотропӣ\n'
                '• Ҳайвонот ва растаниҳо\n'
                '• Маводҳои порнографӣ\n'
                '• Маҳсулотҳои хӯрока ва тиббӣ\n'
                '• Пул ва ҳуҷҷатҳои қалбакӣ'
            )
        elif message.text == '🔍 Тафтиш кардани трек-код':
            file_path = 'guide.pdf'  # Замените на путь к вашему файлу
            try:
                with open(file_path, 'rb') as file:
                    bot.send_document(message.chat.id, file)
            except FileNotFoundError:
                           bot.send_message(message.chat.id, '🔍 Тафтиш кардани трек-код айни хол дастнорас мебошад. Лутфан, барои маълумоти бештар ба [https://t.me/barodarkargo] муроҷиат кунед.')
        elif message.text == '⬅️Баромад':
            start(message)
        else:
            bot.send_message(message.chat.id, '🔍 Тафтиш кардани трек-код айни хол дастнорас мебошад. Лутфан, барои маълумоти бештар ба [канали Telegram] муроҷиат кунед.')


# Запуск бота
bot.polling(none_stop=True)
