""" command utilities """

from config import bot

class CommandGenerator:
    'Generates commands based on key-value pairs in dict object in content.py'

    commands = list()  # listyboi

    def __init__(self, name, response):
        # add the command to the list
        CommandGenerator.commands.append(name)

        # generate the bot.command
        @bot.command(name=name)
        async def call_and_response(ctx):
            await ctx.send(response)
