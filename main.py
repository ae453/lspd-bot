import json
import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import get
import random
import time
import typing
from datetime import datetime
from pytz import timezone
from discord.ext import tasks

with open('config.json', 'r') as f:
    data = json.load(f)
    token = data['token']
    prefix = data['prefix']

bot = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), case_insensitive=True, intents=discord.Intents.all())
bot.is_synced = False
bot.remove_command("help")

@tasks.loop(minutes=1)
async def status():
    choices = [
        discord.Activity(type=discord.ActivityType.listening, name='Code 3 Sirens'),
        discord.Activity(type=discord.ActivityType.watching, name='Body Cam Footage'),
        discord.Activity(type=discord.ActivityType.watching, name='Over Police Units'),
        discord.Game('FiveM'),
        discord.Game('West Coast Roleplay'),
        discord.Game('with N. Watson'),
        discord.Game('with F. Sheets'), 
        discord.Game('with Other Units')
    ]
    chosen = random.choice(choices)
    await bot.change_presence(activity=chosen)

@bot.event
async def on_ready():
    e = None
    try:
        channel = bot.get_channel(1049996024619474974)
        await channel.send(f'{bot.user.mention} is now online!')
    except Exception as e:
        print(e)
        await channel.send(f'{e}')
        return e
    if e == None:
        await channel.send(f"> All Functions Seem to be Operational.")
    if e != None:
        await channel.send(f"> We are Currently Having Issues with Some Functions.")
    print(f'The LSPD Bot is Now Online!')

    if not bot.is_synced:
        bot.tree.copy_global_to(guild=discord.Object(id=1043951982139940955))
    await bot.tree.sync()
    bot.is_synced = True

    status.start()


async def avatar(ctx: commands.Context, member: typing.Union[discord.Member, discord.User] = None):
    if member == None:
        try:
            member = ctx.author
            Avatar = member.avatar.url
            return Avatar
        except Exception as e:
            await ctx.channel.send(f"Uh Oh. Something Went Wrong! Exception Raised, Process Terminated.\n> `{e}`")
            print(e)
            time.sleep(5)
            pass
    else:
        try:
            Avatar = member.avatar.url
            return Avatar
        except Exception as e:
            await ctx.channel.send(f"Uh Oh. Something Went Wrong! Exception Raised, Process Terminated.\n> `{e}`")
            print(e)
            time.sleep(5)
            pass

@bot.command(name="ping", description="Simple ping pong command")
async def ping(ctx, interaction):
    await ctx.reply(f"Pong", ephemeral=True)

@bot.hybrid_command(
    name="promologchannel",
    ephemeral=True
)
async def promologchannel(ctx: commands.Context, channel):
    chiefcheck = discord.utils.get(ctx.author.roles, id=1043952177128951849)
    if chiefcheck or ae453check == true:
        await ctx.reply("Process Initalized.")
        return True
    else:
        await ctx.reply(f"Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `User does not pertain the neccessary roles to complete this action!`")
        return False
    if True:
        if channel == channel.id:
            await ctx.reply(f"Channel Selected: <#{channel}>")
            return True
        else:
            await ctx.reply(f"Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `Integer Imported Does Not Represent a Channel.`")
            return False
            try:
                with open('config.json', 'w') as f:
                    data = json.load(f)
                    data['promolog']
                    f.write(channel)
                    newchannel = data['promolog']
                    if newchannel == channel:
                        return True
                    else:
                        return False
            except Exception as e:
                print(e)
                return e
            if True:
                await ctx.reply(f"The Promotion Log Channel has Successfully Been Change to <#{channel}>")
            else:
                await ctx.reply(f"Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `{e}`")

@bot.hybrid_group(
    name="unit"
)
async def unit(ctx):
    pass

@unit.command(
    name="modify",
    ephemeral=True
)
@discord.app_commands.checks.has_any_role(1043952177128951849, 1043952204211556373)
async def modify(ctx: commands.Context, username: typing.Union[discord.Member, discord.User], previousrank, newrank, details):
    previousrank = previousrank.lower()
    newrank = newrank.lower()
    newrankrole = discord.Role
    prevrankrole = discord.Role
    userid = username.id
    member = ctx.guild.get_member(userid)
    if newrank == "probationary officer":
        newrankrole = get(member.guild.roles, id=1050326925157081108)
    elif newrank == "officer":
        newrankrole = get(member.guild.roles, id=1043952220951027762)
    elif newrank == "sergeant":
        newrankrole = get(member.guild.roles, id=1043952212897955901)
    elif newrank == "commander":
        newrankrole = get(member.guild.roles, id=1043952206568759388)
    elif newrank == "senior commander":
        newrankrole = get(member.guild.roles, id=1043952206568759388)
    elif newrank == "deputy chief":
        newrankrole = get(member.guild.roles, id=1043952205176250480)
    elif newrank == "assistant chief":
        newrankrole = get(member.guild.roles, id=1043952202143764661)
    else:
        return await ctx.reply(f"Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `Variable 'newrank' does not represent any current rank. Check your spelling and try again.`")
    if previousrank == "probationary officer":
        prevrankrole = get(member.guild.roles, id=1050326925157081108)
    elif previousrank == "officer":
        prevrankrole = get(member.guild.roles, id=1043952220951027762)
    elif previousrank == "sergeant":
        prevrankrole = get(member.guild.roles, id=1043952212897955901)
    elif previousrank == "commander":
        prevrankrole = get(member.guild.roles, id=1043952206568759388)
    elif previousrank == "senior commander":
        prevrankrole = get(member.guild.roles, id=1043952206568759388)
    elif previousrank == "deputy chief":
        prevrankrole = get(member.guild.roles, id=1043952205176250480)
    elif previousrank == "assistant chief":
        prevrankrole = get(member.guild.roles, id=1043952202143764661)
    else:
        return await ctx.reply(f"Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `Variable 'previousrank' does not represent any current rank. Check your spelling and try again.`")
    if newrankrole >= ctx.author.top_role:
        return await ctx.reply("Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `User Requested Promotion for a Higher Rank than Themselves`")
    elif newrankrole <= ctx.author.top_role:
        pass
    if username == ctx.author:
        print("Process Terminated.\n    Reason: User attempted to promote self.")
        return await ctx.reply("Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `User Attempted to Promote Self`")
    else:
        pass
