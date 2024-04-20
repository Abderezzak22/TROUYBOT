import os
import telebot
from domain_layer import get_response

TELEGRAM_API_KEY = '7146425791:AAEhuPiNYLvMbjBJWHqMYYr-SUcKOlE2_8w'
bot = telebot.TeleBot(TELEGRAM_API_KEY)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    help_text = """مرحبًا بك في 𝐓𝐑𝐎𝐔𝐘 🤖
    
تم دمج هذا الروبوت مع الذكاء الاصطناعي. يمكنك طرح الأسئلة عليه وسيقدم لك الإجابات بناءً على قدرات الذكاء الاصطناعي الخاصة به.

وإليك كيفية استخدامه:

1. ما عليك سوى كتابة سؤالك في الدردشة وإرساله.
2. سيقوم الروبوت بمعالجة سؤالك وتقديم إجابة في أقرب وقت ممكن.

يرجى ملاحظة أن جودة الإجابة تعتمد على مدى تعقيد السؤال. تم تصميم الروبوت للتعامل مع مجموعة واسعة من المواضيع، لكنه قد لا يتمكن من الإجابة على أسئلة محددة أو معقدة للغاية.

تم تطويري من قبل: @AY_Y4
استمتع باستخدامي 🥰♥
    """
    bot.reply_to(message, help_text)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    wait_message = bot.reply_to(message, "ستنى نشوف..🕐")
    response = get_response(message.text)
    bot.delete_message(wait_message.chat.id, wait_message.message_id)
    bot.reply_to(message, response.text)




bot.infinity_polling()

