""" bot.py Main file for teaja_bot. Puts everything together and sets up main loop. """

import os
from config import bot, env_prefix

import general_commands
import joke_commands
import shower_thoughts_commands
import queue_commands
import giveaway_commands


# bot specific commands
if(env_prefix == 'TEAJA_'):
    import teaja_commands
elif(env_prefix == 'CELERY_'):
    import celery_commands
elif(env_prefix == 'SODA_'):
    import soda_commands
    queue_commands.allow_requeue = True


# temporary introduction command to introduce viewers to bot
@bot.command(name='intro')
async def intro(ctx):
    bot_name = os.environ[f"{env_prefix}BOT_NICK"]
    await ctx.send(f"Hello I am {bot_name}. I am new and still under contruction. To see what I can currently do type !commands.")


# add the list of available commands, all commands need to be imported before this
@bot.command(name='commands')
async def commands(ctx):
    'Outputs a list of all configured commands'
    command_list = bot.commands.keys()
    command_list_str =''
    for key in command_list:
        command_list_str += f"!{key}, "

    # remove the last comma and space
    command_list_str = command_list_str[:-2]

    await ctx.send(f"Available commands: {command_list_str}")


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    nickname = os.environ[f"{env_prefix}BOT_NICK"]
    print(f"{nickname} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ[f"{env_prefix}CHANNEL"], f"/me Hello. I am {nickname}. Type !commands to see what I can do.")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # basic logging to terminal, just lets you see that the bot is working
    print(f"User: {ctx.author.name}, badges: {ctx.author.badges}")

    # just make content lowercase so that upper case commands will work
    ctx.content = ctx.content.lower()

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ[f"{env_prefix}BOT_NICK"].lower():
        return

    # respond to a variety of hello, hey, hi, sup, etc.
    hellos = ['allo', 'hello', 'helloo', 'henlo', 'hey', 'heyhey', 'hai', 'haii', 'hi', 'hii', 'hiii', 'hiiii', 'hiiiii', 'sup', 'sah', 'whatsup', 'elo', 'ello', 'hawwo', 'hewo', 'howdy', 'yo', 'yoyo', 'yoyoyo', 'yoo', 'yooo', 'yoooo', 'yooooo', 'yoooooo', 'wuddup', 'wuddupwuddup', 'wuddupwuddupwuddupa', 'whatup', 'whatupwhatup', 'suspec19bff', 'suspec19bffsuspec19bff', 'suspec19bffsuspec19bffsuspec19bff', 'oi', 'oi oi']
    # remove special characters and convert to lower case to compare to list
    message = ''.join(filter(str.isalnum, ctx.content))
    # print(message)

    if message in hellos:
        await ctx.channel.send(f"Hello @{ctx.author.name}! Welcome to the stream!")


    # Parrotings
    # if someone sends __ parrot back __
    if ctx.content == '^':
        await ctx.channel.send('^')

    # TODO add a cooldown so bot only adds one f to a particular fs-in-chat event
    if ctx.content == 'f':
        await ctx.channel.send('f')


    # process the command
    await bot.handle_commands(ctx)


if __name__ == "__main__":
    bot.run()
