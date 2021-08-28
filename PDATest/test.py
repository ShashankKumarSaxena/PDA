from PDA.ext.commands.core import command
from PDA.ext import commands
import PDA

bot = commands.Bot(command_prefix="%")


@bot.event
async def on_ready():
    print("Bot is Online WITH PDA!!")


# NOTE: Don't assign message event on bot directly... If you do so invoke the process_commands() function at the end


@bot.command()
async def ping(ctx: commands.Context):
    return await ctx.reply(
        "Pong! Latency is {0}ms.".format(bot.latency * 1000), mention_author=False
    )


bot.load_extension("test-cog")

bot.run("TOKEN")