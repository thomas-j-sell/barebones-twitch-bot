""" Commands to print out shower thoughts to chat. """

from config import bot
import random

@bot.command(name='showerthought', aliases=['showerthoughts', 'st'])
async def showerthought(ctx):
    words = ctx.content.split()
    if len(words) > 1:
        if words[1].isnumeric():
            index = int(words[1])
            if 0 <= index < len(thoughts):
                await ctx.send(thoughts[index])
            else:
                await ctx.send(f"Sorry {ctx.author.name}, that number is out of the range of my shower thoughts list.")
        elif words[1].lower() == 'size' or words[1].lower() == 'length':
            await ctx.send(f"There are {len(thoughts)} thoughts in my list. So valid joke indexes are 0-{len(thoughts)-1}.")
    else:
        await ctx.send(random.choice(thoughts))

# the dad-a-base
thoughts = [
        'No matter how many lasagnas you stack on top of one another, you still only have 1 lasagna.',
        'CPR is just the human version of "blowing on a game cardtridge".',
        'Aliens invaded the moon on July 20, 1969.',
        'Why is it that we park on a driveway, but drive on a parkway?',
        'Why are pizzas round, but we cut them into triangles and put them in a square box?',
        "Why is it that when we send something by boat it's called cargo, but when we send it by car it's called a shipment?"
 ]
