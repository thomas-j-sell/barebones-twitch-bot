from config import bot
import random

@bot.command(name='source')
async def source(ctx):
    await ctx.send('I was created by dredgen_teaja. You can see the code that makes me work at https://github.com/thomas-j-sell/teaja-bot')


@bot.command(name='blurg')
async def blurg(ctx):
    await ctx.send('blurg')


# picks a random lurk message to give lurker
@bot.command(name='lurk')
async def lurk(ctx):
    lurk_messages = [
            "Lurk, Lurk.",
            "Live, laugh, Lurk.",
            "Can you feel the lurk tonight?",
            "It's the circle of lurk.",
            "Lurkin at the car wash.",
            "Lurking hard or hardly lurking.",
            "Lurk of the Irish.",
            "Livin la vida Lurk-a.",
            "I'm pretty sure there's more to life than being really, really ridiculously good lurking.",
            "We're up all night to get lurk-y.",
            "Lurk-en... Wait for it, and I hope you're not lurk-tose intolerant cause the second half of that word is... dary.",
            "The cake is a lurk.",
            "They see me playin', they lurkin'.",
            "What is lurk? Baby don't chat me, don't chat me, no more.",
            "What's lurkin? Don't mind me just watchin."
            ]
    await ctx.send(f"{random.choice(lurk_messages)}")


@bot.command(name='thicc')
async def thicc(ctx):
    await ctx.send("Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibu")
