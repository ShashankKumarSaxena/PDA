from pda.ext import commands

import pda

class EphemeralCounterBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('$'))

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

# Define a simple View that gives us a counter button
class Counter(pda.ui.View):

    # Define the actual button
    # When pressed, this increments the number displayed until it hits 5.
    # When it hits 5, the counter button is disabled and it turns green.
    # note: The name of the function does not matter to the library
    @pda.ui.button(label='0', style=pda.ButtonStyle.red)
    async def count(self, button: pda.ui.Button, interaction: pda.Interaction):
        number = int(button.label) if button.label else 0
        if number + 1 >= 5:
            button.style = pda.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)

# Define a View that will give us our own personal counter button
class EphemeralCounter(pda.ui.View):
    # When this button is pressed, it will respond with a Counter view that will
    # give the button presser their own personal button they can press 5 times.
    @pda.ui.button(label='Click', style=pda.ButtonStyle.blurple)
    async def receive(self, button: pda.ui.Button, interaction: pda.Interaction):
        # ephemeral=True makes the message hidden from everyone except the button presser
        await interaction.response.send_message('Enjoy!', view=Counter(), ephemeral=True)

bot = EphemeralCounterBot()

@bot.command()
async def counter(ctx: commands.Context):
    """Starts a counter for pressing."""
    await ctx.send('Press!', view=EphemeralCounter())

bot.run('token')
