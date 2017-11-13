import discord
import re
import asyncio
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='h!', description='This is a practice development bot created by katchshi#0454 on discord.')

@bot.event
async def on_ready(): #states bot's name when successfully connected to discord
        print('Currently logged in as: ')
        print(bot.user.name)

@bot.command()
async def rawr():
    await bot.say('XD')

@bot.command()
async def h():
    await bot.say('h-hewwo???')

@bot.command()
async def flux():
    await bot.say('stop c;')

@bot.command()
async def cinx():
    await bot.say('I go by Rib now!! >:(')

@bot.command(pass_context=True)
async def slap(ctx):
    menn = ' and '.join([str(member.mention) for member in ctx.message.mentions])
    await bot.say(':cry: | {0.message.author.mention} **just slapped** ' % menn % '!')

@bot.command(pass_context=True)
async def slap2(ctx):
    menn = ' and '.join([str(member.mention) for member in ctx.message.mentions])
    await bot.say(':cry: | {0.message.author.mention} **just slapped** {1}'.format(ctx, menn))

@bot.command(pass_context=True)
async def ment(ctx):
    mentions = ctx.message.mentions
    count = len(mentions)
    await bot.say (count)
    menn = ' and '.join([str(member.mention) for member in ctx.message.mentions])
    await bot.say(menn)

@bot.command(pass_context=True)
async def juice(ctx):
    menn = ' and '.join([str(member.mention) for member in ctx.message.mentions])
    if len(ctx.message.mentions) < 1:
        menn = 'themselves'
    juices = ['orange :orange:', 'apple :apple:', 'cherry :cherries:', 'peach :peach:', 'boy :boy:', 'grape :grapes:', 'pineapple :pineapple:']
    juice_ch = random.choice(juices)
    await bot.say('{0.message.author.mention} **just handed** {1} some {2} juice!'.format(ctx, menn, juice_ch))

@bot.command(pass_context=True)
async def cry(ctx):
    menn = ' and '.join([str(member.mention) for member in ctx.message.mentions])
    if len(ctx.message.mentions) < 1:
        menn = '{0.message.author.mention}'.format(ctx)
    await bot.say('don\'t cry, %s' % menn)
    channel = ctx.message.channel
    with open('img1.png', 'rb') as f:
        await bot.send_file(channel, f)

@bot.command(pass_context=True)
async def wet(ctx):
    menn = ' and '.join([str(member.mention) for member in ctx.message.mentions])
    await bot.say('you need to dry yourself off, {1}'.format(ctx, menn))
    channel = ctx.message.channel
    with open('img2.png', 'rb') as f:
        await bot.send_file(channel, f)

@bot.command(pass_context=True)
async def insult(ctx):
    number = randint(1, 3)
    if number == 3:
        await bot.say('fuckin\' lookin ass furry')
    if number == 2:
        await bot.say('your reatard')
    if number == 1:
        await bot.say('vaping is ghey, dude')

bot.run('')
