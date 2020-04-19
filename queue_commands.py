""" Commands to create and admin queues """

from config import bot

# I know globals are kind of evil, but I don't see another way to share these with async functions just yet
is_open = False
player_queue = []
players_that_queued = []

#TODO add command to let mods remove players from the queue
@bot.command(name='queue', aliases=['q'])
async def queue(ctx):
    'Queue commands. Open/close, pop, print'
    words = ctx.content.split()
    if len(words) > 1:
        sub_command = words[1].lower()

        if sub_command == 'open' or sub_command == 'start':
            if ctx.author.is_mod:
                globals()['is_open'] = True
                await ctx.send("The queue is now open. You can join with !join.")
            else:
                await ctx.send(f"Sorry {ctx.author.name} only mods can do that.")

        elif sub_command == 'close' or sub_command == 'stop':
            if ctx.author.is_mod:
                globals()['is_open'] = False
                await ctx.send("The queue is now closed.")
            else:
                await ctx.send(f"Sorry {ctx.author.name} only mods can do that.")

        elif sub_command == 'next' or sub_command == 'pop':
            if ctx.author.is_mod:
                next_up = globals()['player_queue'].pop(0)
                print(f"{next_up} has been popped from the queue")
                await ctx.send(f"{next_up} is up next.")
            else:
                await ctx.send(f"Sorry {ctx.author.name} only mods can do that.")

    else: # print queue to chat
        if globals()['is_open']:
            queue_tip = 'The queue is open. You can join with !join.'
        else:
            queue_tip = 'The queue is closed.'

        if globals()['player_queue']:
            await ctx.send(f"{globals()['player_queue']} {queue_tip}")
        else:
            await ctx.send(f"The queue is currently empty. {queue_tip}")


@bot.command(name='join')
async def join(ctx):
    print(f"is_open = {is_open}")
    if is_open:
        if ctx.author.name in globals()['player_queue']:
            await ctx.send(f"{ctx.author.name} you're already in the queue.")
        elif ctx.author.name in globals()['players_that_queued']:
            await ctx.send(f"{ctx.author.name} you have already queued today.")
        else:
            globals()['player_queue'].append(ctx.author.name)
            globals()['players_that_queued'].append(ctx.author.name)
            print(f"{ctx.author.name} has been added to the queue")
            await ctx.send(f"{ctx.author.name} you've been added to the queue.")
    else:
        await ctx.send(f"Sorry {ctx.author.name} the queue is closed.")

