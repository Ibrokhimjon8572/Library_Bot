import telebot
import logging

from django.http import HttpResponse
from telebot import types
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.utils.translation import gettext as _
from django.http.request import HttpRequest
from .models import TelegramUser, Book, BookSubject
from .bot import Control

BOT_TOKEN = getattr(settings, "BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

ok = False
@csrf_exempt
def index(request: HttpRequest):
    print(request, request.body, request.headers)
    if request.method == 'GET':
        return HttpResponse("Delever Telegram Bot")
    if request.method == 'POST':
        update = telebot.types.Update.de_json(
                request.body.decode("utf-8"))
        print(update)
        bot.process_new_updates([update])
        return HttpResponse(status=200)


@bot.message_handler(commands=['start'])
def handle_start(msg: types.Message):
    tg_user = msg.from_user
    try:
        referal_code = msg.text.split()[-1]
        try:
            referred_by = TelegramUser.objects.get(referal_code=referal_code)
        except:
            referred_by = None
        print(tg_user)
        control = Control(tg_user, referred_by)
        control.handle_start_cmd(tg_user)
    except Exception as e:
        logging.error("Error while handling start cmd: " + str(e))
        logging.exception("message")
    

@bot.message_handler(content_types=["text"])
def handle_text_message(msg: types.Message):
    try:
        user = TelegramUser.objects.get(user_id = msg.from_user.id)
        control = Control(msg.from_user)
    except:
        return
    if msg.from_user.id != msg.chat.id:
        return
    if user.step == "start":
        control.handle_start_cmd(msg.from_user)
        return
    if user.step == "ask_name":
        control.handle_name_sent(msg.from_user, msg.text)
        return

    if user.step == "ask_grade":
        control.handle_grade_sent(msg.from_user, msg.text)
        return
    if user.step == "ask_subject":
        control.handle_subject_sent(msg.from_user, msg.text)
        return
    control.handle_start_cmd(msg.from_user)
@bot.message_handler(content_types=["document"])
def handle_document(msg: types.Message):
    book = Book()
    book.name = msg.document.file_name
    subject = BookSubject()
    subject.name = msg.document.file_id
    subject.save()
    book.subject = subject
    book.save()



