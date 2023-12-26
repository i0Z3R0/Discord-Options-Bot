import selfcord
import os

# token = "ODIzMTI1MzcxMTA4NTg5NTg5.GB1GrR.MEwxRHyvz5bl1ynXrZwr-6cLs2ygf8sC_ytCmI"
token = "NTE1MzkyNTc3OTE5MjU0NTUx.GHQift.srGT5-E9MLFLP5XYTyGnHJFlh50l3cxS1SOxzA"


class MyClient(discord.Client):

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # only respond to ourselves
        if message.author != self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')


client = MyClient()
client.run('token')
