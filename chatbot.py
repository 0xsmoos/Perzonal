# -*- coding: utf-8 -*-
# filename          : chatbot.py
# description       : Talk to humans and make them feel good
# author            : Warren
# email             : warren@secmail.pro
# date              : 03-06-1970
# version           : v1.0
# usage             : python chatbot.py
# notes             :
# license           : MIT
# py version        : 3.9.7 (must run on 3.6 or higher)
#==============================================================================
from discord.ext import commands
from prsaw import RandomStuff

bot = commands.Bot(command_prefix=">")
rs = RandomStuff(async_mode = True, api_key = 'WtqiODHitCgi')

@bot.event
async def on_message(message):
	if bot.user == message.author:
		return

	if message.channel.id == 862050746191314984:
		response = await rs.get_ai_response(message.content)
		await message.reply(response)

	await bot.process_commands(message)

TOKEN = ''
bot.run(TOKEN)
