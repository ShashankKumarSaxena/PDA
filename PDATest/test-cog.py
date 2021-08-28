from PDA.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Test")

def setup(bot):
    bot.add_cog(TestCog(bot))