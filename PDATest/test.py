from pda.ext import commands
import pda

bot = commands.Bot(command_prefix="%")


@bot.event
async def on_ready():
    print("Bot is Online WITH pda!!")


# NOTE: Don't assign message event on bot directly... If you do so invoke the process_commands() function at the end


@bot.command()
async def ping(ctx: commands.Context):
    return await ctx.reply(
        "Pong! Latency is {0}ms.".format(bot.latency * 1000), mention_author=False
    )


bot.load_extension("test-cog")

bot.run("NzM0MDg4MzU3NDIzODc0MDU5.XxMnDw.8aejlBBXrP83oIu-IXGvY94Siq0")