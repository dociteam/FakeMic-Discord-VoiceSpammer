# FakeMic - Discord VoiceSpammer
# Author: DociTeam - https://github.com/DociTeam
# December 30rd, 2021
# Copyright 2021, Doctor


import discord
from discord.ext import commands
from asyncio import sleep

#Your Token
TOKEN_AUTH = "Your Token"
#Your Prefix
client = commands.Bot(command_prefix = 'fm!', self_bot=True)
#Channel ID You Want To Join
VOICE_CHANNEL_ID = 925437448387981342


@client.event
async def on_ready():
    voice_channel = client.get_channel(VOICE_CHANNEL_ID)
    vc = await voice_channel.connect()
    print("Joined Voice!")
    while True: #You Can Delete While Loop
        vc.play(discord.FFmpegPCMAudio(source="salam-gl.mp3"))
        while vc.is_playing():
            await sleep(.1)

@client.command()
async def mute(ctx):
    await ctx.message.delete()
    voice_channel = client.get_channel(VOICE_CHANNEL_ID)
    await ctx.guild.change_voice_state(channel=voice_channel, self_mute=True)

@client.command()
async def unmute(ctx):
    await ctx.message.delete()
    voice_channel = client.get_channel(VOICE_CHANNEL_ID)
    await ctx.guild.change_voice_state(channel=voice_channel, self_mute=False)

@client.command()
async def deafen(ctx):
    await ctx.message.delete()
    voice_channel = client.get_channel(VOICE_CHANNEL_ID)
    await ctx.guild.change_voice_state(channel=voice_channel,self_deaf=True)

@client.command()
async def undeafen(ctx):
    await ctx.message.delete()
    voice_channel = client.get_channel(VOICE_CHANNEL_ID)
    await ctx.guild.change_voice_state(channel=voice_channel,self_deaf=False)


client.run(TOKEN_AUTH, bot=False)
