# coding=utf-8
import os
import telebot
import urllib
import json

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])

@bot.message_handler(commands=['start', 'help'])
def send_start_message(message):
    bot.reply_to(message, "Olá, eu sou Dorinho. \n "
    "Envie o comando /listhost para listar os hosts.")

@bot.message_handler(commands=[host'])
def send_hosts(message):
    bot.reply_to(message, get_reply_message())


def get_reply_message():
    n_host, host = get_host()
    message = "Lista: " \ 
                + str(n_host) + \ 
                "Hosts. Lista: \n \n"
            