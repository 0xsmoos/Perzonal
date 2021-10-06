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

TOKEN = 'ODYxNjcwNjE0MjU4NDE3Njc0.YONLSw.ojgmYuD4hz9o4UUkHASKDhcYXtg'
bot.run(TOKEN)