import telebot

from telebot import types
from django.utils.translation import gettext as _
import random

_hello_texts = ["""
Assalomu alaykum!
Men xalq ta'limi kutubxonasi botiman.
Sizningi ismingizni bilsam bo'ladimi?
""", 
"""
Salom! Xalq ta'limi kutubxonasi, ismingiz nima?
""",
"Xayrli kun! Sizga qanday murojaat qilsam bo'ladi?",
"""
Assalomu alaykum! Ismingiz nima?
"""
]

_ask_grade_texts = ["""
Tanishganimdan xursandman, {name}.
Sizga qaysi sinf darsliklari kerak?
""",
"""Ajoyib! {name}, sizni nechanchi sinf kitoblari qiziqtiradi?""",
"""Rahmat, {name}. Nechanchi sinf darsliklari kerak?""",
"""{name}, chiroyli ism ekan :)
Nechanchi sinfda o'qiysiz?""",
]


_ask_subject_texts = ["""
Zo'r!
Qaysi fan kitoblari kerak?
""",
"""
Yaxshi. Bizda hamma fanlar bo'yicha kitoblar bor. Sizga ko'proq qaysi fan qiziq?""",
"""
👍 Qaysi fan bo'yicha adabiyotlar kerak?"""
]


_didnt_understand_texts = ["""
Kechirasiz, tushunmadim?
""",
"""
🤔 Tushunmay qoldimku
""",
"""
Nechanchi sinfligingizni aytmasangiz, sizga qanday kitob kerak ekanligini bilolmaymanku
"""
]

_didnt_understand_name = ["""
Kechirasiz, tushunmadim. Ismingiz nima?
""",
"""
Kim deb murojaat qilsam bo'ladi?
""",
"""
Ismingizni qaytarib yuborasizmi?
"""
]
_bye_texts = ["""
Shu kitoblar bor ekan.
Sizga foydasi tegadi degan umiddaman :)
""",
"""
Shu kitoblarni topdim. Yana kerak bo'lsam yozing, doim xizmatingizga tayyorman
""",
]



def hello_ask_name():
    return random.choice(_hello_texts)


def ask_grade(name):
    return random.choice(_ask_grade_texts).format(name=name)

def ask_subject():
    return random.choice(_ask_subject_texts)

def didnt_understand():
    return random.choice(_didnt_understand_texts)


def bye():
    return random.choice(_bye_texts)
def ask_name():
    return random.choice(_didnt_understand_name)
