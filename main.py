import discord
import random
import os
from discord.ext import commands
from functions import classify


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')
        
@bot.command()
async def recognize(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.message.attachments: #cek attatch men
        for attachment in ctx.message.attachments: #ambil data attatchment
            await attachment.save(attachment.filename)
            name,score = classify(attachment.filename)
            await ctx.send(f"Nama: {name} dengan skor {score}")
    else:
        await ctx.send('File Unrecognized!')

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command(name='meme')
async def meme(ctx):
    memes = random.choice(os.listdir('memes'))
    with open('memes/' + memes, 'rb') as f:
        picture = discord.File(f)
    await ctx.send('Yes, the bot is memeing.',file = picture)
    
@bot.command('quotes')
async def quotes(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    quotes = ["Throw trash at trashbins","Care for Nature!!!","stop killing trees"]
    save_earth = random.choice(os.listdir('nature'))
    with open('nature/' + save_earth, 'rb') as f:
        nature = discord.File(f)
    await ctx.send(random.choice(quotes),file = nature)

bot.run("MTE2MDU3MTUyMTY4MTYwNDc0OQ.GsKYPY.fh1OB8U97D3xGJgJxWAC2Bp6T1DcUCY6REPcrc")