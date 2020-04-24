# teaja_bot

>**This is a fork of https://github.com/NinjaBunny9000/barebones-twitch-bot with a few snippits taken from https://github.com/NinjaBunny9000/DeepThonk**
><br>
>**Big thanks to NinjaBunny9000 for building the base.**

This is a basic twitch chatbot written in python. Noteable features include a joke command and a series of queue commands for playing with viewers.

## Getting Started

Should be quick & easy to get up and running but, ofc, if you ever have questions about the specifics, please feel free to ask me.

### Prerequisites
- [Python 3.6](https://www.python.org/downloads/release/python-368/)
- PIPENV -> `python -m pip install pipenv`
- oauth token & client-id for a Twitch account for your bot

### Installing
1. Clone the repo, unzip it somewhere
2. Open up a console window and navigate to the directory you unzipped it in
3. Install requirements with `pipenv install`
4. Copy & rename `.env-example` to `.env`
5. Pop in all your secrets into the respective areas in `.env`
6. Back to the console, `pipenv run python bot.py` to start the bot
7. Type `!test` in the chatroom to test the bot's working

**You just installed a basic chat bot for Twitch!** Have fun expanding the bot with more commands!! :D

## Bot Interaction
Once the bot is connected to a chatroom you can use the command !command to make the bot print out a list of it's available commands.

You can add commands with the following syntax:

```python
@bot.command(name='likethis', aliases=['this'])
async def likethis(ctx):
    await ctx.send(f'Asuh, @{ctx.author.name}!')
```

Test is out with `!likethis` in chat! :D

## Events

There are 2 events that are used in the code right now.. `on_ready` and `on_event`.

### on_ready
This executes when the bot comes online, and will print out to the console. 
```python
@bot.event
async def event_ready():
    print(f'Ready | {bot.nick}')
```

### event_message
This function executes once per event (or message) sent. You can make it handle input from chat that *aren't* necesarily commands, and fun stuff like that.

```python
@bot.event
async def event_message(message):
    print(message.content)
    await bot.handle_commands(message)
```

You can find more info in [TwitchIO's official documentation](https://twitchio.readthedocs.io/en/rewrite/twitchio.html).


### Contributors & Licenses

[NinjaBunny9000](https://github.com/NinjaBunny9000) - Author of forked repo

[thomas-j-sell](https://github.com/thomas-j-sell) - Author of teaja_bot

