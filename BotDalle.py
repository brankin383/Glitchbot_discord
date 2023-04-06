import openai
import discord

# specifying server for bot
GUILD = "{Glitch.bot}"

#create an object that will controll our discord bot
client = discord.Client(intents=discord.Intents.default())

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

with open("keys.txt") as f:
	lines = f.read().split('\n')
	openai.api_key = lines[0]
	DISCORD_TOKEN = lines[1]

f.close()

client.run(DISCORD_TOKEN)