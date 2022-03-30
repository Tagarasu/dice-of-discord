import random
from discord.ext import commands
from discord_token import token

numbers = ["1", "2", "3", "4", "5", "6"]
bot = commands.Bot(command_prefix='/')


@bot.command()
async def d6(ctx, arg):
    if arg in numbers:
        dice = random.randint(1, 2)
        if dice == 1:
            gif = "https://giphy.com/gifs/MAwh10DSEScWAZ0q42"
            await ctx.send(gif)
            if dice == int(arg):
                await ctx.send("Вы выиграли")
            else:
                await ctx.send("Вы проиграли")
        if dice == 2:
            gif = "https://media.giphy.com/media/2DkajhbFLNadNtFucB/giphy.gif"
            await ctx.send(gif)
            if dice == int(arg):
                await ctx.send("Вы выиграли")
            else:
                await ctx.send("Вы проиграли")
        if dice == 3:
            gif = "https://media.giphy.com/media/EjVxIXeFMA7IyKIkRQ/giphy.gif"
            await ctx.send(gif)
            if dice == int(arg):
                await ctx.send("Вы выиграли")
            else:
                await ctx.send("Вы проиграли")
        if dice == 4:
            gif = "https://media.giphy.com/media/W6fgtmQjDFKZFlqLw4/giphy.gif"
            await ctx.send(gif)
            if dice == int(arg):
                await ctx.send("Вы выиграли")
            else:
                await ctx.send("Вы проиграли")
        if dice == 5:
            gif = "https://media.giphy.com/media/lhHfJEzGFtLHhzVrTQ/giphy.gif"
            await ctx.send(gif)
            if dice == int(arg):
                await ctx.send("Вы выиграли")
            else:
                await ctx.send("Вы проиграли")
        if dice == 6:
            gif = "https://media.giphy.com/media/ma36iAcCC9P2rjR6fd/giphy.gif"
            await ctx.send(gif)
            if dice == int(arg):
                await ctx.send("Вы выиграли")
            else:
                await ctx.send("Вы проиграли")


bot.run(token)
