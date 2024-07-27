# -*- coding: utf-8 -*-
"""start_help.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Tc8cJdozQOCvpuzuf-R0jNTmgfjGG-aZ
"""

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.help_button import get_help_kb

router = Router()  # [1]

@router.message(Command("start"))  # [2]
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я бот, распознающий сгенерировано ли изображение нейросетью или сделано человеком.",
        reply_markup=get_help_kb()
    )

@router.message(Command("help"))
async def help(message: Message):
    await message.answer("Просто отправьте мне изображение в формате jpg, jpeg или png.")


@router.message(F.text == "Помощь")
async def help(message: Message):
    await message.answer(
        "Просто отправьте мне изображение в формате jpg, jpeg или png."
    )