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
            await ctx.send(f"There are {len(thoughts)} thoughts in my list. So valid thought indexes are 0-{len(thoughts)-1}.")
    else:
        await ctx.send(random.choice(thoughts))

# * scratches chin * hmmmmmmmm
thoughts = [
        'No matter how many lasagnas you stack on top of one another, you still only have 1 lasagna.',
        'CPR is just the human version of "blowing on a game cardtridge".',
        'Aliens invaded the moon on July 20, 1969.',
        'Why is it that we park on a driveway, but drive on a parkway?',
        'Why are pizzas round, but we cut them into triangles and put them in a square box?',
        "Why is it that when we send something by boat it's called cargo, but when we send it by car it's called a shipment?",
        "If a house has solar panels and AC, the sun is simultaneously heating and cooling it.",
        "If it hasn't been cold before then technically it can only be fridgerated.",
        "How did a fool and his money get together in the first place?",
        "What monster put the cat in a bag to begin with?",
        "Why do we call it a double U when it's clearly a double V?",
        'Why does "fridge" have a D in it but "refrigerator" does not?',
        "When Sweden plays against Denmark in sports, the scoreboard will say Swe-Den and the unused letters will be Den-Mark.",
        'Why do they make "birthday cake" flavored things when birthday cakes can be any flavor?',
        "Onion rings are just vegatable donuts.",
        "Your stomach thinks all potatoes are mashed.",
        "Lobsters are mermaids to scorpions.",
        "Cookie dough is the sushi of desserts.",
        "If tomatoes are fruits then isn't ketchup a jelly?",
        "Two wrongs don't make a right, but three lefts do.",
        "Lasagna is just spaghetti flavored cake.",
        "It's weird that we cook bacon and bake cookies.",
        "Why is it that fingers have tips yet we can't tip-finger, but toes don't have tips and we can tip-toe?",
        'The phrases "I\'m down" and "I\'m up" mean the same thing',
        "Aladdin's magic carpet is actually a rug.",
        "Technically if you don't cut a cake and just eat the whole thing with a fork you only had once piece.",
        "If your shirt isn't tucked into your pants, are your pants tucked into your shirt?",
        "If you're invisbile and you close your eyes, can you see through your eyelids?",
        "A firetruck is actually a watertruck.",
        "If you pamper a cow, would you get spoiled milk?",
        "If you keep traveling north long enough you will eventually start traveling south, but you can travel east or west forever.",
        'Are oranges named "oranges" because oranges are orange or is orange named "orange" because oranges are orange?',
        "The youngest picture of you, is also the oldest picture of you.",
        "The only part of your reflection you can lick is your tongue.",
        'The word "bed" is shaped like a bed.',
        'Slim Jims are hot dog raisins.',
        'Saying "everyone on earth" excludes about 6 people.',
        'Why do people say "tuna fish" but not "chicken bird" or "pork hog?"',
        'If you buy a bigger bed you have more bed room, but less bedroom.'
        ]
