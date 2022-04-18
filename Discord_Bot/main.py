# Discord API
import discord
from discord.ext import commands

# Другое
import color as Color
import platform
import ctypes

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
	print(f'{Color.GREEN}Бот успешно запущен.{Color.RESET}')

@bot.event
async def on_member_join(member):
	member = str(member).split('#')[0]

	print(f'{Color.GREEN}Пользователь {Color.MAGENTA}{member}{Color.GREEN} присоединился к серверу.{Color.RESET}')
	channel = bot.get_channel(903423262443315270)
	await channel.send(f'**{member}**, теперь с нами 🤩')

@bot.event
async def on_member_remove(member):
	member = str(member).split('#')[0]

	print(f'{Color.RED}Пользователь {Color.MAGENTA}{member}{Color.GREEN} вышел с сервера.{Color.RESET}')
	channel = bot.get_channel(903423218658996314)
	await channel.send(f'**{member}**, нам будет его не хватать 😢')

@bot.event
async def on_message(message):
	message.content = message.content.lower()
	if message.content.startswith('!cat'):
		embed = discord.Embed(color=0xff9900, title='Cat 🤤')
		embed.set_image(url='https://cdnn21.img.ria.ru/images/07e5/02/1a/1599054973_0:383:2048:1535_1920x0_80_0_0_82fec75b402fe33b2c83abff6c090b3e.jpg')
		await message.channel.send(embed=embed)

if __name__ == '__main__':
	if platform.system() == 'Windows':
		kernel32 = ctypes.windll.kernel32
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
	bot.run('СЮДА ВАШ ТОКЕН БОТА!!!')