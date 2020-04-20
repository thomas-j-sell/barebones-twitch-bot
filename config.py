import os, sys
from twitchio.ext import commands


# parse arguments to decide which bot to boot and where to connect it
# selects different sets of environment varialbes and commands
if(len(sys.argv) > 1):
    if(sys.argv[1] == 'teaja'):
        print('booting teaja_bot')
        env_prefix = 'TEAJA_'
    elif(sys.argv[1] == 'celery'):
        print('booting celery_bot')
        env_prefix = 'CELERY_'
    elif(sys.argv[1] == 'soda'):
        print('booting soda_bot')
        env_prefix = 'SODA_'
    else:
        print(f"{sys.argv[1]} is not a valid bot. Booting teaja_bot")

# set up the bot
bot = commands.Bot(
    irc_token=os.environ[f"{env_prefix}TMI_TOKEN"],
    client_id=os.environ[f"{env_prefix}CLIENT_ID"],
    nick=os.environ[f"{env_prefix}BOT_NICK"],
    prefix=os.environ[f"{env_prefix}BOT_PREFIX"],
    initial_channels=[os.environ[f"{env_prefix}CHANNEL"]]
)
