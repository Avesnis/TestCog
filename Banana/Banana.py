import discord
from discord.ext import commands

class Power:
    """initialize Doomsday!"""

    def __init__(self, bot):
        self.bot = bot

	@commands.command()
    async def wake(self, server, owner):
        await self.bot.say("Are you sure you want me "
                    "to connect {}? (yes/no)".format(server.name))

        msg = await self.bot.wait_for_message(author=owner, timeout=15)

        if msg is None:
            await self.bot.say("Connection terminated")
		elif msg.content.lower().strip() in ("yes", "y"):
            await self.bot.say("connecting...")
        elif msg.content.lower().strip() in ("no", "n"):
            await self.bot.say("Terminating connection ")
                await self.bot.say("Done.")
        else:
            await self.bot.say("Alright then.")
def setup(bot):
    bot.add_cog(Banana(bot))