#### Fixing Grammar
    if previousrank == "probationary officer":
        prevranktext = "Probationary Officer"
    elif previousrank == "officer":
        prevranktext = "Officer"
    elif previousrank == "sergeant":
        prevranktext = "Sergeant"
    elif previousrank == "commander":
        prevranktext = "Commander"
    elif previousrank == "senior commander":
        prevranktext = "Senior Commander"
    elif previousrank == "deputy chief":
        prevranktext = "Deputy Chief of Police"
    elif previousrank == "assistant chief":
        prevranktext = "Assistant Chief of Police"
    elif previousrank == "chief":
        prevranktext = "Chief of Police"
    else:
        return await ctx.reply("Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `Improper Rank for Variable 'previousrank'. Check Your Spelling and Try Again.`")
    if newrank == "probationary officer":
        newranktext = "Probationary Officer"
    elif newrank == "officer":
        newranktext = "Officer"
    elif newrank == "sergeant":
        newranktext = "Sergeant"
    elif newrank == "commander":
        newranktext = "Commander"
    elif newrank == "senior commander":
        newranktext = "Senior Commander"
    elif newrank == "deputy chief":
        newranktext = "Deputy Chief of Police"
    elif newrank == "assistant chief":
        newranktext = "Assistant Chief of Police"
    elif newrank == "chief":
        newranktext = "Chief of Police"
    else:
        return await ctx.reply("Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `Improper Rank for Variable 'newrank'. Check Your Spelling and Try Again.`")
