from config import bot
from command_utils import CommandGenerator
import random


@bot.command(name='socials', aliases=['social'])
async def socials(ctx):
    await ctx.send("Hey! Listen! If you want to keep up with me on social media you can follow on these platforms: twitter.com/teaja instagram.com/dredgen_teaja")


##################
# gaming accounts
##################
@bot.command(name='accounts', aliases=['account'])
async def accounts(ctx):
    await ctx.send('PSN: teaja, Epic: dredgen_teaja, Activision: teaja#7667376, riot: TBD')

gaming_account_commands = {
        'psn' : 'PSN: teaja',
        'epic' : 'Epic: dredgen_teaja',
        'activision' : 'Activision: teaja7667376'
        }

# use command generator to build commands
for cmd, response in gaming_account_commands.items():
    CommandGenerator(cmd, response)


########################
# team pyramid commands
########################
@bot.command(name='pyramid', aliases=['pyrmd'])
async def pyramid(ctx):
    await ctx.send("You can connect with and support Team Pyramid by: joining the discord https://discord.gg/FwMhsgp -- using the Epic creator code: pyrmd -- buying merch: https://pyrmd-design.myshopify.com/ -- or most importanly, just hanging out in stream.")

team_commands = {
        'cc' : 'You can support Team Pyramid by using the Epic creator code: "pyrmd"',
        'discord' : 'Come hang out with Teaja and the other members of Team Pyramid in our Discord! https://discord.gg/FwMhsgp',
        'merch' : 'Check out the Team Pyramid merch! https://pyrmd-design.myshopify.com/'
        }

# use command generator to build commands
for cmd, response in team_commands.items():
    CommandGenerator(cmd, response)

################
# gear commands
################
gear_commands = {
        'controller' : 'Scuf Impact: https://scufgaming.com/playstation-impact-controller',
        'headphones' : 'HyperX Cloud II: https://www.amazon.com/HyperX-Cloud-Gaming-Headset-KHX-HSCP-GM/dp/B00SAYCVTQ'
        }

# use command generator to build commands
for cmd, response in gear_commands.items():
    CommandGenerator(cmd, response)


@bot.command(name='brb')
async def brb(ctx):
    await ctx.send("I have to step away for a moment, but I'll be right back. Would you kindly stick around?")

@bot.command(name='back')
async def back(ctx):
    await ctx.send("I'm back. Stay awhile and listen.")


@bot.command(name='lurk')
async def lurk(ctx):
    lurk_messages = [
            "Lurk, Lurk, Lurk.",
            "Live, laugh, Lurk.",
            "Can you feel the lurk tonight?",
            "It's the circle of lurk.",
            "Lurkin at the car wash."
            ]
    await ctx.send(f"{random.choice(lurk_messages)}")


