""" command utilities """

from config import bot

class CommandGenerator:
    'Generates commands based on key-value pairs in dict object'

    commands = list()  # listyboi

    def __init__(self, name, response):
        # add the command to the list
        CommandGenerator.commands.append(name)

        # generate the bot.command
        @bot.command(name=name)
        async def call_and_response(ctx):
            await ctx.send(response)


# safely print comma seperated lists that could be messages over 500 characters
async def safe_list_print(ctx, message):
    messages = []

    split = message.split(',')
    temp = ''
    last_name = ''
    while split:
        while len(temp) <= 500 and split:
            temp += split.pop(0) + ','

        if len(temp) >= 500:
            temp, last_name = temp[:-1].rsplit(',', 1)

        messages.append(temp + ',')
        temp = last_name + ','

    # The last message will have two extra commas at the end we need to strip
    messages[len(messages)-1] = messages[len(messages)-1][:-2]
    for message in messages:
        await ctx.send(message)

# test_queue_message = "The queue is open. You can join with !join. ['blurg000000', 'blurg1', 'blurg2', 'blurg3', 'blurg4', 'blurg5', 'blurg6', 'blurg7', 'blurg8', 'blurg9', 'blurg10', 'blurg11', 'blurg12', 'blurg13', 'blurg14', 'blurg15', 'blurg16', 'blurg17', 'blurg18', 'blurg19', 'blurg20', 'blurg21', 'blurg22', 'blurg23', 'blurg24', 'blurg25', 'blurg26', 'blurg27', 'blurg28', 'blurg29', 'blurg30', 'blurg31', 'blurg32', 'blurg33', 'blurg34', 'blurg35', 'blurg36', 'blurg37', 'blurg38', 'blurg39', 'blurg40', 'blurg41', 'blurg42', 'blurg43', 'blurg44', 'blurg45', 'blurg46', 'blurg47', 'blurg48', 'blurg49', 'blurg50', 'blurg51', 'blurg52', 'blurg53', 'blurg54', 'blurg55', 'blurg56', 'blurg57', 'blurg58', 'blurg59', 'blurg60', 'blurg61', 'blurg62', 'blurg63', 'blurg64', 'blurg65', 'blurg66', 'blurg67', 'blurg68', 'blurg69', 'blurg70', 'blurg71', 'blurg72', 'blurg73', 'blurg74', 'blurg75', 'blurg76', 'blurg77', 'blurg78', 'blurg79', 'blurg80', 'blurg81', 'blurg82', 'blurg83', 'blurg84', 'blurg85', 'blurg86', 'blurg87', 'blurg88', 'blurg89', 'blurg90', 'blurg91', 'blurg92', 'blurg93', 'blurg94', 'blurg95', 'blurg96', 'blurg97', 'blurg98', 'blurg99', 'blurg100', 'blurg101', 'blurg102', 'blurg103', 'blurg104', 'blurg105', 'blurg106', 'blurg107', 'blurg108', 'blurg109', 'blurg110', 'blurg111', 'blurg112', 'blurg113', 'blurg114', 'blurg115', 'blurg116', 'blurg117', 'blurg118', 'blurg119', 'blurg120', 'blurg121', 'blurg122', 'blurg123', 'blurg124', 'blurg125', 'blurg126', 'blurg127', 'blurg128', 'blurg129', 'blurg130', 'blurg131', 'blurg132', 'blurg133', 'blurg134', 'blurg135', 'blurg136', 'blurg137', 'blurg138', 'blurg139', 'blurg140', 'blurg141', 'blurg142', 'blurg143']"

# test_queue_message_2 = "The queue is open. You can join with !join. ['blurg000000', 'blurg1']"

# @bot.command(name='printy')
# async def printy(ctx):
#     # messages = safe_list_print(test_queue_message_2)
#     await safe_list_print(ctx, test_queue_message)

