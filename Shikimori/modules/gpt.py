# Provided By :- @NovaXMod
# Made by :- @ImmortalsXKing
# API Credits :- @ImSafone

import requests
import json
from repo import pbot as app
from pyrogram import filters
from pyrogram.enums import ChatType

@pbot.on_message(filters.command("chat"))
async def gpt(app,message):
	if message.chat.type == ChatType.PRIVATE:
      (txt =await message.reply("**Generating...**")
      if len(message.command) < 2 :
          return await txt.edit("**Give me a query too**")
      query = message.text.split("/chat")[1]
      url = "https://api.safone.me/chatgpt"
      payloads = {
           "message": query,
          "chat_mode": "assistant",
          "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
          }
      headers = {"Content-Type" : "application/json"}
      try:
         response = requests.post(url, json=payloads, headers=headers)
         results = response.json()
         res = results["message"]
         credit = "Provided By :- @Xd_Bots_Updates"
         await txt.edit(f"{res}\n\n{credit}")
      except Exception as e:
         await txt.edit(f"Error :-\n{e}" )
    else:
      txt =await message.reply("**Generating...**")
      if len(message.command) < 2 :
          return await txt.edit("**Give me a query too**")
      query = message.text.split("/chat")[1]
      url = "https://api.safone.me/chatgpt"
      payloads = {
           "message": query,
          "chat_mode": "assistant",
          "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
          }
      headers = {"Content-Type" : "application/json"}
      try:
         response = requests.post(url, json=payloads, headers=headers)
         results = response.json()
         res = results["message"]
         credit = "Provided By :- @Xd_Bots_Updates"
         await txt.edit(f"{res}\n\n{credit}")
      except Exception as e:
         await txt.edit(f"Error :-\n{e}" )
