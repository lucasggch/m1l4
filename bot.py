import discord
import random
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def pasw(ctx):
    await ctx.send(gen_pass(10))

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

# 👇 NUEVO COMANDO COIN
@bot.command()
async def coin(ctx):
    resultado = random.choice(["cara", "cruz"])
    await ctx.send(f'🪙 Salió **{resultado}**!')

@bot.group()
async def cool(ctx):
    """Says if a user is cool."""
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} no es cool')

@cool.command(name='bot')
async def _bot(ctx):
    await ctx.send('si,el bot es cool.')

@cool.command(name='lucas')
async def _lucas(ctx):
    await ctx.send('si,lucas es cool.')

@cool.command(name='victorio')
async def _victorio(ctx):
    await ctx.send('si,victorio es cool.')

@cool.command(name='bauti')
async def _bauti(ctx):
    await ctx.send('si,bauti es cool.')

@cool.command(name='cubanito')
async def _cubanito(ctx):
    await ctx.send('si,cubanito es cool.')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Dice cuándo un usuario se unió."""
    if member.joined_at is None:
        await ctx.send(f'{member} no tiene fecha de ingreso.')
    else:
        await ctx.send(f'{member} se unió {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def cool2(ctx, *, palabra: str):
    resultado = random.choice([True, False])

    if resultado:
        await ctx.send(f"Sí, {palabra} es cool 😎")
    else:
        await ctx.send(f"No, {palabra} no es cool 😢")

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)



bot.run("TOKEN")
