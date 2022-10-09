import discord 
from discord.ext import commands 

client = commands.Bot(command_prefix = '>')

@client.event 
async def on_ready():
    print('Helper bot is now online.')

@client.command() 
async def kick(ctx, member:discord.Member, *, reason=None): 
    if (not ctx.author.guild_permissions.kick_members):
        await ctx.send('You do not have access to this command.')
        return
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked from the server.')

@client.command() 
async def ban(ctx, member:discord.Member, *, reason=None): 
    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send('You do not have access to this command.')
        return
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned from the server.')

@client.command() 
async def unban(ctx, *, member):
    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send('You do not have access to this command.')
        return
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user 

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}.')
            return 

@client.command(aliases=['purge'])
async def clear(ctx, amount=11):
    if (not ctx.author.guild_permissions.manage_messages):
        await ctx.send('You do not have access to this command.')
        return
    amount = amount+1
    if amount > 101:
        await ctx.send('Can not purge more than 100 messages.')
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Purged ${amount} messages.')


client.run('TOKEN')
