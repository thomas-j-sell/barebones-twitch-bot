""" Commands to create and admin giveaways """

from config import bot

import random

giveaway_is_open = False
giveaway_pool = []
current_giveaway = ''

@bot.command(name='giveaway', aliases=['g'])
async def giveaway(ctx):
    'Giveaway commands. Open/start, close/stop, pick/winner, clear'
    words = ctx.content.split()
    if len(words) > 1:
        sub_command = words[1].lower()

        if sub_command == 'open' or sub_command == 'start':
            if ctx.author.is_mod:
                # everything after 'open/start' with be the giveaway message
                globals()['current_giveaway'] = " ".join(words[2:])
                globals()['giveaway_is_open'] = True
                await ctx.send(f"A giveaway for {globals()['current_giveaway']} is open")
            else:
                await ctx.send(f"Sorry {ctx.author.name} only mods can do that.")

        elif sub_command == 'close' or sub_command == 'stop':
            if ctx.author.is_mod:
                if globals()['giveaway_is_open']:
                    globals()['giveaway_is_open'] = False
                    await ctx.send("The giveaway has been closed.")
                else:
                    await ctx.send("There isn't a giveaway open.")
            else:
                await ctx.send(f"Sorry {ctx.author.name} only mods can do that.")

        elif sub_command == 'pick' or sub_command == 'winner':
            if ctx.author.is_mod:
                winner = random.choice(globals()['giveaway_pool'])
                # remove the winner from the pool to allow for multple winners to be drawn
                globals()['giveaway_pool'].remove(winner)
                await ctx.send(f"Congratulations {winner}! You've won!")
            else:
                await ctx.send(f"Sorry {ctx.author.name} only mods can do that.")

        elif sub_command == 'clear':
            if ctx.author.is_mod:
                if globals()['giveaway_pool']:
                    globals()['giveaway_pool'] = []
                    await ctx.send("The giveaway entrants have been cleared.")
                else:
                    await ctx.send("There are currently no entrants in the giveaway to clear.")
            else:
                await ctx.send(f"Sorry {ctx.author.name} only mods can do that.")

        elif sub_command == 'rules':
            await ctx.send("Anyone can enter, you don't need to be a follower or a sub. You just need to be in the stream when the winner is called.")

    else: # print queue to chat
        # TODO allow the 'join' word to be set with open command?
        if globals()['giveaway_is_open']:
            if globals()['giveaway_pool']:
                await ctx.send(f"A giveaway for {globals()['current_giveaway']} is open. You can join with !win. The following players are already entered: {globals()['giveaway_pool']}")
            else:
                await ctx.send(f"A giveaway for {globals()['current_giveaway']} is open. You can join with !win.")
        elif giveaway_pool:
            await ctx.send(f"The giveaway is closed, but the following players are entered to win: {globals()['giveaway_pool']}")
        else:
            await ctx.send(f"Sorry {ctx.author.name} there is no giveaway open.")


@bot.command(name='win')
async def win(ctx):
    user = ctx.author
    if globals()['giveaway_is_open']:
        if user.name in globals()['giveaway_pool']:
            await ctx.send(f"{user.name} you have already been entered to win.")
        else:
            globals()['giveaway_pool'].append(user.name)
            await ctx.send(f"{user.name} you have been entered to win!")
    else:
        await ctx.send(f"Sorry {user.name}, there's no giveaway to enter.")
