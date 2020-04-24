from config import bot

@bot.command(name='source')
async def source(ctx):
    await ctx.send('I was created by dredgen_teaja. You can see the code that makes me work at https://github.com/thomas-j-sell/teaja-bot')


@bot.command(name='blurg')
async def blurg(ctx):
    await ctx.send('blurg')

