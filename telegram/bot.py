from queue import Queue
import telebot
from telebot import types

from telebot.types import User, Contact
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
#from .models import BotSettings, Channel, TelegramUser, Transaction
from .models import TelegramUser, Book
from .strings import *
from .utils import *
import glob

BOT_TOKEN = getattr(settings, "BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)



class Control:
    def __init__(self, tg_user: User, referred_by: TelegramUser = None):
        self.user_id = tg_user.id
        self.user, _ = TelegramUser.objects.get_or_create(user_id=tg_user.id, defaults={
            'username': tg_user.username,
        })


    def handle_start_cmd(self, user: User):
        self.reply(hello_ask_name())
        self.user.step = "ask_name"
        self.user.save()


    def handle_name_sent(self, user: User, text):
        if any([i.isdigit() for i in text]):
             self.reply(ask_name())
             return
        self.user.fullname = text
        self.user.step = "ask_grade"
        self.user.save()
        self.reply(ask_grade(text))

    def handle_grade_sent(self, user: User, text):
        try:
            grade = extract_number(text)
        except:
            self.reply(didnt_understand())
            return
        self.user.grade = grade
        self.user.step = "ask_subject"
        self.user.save()
        self.reply(ask_subject())

    def handle_subject_sent_(self, user: User, text):
        self.user.subject = text.split()[0]
        self.user.step = "start"
        self.user.save()
        files = glob.glob(f"./books/{self.user.grade}.{self.user.subject.lower()}*.pdf")
        for i in files:
            file = open(i, 'rb')
            print(bot.send_document(self.user.user_id, file))
            file.close()
        self.reply(bye())
    def handle_subject_sent(self, user: User, text):
        self.user.subject = text.split()[0]
        self.user.step = "start"
        self.user.save()
        if "audio" in text.lower():
            self.reply("Ushbu kanallardan audio kitoblarni olishingiz mumkin: \nhttps://t.me/mtrkaudiokitoblar\n\nhttps://t.me/audio_ertaklar_xikoya_hikoyalari")
            self.reply("Yana yordam kerak bo'lsa yozing")
            return
        count = 0
        files = Book.objects.filter(name__startswith=str(self.user.grade)).filter(name__icontains=self.user.subject)
        for file in files:
            bot.send_document(self.user.user_id, file.subject.name)
            count += 1
        if count == 0:
            self.reply("Afsuski bunday kitoblar bizda hali yo'q ekan. Lekin https://kitob.uz saytidan qidirib ko'rishingiz mumkin")
            self.reply("Yana yordam kerak bo'lsa yozing")
            return # self.reply("Yana yordam kerak bo'lsa yozing")
        self.reply(bye())
        self.reply("Yana yordam kerak bo'lsa yozing")



    def reply(self, text, markup = None):
        bot.send_message(self.user.user_id, text, parse_mode='html', reply_markup=markup)