#### Setting Emojis
    if previousrank == "probationary officer":
        prevrankemoji = "<:LSPDLogo:1049462994297442364>"
    elif previousrank == "officer":
        prevrankemoji = "<:LSPDLogo:1049462994297442364>"
    elif previousrank == "sergeant":
        prevrankemoji = "<:Sergeant:1049455524346875914> "
    elif previousrank == "commander":
        prevrankemoji = "<:Commander:1049454364797960243>"
    elif previousrank == "senior commander":
        prevrankemoji = "<:SeniorCommander:1049454125466800162>"
    elif previousrank == "deputy Chief":
        prevrankemoji = "<:DeputyChief:1049454113903099934>"
    elif previousrank == "assistant chief":
        prevrankemoji = "<:AssistantChief:1049454102314233887>"
    elif previousrank == "chief":
        prevrankemoji = "<:Chief:1049454084962406410>"
    else:
        return await ctx.reply("Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `Improper Rank for Variable 'previousrank'. Check Your Spelling and Try Again.`")
    if newrank == "probationary officer":
        newrankemoji = "<:LSPDLogo:1049462994297442364>"
    elif newrank == "officer":
        newrankemoji = "<:LSPDLogo:1049462994297442364>"
    elif newrank == "sergeant":
        newrankemoji = "<:Sergeant:1049455524346875914> "
    elif newrank == "commander":
        newrankemoji = "<:Commander:1049454364797960243>"
    elif newrank == "senior commander":
        newrankemoji = "<:SeniorCommander:1049454125466800162>"
    elif newrank == "deputy chief":
        newrankemoji = "<:DeputyChief:1049454113903099934>"
    elif newrank == "assistant chief":
        newrankemoji = "<:AssistantChief:1049454102314233887>"
    elif newrank == "chief":
        newrankemoji = "<:Chief:1049454084962406410>"
    else:
        return await ctx.reply("Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `Improper Rank for Variable 'newrank'. Check Your Spelling and Try Again.`")
    if previousrank == "probationary officer":
        prevrankrole2 = get(member.guild.roles, id=1043961157641310258) # category role
        await member.remove_roles(prevrankrole)
        await member.remove_roles(prevrankrole2)
    if previousrank == "officer":
        prevrankrole2 = get(member.guild.roles, id=1043952218962931733)  # category role
        await member.remove_roles(prevrankrole)
        await member.remove_roles(prevrankrole2)
    if previousrank == "sergeant":
        prevrankrole2 = get(member.guild.roles, id=1043952208863055902)  # category role
        await member.remove_roles(prevrankrole)
        await member.remove_roles(prevrankrole2)
    if previousrank == "commander":
        prevrankrole2 = get(member.guild.roles, id=1043952204211556373)  # category role
        await member.remove_roles(prevrankrole)
        await member.remove_roles(prevrankrole2)
    if previousrank == "senior commander":
        prevrankrole2 = get(member.guild.roles, id=1043952204211556373)  # category role
        await member.remove_roles(prevrankrole)
        await member.remove_roles(prevrankrole2)
    if previousrank == "deputy chief":
        prevrankrole2 = get(member.guild.roles, id=1043952177128951849)  # category role
        await member.remove_roles(prevrankrole)
        await member.remove_roles(prevrankrole2)
    if previousrank == "assistant chief":
        prevrankrole2 = get(member.guild.roles, id=1043952177128951849)  # category role
        await member.remove_roles(prevrankrole)
        await member.remove_roles(prevrankrole2)
    if newrank == "probationary officer":
        newrankrole2 = get(member.guild.roles, id=1043961157641310258) # category role
        await member.add_roles(newrankrole)
        await member.add_roles(newrankrole2)
    if newrank == "officer":
        newrankrole2 = get(member.guild.roles, id=1043952218962931733) # category role
        await member.add_roles(newrankrole)
        await member.add_roles(newrankrole2)
    if newrank == "sergeant":
        newrankrole2 = get(member.guild.roles, id=1043952208863055902) # category role
        await member.add_roles(newrankrole)
        await member.add_roles(newrankrole2)
    if newrank == "commander":
        newrankrole2 = get(member.guild.roles, id=1043952204211556373) # category role
        await member.add_roles(newrankrole)
        await member.add_roles(newrankrole2)
    if newrank == "senior commander":
        newrankrole2 = get(member.guild.roles, id=1043952204211556373) # category role
        await member.add_roles(newrankrole)
        await member.add_roles(newrankrole2)
    if newrank == "deputy chief":
        newrankrole2 = get(member.guild.roles, id=1043952177128951849) # category role
        await member.add_roles(newrankrole)
        await member.add_roles(newrankrole2)
    if newrank == "assistant chief":
        newrankrole2 = get(member.guild.roles, id=1043952177128951849) # category role
        await member.add_roles(newrankrole)
        await member.add_roles(newrankrole2)
    #### Setting up the Embed
    authorName = ctx.message.author
    authorPhoto = ctx.message.author.display_avatar
    memberAvatar = await avatar(ctx, member=username)
    embedPromote = discord.Embed(
        title="🎉🎉 ***LSPD Promotion Logging*** 🎉🎉\n",
        description="<:lines:1050287334752526356>"*15,
        color=0x0599f0
    )
    embedPromote.add_field(
        name="<:userbadge:1050285701482151956> User",
        value="<:lines:1050287334752526356>"*4 + f"\n<:line_arrow_white:1050286867326705665> *<@{userid}>*",
        inline=False
    )
    embedPromote.add_field(
        name=f":military_medal: Previous Rank {prevrankemoji}",
        value=f"<:lines:1050287334752526356>"*8 + f"\n<:line_arrow_white:1050286867326705665> *{prevranktext}*",
        inline=False
    )
    embedPromote.add_field(
        name=f":military_medal: New Rank {newrankemoji}",
        value="<:lines:1050287334752526356>"*7 + f"\n<:line_arrow_white:1050286867326705665> *{newranktext}*",
        inline=False
    )
    embedPromote.add_field(
        name=":pencil: Details",
        value="<:lines:1050287334752526356>"*5 + f"\n<:line_arrow_white:1050286867326705665> *{details}*",
        inline=False
    )
    embedPromote.set_author(name=authorName, url=None, icon_url=authorPhoto)
    embedPromote.set_thumbnail(url=memberAvatar)
    embedPromote.set_footer(text="𝘛𝘳𝘶𝘴𝘵𝘦𝘥 𝘚𝘦𝘳𝘷𝘪𝘤𝘦 𝘸𝘪𝘵𝘩 𝘙𝘦𝘴𝘱𝘦𝘤𝘵",
                            icon_url="https://media.discordapp.net/attachments/1025840738388410428/1026548866675392662/Seal_of_LS_Ghost.png",
                            )
    tz = timezone('EST')
    embedPromote.timestamp = datetime.now(tz)
#### Sending Initial Messages to User
    time.sleep(2)
    try:
        with open('config.json', 'r') as f:
            data = json.load(f)
            promologid = data['promolog']
        channel = bot.get_channel(promologid)
        await channel.send(embed=embedPromote)
        await ctx.reply('Promotion Sucessfully Logged! :tada:')
        print(f'{username} has been promoted!')
    except Exception as e:
        await ctx.channel.send(f"Uh Oh. Something Went Wrong! Exception Raised, Process Terminated.\n> `{e}`")
        print(e)


bot.run(token)
