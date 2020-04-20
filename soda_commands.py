from config import bot
from command_utils import CommandGenerator

@bot.command(name='soda')
async def soda(ctx):
    await ctx.send('Best hair on twitch?')


