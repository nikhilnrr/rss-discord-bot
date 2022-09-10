import nextcord.ext.commands
from nextcord import Intents

intents = Intents.default()
intents.message_content = True

client = nextcord.ext.commands.Bot(intents = intents, command_prefix="rss!")


@client.listen()
async def on_ready():
    print("running")


with open("token.secret") as token_file:
    client.run(token_file.read().strip())
