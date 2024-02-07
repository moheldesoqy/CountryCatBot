import discord
from discord.ext import commands
import os
from discord import app_commands, Intents, Client, Interaction
import inspect
import random
import discord.opus
import asyncio
import yt_dlp as youtube_dl
import requests
import time
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents)
voice_clients = {}
yt_dl_opts = {"format": "bestaudio/best"}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {"options": "-vn"}

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.tree.command(
    name="hello",
    description="Retrieves the live doppler radar for a station, if none given, gets CONUS.",
)

async def _space(ctx: discord.interactions.Interaction):
    await ctx.response.send_message("hello")

images_directory = "images"
music_directory = "music"

images = [
    os.path.join(images_directory, file)
    for file in os.listdir(images_directory)
    if file.endswith((".png", ".jpg", ".jpeg", ".gif"))
]
music = [
    os.path.join(music_directory, file)
    for file in os.listdir(music_directory)
    if file.endswith((".mp3"))
]

yeehaw_phrases = [
    "Yeehaw!",
    "Yippee ki-yay!",
    "Giddy up cowboy!",
    "Howdy partner!",
    "Saddle up, we've got a yeehaw coming!",
    "Hold on to your hats, it's yeehaw time!",
    "Yeehaw, y'all!",
    "Get ready for a rootin' tootin' good time!",
    "Cowboy up, it's yeehaw o'clock!",
    "Y'all ready to ride the yeehaw express?",
    "Buckle up, it's gonna be a wild yeehaw ride!",
    "Yeehawing into the sunset!",
    "Round 'em up, it's yeehaw season!",
    "Yeehaw squared!",
    "Double the yippee ki-yay!",
    "Giddy up for round two, cowboy!",
    "Howdy again, partner!",
    "Saddle up, we've got another yeehaw coming!",
    "Hold on tight, more yeehaw is on the way!",
    "Yeehaw encore, y'all!",
    "Another rootin' tootin' good time!",
    "Double down on the yeehaw fun!",
    "Ride the yeehaw express one more time!",
    "Buckle up, the wild yeehaw ride continues!",
    "Yeehawing under the moonlight!",
    "Round 'em up for more yeehaw season!",
    "This town ain't big enough for the both of us..",
    "Yeehaw squared again!",
    "Double the yippee ki-yay again!",
    "Giddy up for round three, cowboy",
    "Howdy again, partner!",
    "Saddle up, we've got another yeehaw coming!",
]

@client.command()
async def stop(ctx):
    # Check if the bot is in a voice channel
    if ctx.voice_client:
        # Stop playing audio
        ctx.voice_client.stop()
        # Disconnect from the voice channel
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("I'm not currently in a voice channel.")

@client.command()
async def stopdance(ctx):
    global dance_loop_flag
    dance_loop_flag = False

@client.command()
async def dance(ctx):
    dances = ["images/image10.png", "images/10image.png"]
    counter = 0

    for file_path in dances:
        if not os.path.exists(file_path):
            await ctx.send(f"File not found: {file_path}")
            return

    global dance_loop_flag
    dance_loop_flag = True

    while dance_loop_flag:
        file_path = dances[counter]
        file = discord.File(file_path)
        await ctx.send(file=file)

        counter = (counter + 1) % len(dances)

        await asyncio.sleep(0.3)

@client.command()
async def yeehaw(ctx):
    file_path = random.choice(images)
    file = discord.File(file_path)
    await ctx.send(file=file)
    music_path = random.choice(music)

    await ctx.send(random.choice(yeehaw_phrases))

    voice_channel = ctx.author.voice.channel
    voice_client = await voice_channel.connect()
    voice_clients[voice_client.guild.id] = voice_client

    print("________________________________________________________")
    print(f"Command invoked by: {ctx.author.name} ({ctx.author.id})")
    print("________________________________________________________")
    print(f"Now playing music: {music_path}")

    voice_client.play(discord.FFmpegPCMAudio(source=music_path))

    while voice_client.is_playing():
        await asyncio.sleep(1)

    await voice_client.disconnect()

try:
    client.run(
        "TOKEN_HERE"
    )
except Exception as error:
    print(error)
