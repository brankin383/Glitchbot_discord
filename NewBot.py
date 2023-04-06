import openai
import discord
import os

# specifying server for bot
GUILD = "{Glitch.bot}"

#create an object that will controll our discord bot
client = discord.Client(intents=discord.Intents.default())
openai.api_key = os.environ["API_Key"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
openai.api_base = os.envir["API_BASE"]

@client.event
async def on_ready():
	for guild in client.guilds:
		if guild.name == GUILD:
			break
	#print statement
	print(f'{client.user} has connected to Discord!')

@client.event
#pevent indefinite loop of bot on bot love
async def on_message(message):
	if message.author == client.user:
		return
	#bot will reply when mentioned
	elif client.user.mentioned_in(message):
		response = openai.Image.create(
			prompt=message.content,
			n=1,
			size='1024x1024'
		)
		image_url = response['data'][0]['url']
		print(image_url)
		await message.channel.send(image_url)

client.run(DISCORD_TOKEN)