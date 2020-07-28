""" Commands to print out dad jokes to chat. """

from config import bot
import random

@bot.command(name='joke', aliases=['jokes'])
async def joke(ctx):
    words = ctx.content.split()
    if len(words) > 1:
        if words[1].isnumeric():
            index = int(words[1])
            if 0 <= index < len(jokes):
                await ctx.send(jokes[index])
            else:
                await ctx.send(f"Sorry {ctx.author.name}, that number is out of the range of my joke list.")
        elif words[1].lower() == 'size' or words[1].lower() == 'length':
            await ctx.send(f"There are {len(jokes)} jokes in my list. So valid joke indexes are 0-{len(jokes)-1}.")
    else:
        await ctx.send(random.choice(jokes))

# the dad-a-base
jokes = [
        "Some people think filling animals with helium is wrong… I don't judge, whatever floats your goat.",
        "So there was this pun contest…  I entered ten puns in the hopes that one might win. No pun in ten did.",
        "My professor accused me of plagiarism. His words, not mine.",
        'A neutron walked into a bar and asked “how much for a drink?”. The bartender said: "for you, no charge".',
        "Mountains aren't just funny, they're hill areas.",
        "Shipment of viagra stolen. Police searching for gang of hardened criminals.",
        "If I had to rate our solar system I'd give it one star… or 8/9.",
        "I just want a job cleaning mirrors. It's really a job I could see myself doing.",
        "I buy all my guns from a guy named T-Rex. He's a small arms dealer.",
        "Why does Snoop Dogg use an umbrella? Fo drizzle.",
        "I’m only familiar with 25 letters in the English language. I don’t know why.",
        "Sheep dog: All 30 sheep are ready. Farmer: But I only count 26. Sheep dog: Yes, I rounded them up for you",
        "What's Harry Potter's favorite way to get down a hill? Walking... JK Rolling.",
        "I have an irrational fear of speed bumps, but I'm slowly getting over it.",
        "What do you call a singing computer? A dell.",
        "I have a phobia of overly engineered buildings. It's a complex complex complex.",
        "What kind of train eats too much? A chew chew train.",
        "Dr. Frankenstein entered a body building competition and discovered he had seriously misunderstood the objective.",
        "Cigarettes are a lot like hamsters; harmless until you put one in your mouth and light it on fire.",
        "When does a joke become a dad joke?  When it's fully groan.",
        "Orion's Belt is a big waist of space. Terrible joke, only three stars.",
        "Where did Noah keep his bees? In the arc hives.",
        'A Mexican magician told an audience he would disappear on the count of 3.  "Uno, dos, poof."  He disappeared without a tres.',
        "What do you get when you drop a piano on a child? A flat minor.",
        "Why do seagulls fly over the sea? If the flew over the bay they'd be called bagels.",
        "Why do chicken coups only have 2 doors? If they had 4 they'd be chicken sedans.",
        "To the person who stole my copy of Microsoft office: I will find you, you have my word.",
        "Whiteboards: they're remarkable.",
        "How do you count cows? With a cowculator.",
        "I wanted to invest in the Egyptian tourism market. But I realized it's just a pyramid scheme.",
        "Diarrhea is hereditary. It runs in your jeans.",
        "My preferred way to deal with things is to pretend I'm the pope. It's my poping mechanism.",
        "To the guy that invented zero, thanks for nothing.",
        "Did you hear about the fire at the shoe factory? 100 soles were lost.",
        "My friend David had his ID stolen the other day. Now we just call him Dav.",
        "Did you hear about the gummy bear that was missing a leg? He lost in it nom.",
        "I dig, you dig, he dig, she dig, they dig. It's not a beautiful poem, but it's deep.",
        "The invention of the shovel was… ground breaking.",
        "6 out of 7 dwarves aren’t happy.",
        "What did the seal with the broken arm say to the shark? Don’t consume if seal is broken.",
        "How did the hammerhead do on his test? He nailed it.",
        "Where is happiness made? At the satisfactory.",
        "If towels could tell jokes they’d probably have a dry sense of humor.",
        "Imagine if the US switched from pounds to kilograms overnight. There would be mass confusion.",
        "Last night I was attacked by mimes. They did unspeakable things to me.",
        "Most people are shocked to learn how incompetent I am as an electrician.",
        "I took part in the sun tanning Olympics. I only got bronze.",
        'A horse walks into a bar. The bartender says “hey”. The horse replies “Sure”.',
        "I used to sell security alarms door to door.  If no one was home I’d just leave a brochure on the kitchen table.",
        "I’ve had amnesia for as long as I can remember.",
        "What do you call a sea creature that uses a fake name? A pseudonemone.",
        "I’ve been diagnosed with a fear of giants. Feefiphobia.",
        "I’m not fond of cheese.  You could say I’m a curd-mudgeon.",
        "I love jokes about eyes, the cornea the better.",
        "I need to cut my fingernails, they’re really getting out of hand.",
        "Just saw someone rob the Apple store.  I’m now an iWitness.",
        "Why don’t birds like asking for directions? They like to wing it.",
        "What do toes and strawberries have in common? Jam.",
        "Where do you learn to make ice cream? Sundae school.",
        "Did you hear the story about the dog who traveled 1000 miles to pick up a stick. It sounds far fetched.",
        "What do you call a bear with no teeth? A gummy bear.",
        "Did you head about the guy that got hit in the head with a soda can? He was lucky it was a soft drink.",
        "What did the mermaid wear to math class. An algae bra.",
        "How does a mansplainer drink? From a well, actually.",
        "In college my nickname was the love machine. It’s true I was really bad at tennis.",
        "My girlfriend got sick of my beekeeping hobby. She told me I had to chose between her and the bees.  I saw her face and now I’m a bee-leaver.",
        "I made a new playlist for hiking. It has music from Penuts, the Cranberries, and Eminem. I call it my trail mix.",
       "I bought some shoes from a drug dealer. I don’t know what he laced them with, but I was tripping all day.",
       "Give a man a duck, and he'll eat for a day. Teach a man to duck, and he'll never walk into a bar.",
       'Two cannibals were eating a clown. One says to the other "does this taste funny to you?"',
       'How do reavers clean their spears? They run them through the Wash.',
       "I hate it when someone has hand sanitizer and I dont. They're always rubbing it in.",
       'I store all my dad jokes in my dad-a-base.',
       'I crashed my bike into a wall today.... it was wheelie unfortunate.',
       "There are three kinds of people: those who can count and those who can't.",
       'There are two kinds of people: those who can extrapolate from incomplete data...',
       "What's the internal temperature of a tauntaun? Luke warm.",
       "A man walks into a zoo. The only animal in the entire zoo is a small dog. It's a shitzu.",
       "How do you follow Will Smith through a snowstorm? You look for fresh prints.",
       "Why don't melons get married? Because they cantaloupe",
       "When life gives you melons, you may be dyslexic.",
       "If you're addicted to seaweed you should probably sea kelp.",
       "How does the Pope send money? Pray-pal.",
       "Last night I had a dream that I was a muffler. I woke up exausted.",
       "Have you ever noticed how rarely you see DeLoreans on the road? Their owners only drive them from time to time.",
       "Not only I am a master of suspense, I am also...",
       "I can't find the controller for my TV. It's probably in a remote location.",
       "Why did the scarecrow get an award? He was outstanding in his field.",
       "The ghost of a chicken is haunting my attic. It's a poultry-geist.",
       'A Roman walks into a bar. He holds up 2 fingers and says "Five bears please.',
       "How many tickles does it take to make an octopus laugh? Ten tickles.",
       "How do you make a waterbed more bouncy? You pour in spring water.",
       "What's the quietest animal on a farm? A shhhhhheep.",
       "What do you call a chicken staring at lettuce? Chicken sees a salad.",
       "Why are french snails faster than other snails? L'ess cargo.",
       "I got fired from my job at the keyboard factory today. I wasn't putting in enough shifts"
 ]
