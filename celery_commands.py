from config import bot
from command_utils import CommandGenerator


# commands = {
#         '33' : 'https://www.twitch.tv/suspectcelery/clip/YummyCooperativeDotterelYouWHY',
#         '99' : 'https://www.twitch.tv/suspectcelery/clip/SmoothIgnorantNarwhalJonCarnage'
#         }

# # use command generator to build commands
# for cmd, response in commands.items():
#     CommandGenerator(cmd, response)

# @bot.command(name='activision')
# async def activision(ctx):
#     await ctx.send("Celery's activision is suspectcelery#3978683")

# @bot.command(name='average')
# async def average(ctx):
#     await ctx.send("Here at Suspect Celery's streams we provide below average gameplay and above average memes, so sit back and enjoy")

@bot.command(name='cel')
async def cel(ctx):
    await ctx.send("suspec19Bff Celery is the best! suspec19Bff")

