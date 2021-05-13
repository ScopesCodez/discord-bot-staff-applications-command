"""
TITLE : Staff application command
AUTHOR : Scoopy#6969 (dc) | ScopesCodez (gh)
DESCRIPTION : Advanced discord bot staff applications command

Feel free to report any errors or issues!
"""

import discord  # import discord library
from discord.ext import commands  # import commands class from the discord package

# you can change this, just make sure you've got member intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)  # defining our client


@bot.event
async def on_ready():
    # this will print "<your bot name> is online!" once your bot has started
    print(f"{bot.user} is online!")


@bot.command()
async def apply(ctx):
    # we will make a list of questions here and you may add as more as you like
    questions = ["Question 1", "Question 2", "Question 3"]

    answers = []  # this will be an empty list of answers because it will be filled with the user's responses

    for question in questions:  # this is a for loop that will do the same code below for every question in our questions list
        # this will get the order of the question in the questions list
        question_order = questions.index(question)
        # since the index starts with the number 0, this will add 1 to the index number
        question_number = question_order + 1
        question_msg = await ctx.author.send(f"**Q{question_number} : {question}**\nA : Type your answer...")

        def check(msg):  # this is a check that we will use in the `wait_for` to make sure the user responding is the command author and the response is in the bot's DMs
            return msg.author == ctx.author and msg.guild == None

        # this will wait for a response from the command author
        answer = await bot.wait_for('message', check=check)
        # this will edit the message of the question to make sure the response is recorded
        await question_msg.edit(f"**Q : {question}**\nA : {answer.content}")
        # this will append the answer in the answers list with the answer's number
        answers.append(f"A{question_number} : {answer.content}")

    # get the channel that the applications should be sent to
    apps_logs_channel = bot.get_channel(1234)

    embed = discord.Embed(color=discord.Color.purple()
                          )  # creating Embed instance
    embed.set_author(
        name=f"Staff application by {ctx.author}", icon_url=ctx.author.avatar_url)

    for question in questions:  # this is a for loop that will add a field to the embed for every question
        question_order = questions.index(question)
        question_number = question_order + 1

        # now we will need to detect the question's answer

        for answer in answers:  # this will check for the answer in all the answers
            # as we saved the answer "A{question_number} : {answer.content}"
            if answer.startswith(f"A{question_number}"):
                a = answer

        # this will add a field to the embed
        embed.add_field(name=question, value=a)

    await apps_logs_channel.send(embed=embed)
    await ctx.author.send("Your application has been submitted!")

bot.run("your token here")
