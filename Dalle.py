import openai

with open("keys.txt") as f:
	lines = f.read().split('\n')
	openai.api_key = lines[0]
	DISCORD_TOKEN = lines[1]

f.close()

response = openai.Image.create(
	prompt='Irish people drinking and getting crazy at the pub',
	n=1,
	size='1024x1024'
)
image_url = response['data'][0]['url']
print(image_url)