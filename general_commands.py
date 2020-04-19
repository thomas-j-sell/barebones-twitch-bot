from config import bot

@bot.command(name='blurg')
async def blurg(ctx):
    await ctx.send('blurg')

