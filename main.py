from discord.ext import commands
# importing the package we need
import os
# making a commands.Bot client (discord.Client does not work with cogs :/)
client = commands.Bot(command_prefix=['-'])
# we need some reload commands
@client.command()
async def reload(ctx):
  for fn in os.listdir("./cogs"): 
    if fn.endswith('.py'): 
      client.reload_extension(f'cogs.{fn[: -3]}')
# explanation of the code :
# for fn in os.listdir("./cogs"):
# for any file in the folder named cogs
# if the file end with .py (making sure it's a python file)
# reload it
# here is a one line method for the one liner persons
# for fn in os.listdir('./cogs'): client.reload_extension(f'cogs.{fn[: -3]}') if fn.endswith('.py')
# now we are gonna need to load it
for fn in os.listdir("./cogs"): 
  if fn.endswith('.py'): 
    client.load_extension(f'cogs.{fn[: -3]}')
client.run(token)
# just put this anywhere and that it you are done for the main file now create a folder named cogs in the same folder of your main.py
# this is what the code look like without any comments
"""
from discord.ext import commands
import os
client = commands.Bot(command_prefix=['-'])
@client.command()
async def reload(ctx):
  for fn in os.listdir("./cogs"): 
    if fn.endswith('.py'): 
      client.reload_extension(f'cogs.{fn[: -3]}')
for fn in os.listdir("./cogs"): 
  if fn.endswith('.py'): 
    client.load_extension(f'cogs.{fn[: -3]}')
client.run(token)

"""
# here is a one liners way
"""
from discord.ext import commands
import os
client = commands.Bot(command_prefix=['-'])
@client.command()
async def reload(ctx):
  for fn in os.listdir('./cogs'): client.reload_extension(f'cogs.{fn[: -3]}') if fn.endswith('.py')
for fn in os.listdir('./cogs'): client.load_extension(f'cogs.{fn[: -3]}') if fn.endswith('.py')
client.run(token)
"""
# here is a way with minimum import and one liner
"""
from discord.ext.commands import Bot
from os import listdir
client = Bot(command_prefix=['-'])
@client.command()
async def reload(ctx):
  for fn in listdir('./cogs'): client.reload_extension(f'cogs.{fn[: -3]}') if fn.endswith('.py')
for fn in listdir('./cogs'): client.load_extension(f'cogs.{fn[: -3]}') if fn.endswith('.py')
client.run(token)
"""
# and there we go that's it
