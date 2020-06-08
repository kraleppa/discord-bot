import discord
from response_dictionary import analyze_message
from key import key


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):

        if message.author == self.user:
            return

        answer = analyze_message(message.content)
        if answer is None:
            return
        await message.channel.send(answer)


client = MyClient()

client.run(key)
