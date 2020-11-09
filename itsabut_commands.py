""" Commands to print out itsabuts to chat. (It's a _____ but ______: _____) """

from config import bot
import random

@bot.command(name='itsabut')
async def itsabut(ctx):
    words = ctx.content.split()
    if len(words) > 1:
        if words[1].isnumeric():
            index = int(words[1])
            if 0 <= index < len(itsabuts):
                await ctx.send(itsabuts[index])
            else:
                await ctx.send(f"Sorry {ctx.author.name}, that number is out of the range of my itsabut list.")
        elif words[1].lower() == 'size' or words[1].lower() == 'length':
            await ctx.send(f"There are {len(thoughts)} itsabuts in my list. So valid thought indexes are 0-{len(thoughts)-1}.")
    else:
        await ctx.send(random.choice(itsabuts))

itsabuts = [
   "It's a video game, but about office equipment: A-fax Legends",
   "It's a WB cartoon, but about cheating: Animani-hacks",
   "It's an internet connection, but about an anime character: Wai-fi",
   "It's an anime, but about a part of your body: Naru-toe",
   "It's an Apex legend, but also someone you're with forever: Wifeline",
   "It's a network drama, but in a popular game: \"This is sus\"",
]
