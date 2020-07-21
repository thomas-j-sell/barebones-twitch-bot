""" Commands to create and admin queues """

from config import bot
# User: longitude01, Tags: {'badge-info': 'subscriber/3', 'badges': 'vip/1,subscriber/3,sub-gifter/1', 'color': '#B05E81', 'display-name': 'Longitude01', 'emotes': '', 'flags': '', 'id': '81ada176-3143-4cf9-a7ef-0e01f75e3917', 'mod': 0, 'room-id': 439644785, 'subscriber': 1, 'tmi-sent-ts': 1587517847633, 'turbo': 0, 'user-id': 432158063, 'user-type': ''}

# if user.is_sub || 'vip' in user.badges

# I know globals are kind of evil, but I don't see another way to share these with async functions just yet
queue_is_open = False
player_queue = []
players_that_queued = {}
allow_requeue = False

#TODO add command to let mods remove players from the queue
@bot.command(name='queue', aliases=['q'])
async def queue(ctx):
    'Queue commands. Open/start, close/stop, next/pop, rules'
    words = ctx.content.split()
    if len(words) > 1:
        sub_command = words[1].lower()

        if sub_command == 'open' or sub_command == 'start':
            if ctx.author.is_mod:
                globals()['queue_is_open'] = True
                await ctx.send("The queue is now open. You can join with !join.")
            else:
                await ctx.send(f"Sorry {ctx.author.name} only mods can do that.")

        elif sub_command == 'close' or sub_command == 'stop':
            if ctx.author.is_mod:
                globals()['queue_is_open'] = False
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

        elif sub_command == 'rules':
            await ctx.send("1. This is a FIFO queue (first in first out), so you will play in the order you join. We can't accomodate requests to rearrange or manipulate the queue. 2. You need to be in the stream when you're called to be able to play. If you're not here, you will miss out. 3. Have fun!")

    else: # print queue to chat
        if globals()['queue_is_open']:
            queue_tip = 'The queue is open. You can join with !join.'
        else:
            queue_tip = 'The queue is closed.'

        if globals()['player_queue']:
            print(globals()['player_queue'])
            await ctx.send(f"{globals()['player_queue']} {queue_tip}")
        else:
            print(globals()['player_queue'])
            await ctx.send(f"The queue is currently empty. {queue_tip}")


@bot.command(name='join')
async def join(ctx):
    user = ctx.author
    if globals()['queue_is_open']:
        if user.name in globals()['player_queue']:
            await ctx.send(f"{user.name} you are already in the queue.")
        elif user.name in globals()['players_that_queued']:
            if allow_requeue:
                if(user.is_subscriber or 'vip' in user.badges) and globals()['players_that_queued'][user.name] < 2 :
                    globals()['player_queue'].append(user.name)
                    globals()['players_that_queued'][user.name] += 1
                    print(f"{user.name} has been added to the queue")
                    await ctx.send(f"{user.name} you have been added to the queue again.")
                else:
                    await ctx.send(f"{user.name} you have already joined this queue as many times as you can.")
            else:
                await ctx.send(f"{user.name} you have already joined this queue. You cannot join again.")
        else:
            globals()['player_queue'].append(user.name)
            globals()['players_that_queued'][user.name] = 1
            print(f"{user.name} has been added to the queue")
            await ctx.send(f"{user.name} you've been added to the queue.")
    else:
        await ctx.send(f"Sorry {user.name} the queue is closed.")



