
import discord
import os
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == 'regras':
            await message.channel.send(f'Zzzzzzummmmmmmm, {message.author.name}, o servidor tem Zzzzzzummmmmmmm apenas uma regra: {os.linesep}  Não Zzzzzzummmmmmmm desrespeitar ninguém {os.linesep}  De resto, seja livre neste pequeno Zzzzzzummmmmmmm espaço.')
        elif message.content == 'nivel':
            await message.author.send(' Nível de Zzzzzzummmmmmmm intimidade: 1 ')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention}, lindo (a) gostoso (a) acabou de entrar em {guild.name}'
            await guild.system_channel.send(mensagem)

client =  MyClient(intents=intents)
client.run('my token here')
