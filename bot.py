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
		response = openai.ChatCompletion.create(
			model="gpt-3.5-turbo",
			messages=[
			{"role": "system", "content": "you are a knowledgable glitch feminist. Make sure all responses are less than 2000 characters"},
			{"role": "user", "content": "What is Glitch Feminism?"}
			]
		)
		await message.channel.send(response.choices[0].message.content)
		print(message.content)

with open("keys.txt") as f:
	lines = f.read().split('\n')
	openai.api_key = lines[0]
	DISCORD_TOKEN = lines[1]

f.close()





client.run(DISCORD_TOKEN)