# hi we are back here so you will need to import the modules
from discord.ext import commands # you see now why we need the commands.Bot and not the client
# now we need to make a class
class Example(commands.Cog):
  # now we are gonna need to define init
  def __init__(self, bot):
    self.bot = bot # self value will we important (to refer to the client variable we will need to do self.bot
  
  # now we are gonna make a command
  @commands.command()
  async def example(self, ctx):
    # you will now need to import self before ctx on every commands, event or wathever you do
    await ctx.send('Hi your cogs are working !')
  
  # you don't need these it's just to show you how to do an event and a listener
  @commands.event
  async def on_message(self, message):
    await self.bot.process_commands(message)
    if message.content.lower() == 'hi':
      await message.reply('Hi !')
      
  @commands.Cog.listener('on_message')
  async def saying_bye(self, message):
    if message.content.lower() == 'bye':
      await message.reply('Bye, have a nice day !')
    
    
# now we are gonna need to make the setup fonction
def setup(bot):
  bot.add_cog(Example(bot))
  # you will need to put the name of the class in the add_cog(...)
# and guess what
# you are done !
# without any comments your cogs should look like this
"""
from discord.ext import commands # you see now why we need the commands.Bot and not the client

class Example(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def example(self, ctx):
    await ctx.send('Hi your cogs are working !')
  
  @commands.event
  async def on_message(self, message):
    await self.bot.process_commands(message)
    if message.content.lower() == 'hi':
      await message.reply('Hi !')
      
  @commands.Cog.listener('on_message')
  async def saying_bye(self, message):
    if message.content.lower() == 'bye':
      await message.reply('Bye, have a nice day !')
      
def setup(bot):
  bot.add_cog(Example(bot))
"""
# and that's it !
