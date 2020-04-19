from config import bot
from command_utils import CommandGenerator

##################
# gaming accounts
##################
@bot.command(name='socials', aliases=['social'])
async def socials(ctx):
    await ctx.send("Hey! Listen! If you want to keep up with me on social media you can follow on these platforms: twitter.com/teaja instagram.com/dredgen_teaja")

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

