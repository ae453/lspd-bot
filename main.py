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
    prefix = data['prefix']

with open('token.json', 'r') as f:
    data = json.load(f)
    token = data['token']

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
    try:
        channel = bot.get_channel(1050893912950177803)
        await channel.send(f'{bot.user.mention} is now online!')
    except Exception as e:
        print(e)
        await channel.send(f"> We are Currently Experiencing Some Issues with Some Functions, Please Try Again Later.\n> `Processes Terminated. Exception Raised.`")
        await channel.send(f'> `{e}`')
        return e
    await channel.send(f"> All Functions Seem to be Operational.")
    print(f'The LSPD Bot is Now Online!')

    if not bot.is_synced:
        bot.tree.copy_global_to(guild=discord.Object(id=1050863587926749235))
    await bot.tree.sync()
    bot.is_synced = True
    await bot.load_extension('jishaku')

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
            return
    else:
        try:
            Avatar = member.avatar.url
            return Avatar
        except Exception as e:
            await ctx.channel.send(f"Uh Oh. Something Went Wrong! Exception Raised, Process Terminated.\n> `{e}`")
            print(e)
            time.sleep(5)
            return

@bot.command(name="ping", description="Simple ping pong command")
async def ping(ctx, interaction):
    await ctx.reply(f"Pong", ephemeral=True)

@bot.hybrid_command(
    name="promologchannel",
    ephemeral=True
)
async def promologchannel(ctx: commands.Context, channel):
    chiefcheck = discord.utils.get(ctx.author.roles, id=1050868223547019425)
    if chiefcheck == true:
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
                        pass
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
@discord.app_commands.checks.has_any_role(1050868223547019425, 1050871457653202956)
async def modify(ctx: commands.Context, username: typing.Union[discord.Member, discord.User], previousrank, newrank, details):
    tz = timezone('EST')
    print(f"{ctx.author} attempted to run `/unit modify` inside {ctx.channel} at {timezone('EST')} Eastern Standard Time! Unkown exceptions at this time.")
    previousrank = previousrank.lower()
    newrank = newrank.lower()

    newrankrole = discord.Role
    prevrankrole = discord.Role
    newrankrole2 = discord.Role
    prevrankrole2 = discord.Role

    probie_newrankrole = discord.Role
    officer_newrankrole = discord.Role
    sgt1_newrankrole1 = discord.Role
    commander_newrankrole = discord.Role
    chief_newrankrole = discord.Role

    probie_newrankrole2 = discord.Role
    officer_newrankrole2 = discord.Role
    supervisor_newrankrole2 = discord.Role
    commander_newrankrole2 = discord.Role
    chief_newrankrole2 = discord.Role

    probie_prevrankrole2 = discord.Role
    officer_prevrankrole2 = discord.Role
    supervisor_prevrankrole2 = discord.Role
    commander_prevrankrole2 = discord.Role
    chief_prevrankrole2 = discord.Role

    probie_prevrankrole = discord.Role
    officer_prevrankrole = discord.Role
    sgt1_prevrankrole = discord.Role
    sgt2_prevrankrole = discord.Role
    sgt3_prevrankrole = discord.Role
    sgt4_prevrankrole = discord.Role
    commander_prevrankrole = discord.Role
    chief_prevrankrole = discord.Role

    userid = username.id
    member = ctx.guild.get_member(userid)
    if newrank == "probationary officer":
        entry_newrankrole2 = get(member.guild.roles, id=1050873087274520668)  # category role
        probie_newrankrole = get(member.guild.roles, id=1050872986263105567)
        newrankrole = probie_newrankrole2
        newrankrole2 = entry_newrankrole2
        return newrankrole2
    elif newrank == "officer":
        swornIn_newrankrole2 = get(member.guild.roles, id=1050872870848430121)  # category role
        officer_newrankrole = get(member.guild.roles, id=1050872931628105760)
        newrankrole = officer_newrankrole
        newrankrole2 = swornIn_newrankrole2
        return newrankrole2
    elif newrank == "sergeant":
        supervisor_newrankrole2 = get(member.guild.roles, id=1050871602058903572)  # category role
        sgt1_newrankrole1 = get(member.guild.roles, id=1050872770063515718)
        newrankrole = sgt1_newrankrole1
        newrankrole2 = supervisor_newrankrole2
        return newrankrole2
    elif newrank == "commander":
        command_newrankrole2 = get(member.guild.roles, id=1050871457653202956)  # category role
        commander_newrankrole = get(member.guild.roles, id=1050871551353954405)
        newrankrole = commander_newrankrole
        newrankrole2 = command_newrankrole2
        if commander_newrankrole2 >= ctx.author.top_role.position:
            return await ctx.reply("Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `User Requested Promotion for a Higher Rank than Themselves`")
        return newrankrole2
    elif newrank == "senior commander":
        command_newrankrole2 = get(member.guild.roles, id=1050871457653202956)  # category role
        commander_newrankrole = get(member.guild.roles, id=1050871518302847016)
        newrankrole = commander_newrankrole
        newrankrole2 = command_newrankrole2
        if command_newrankrole2 >= ctx.author.top_role:
            return await ctx.reply("Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `User Requested Promotion for a Higher Rank than Themselves`")
        return newrankrole2
    elif newrank == "deputy chief":
        chief_newrankrole2 = get(member.guild.roles, id=1050868223547019425)  # category role
        chief_newrankrole = get(member.guild.roles, id=1050871342129496146)
        newrankrole = chief_newrankrole
        newrankrole2 = chief_newrankrole2
        if chief_newrankrole >= ctx.author.top_role:
            return await ctx.reply("Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `User Requested Promotion for a Higher Rank than Themselves`")
        return newrankrole2
    elif newrank == "assistant chief":
        chief_newrankrole2 = get(member.guild.roles, id=1050868223547019425)  # category role
        chief_newrankrole = get(member.guild.roles, id=1050871238660206662)
        newrankrole = chief_newrankrole
        newrankrole2 = chief_newrankrole2
        if chief_newrankrole2 >= ctx.author.top_role:
            return await ctx.reply("Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `User Requested Promotion for a Higher Rank than Themselves`")
        return newrankrole2
    else:
        return await ctx.reply(f"Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `Variable 'newrank' does not represent any current rank. Check your spelling and try again.`")
    if previousrank == "probationary officer":
        entry_prevrankrole2 = get(member.guild.roles, id=1050873087274520668)  # category role
        probie_prevrankrole = get(member.guild.roles, id=1050872986263105567)
        prevrankrole = probie_prevrankrole
        prevrankrole2 = entry_prevrankrole2
        return prevrankrole2
    elif previousrank == "officer":
        swornIn_prevrankrole2 = get(member.guild.roles, id=1050872870848430121)  # category role
        officer_prevrankrole = get(member.guild.roles, id=1050872931628105760)
        prevrankrole = officer_prevrankrole
        prevrankrole2 = swornIn_prevrankrole2
        return prevrankrole2
    elif previousrank == "sergeant":
        supervisor_prevrankrole2 = get(member.guild.roles, id=1050871602058903572)  # category role
        sgt1_prevrankrole1 = get(member.guild.roles, id=1050872770063515718)
        sgt2_prevrankrole2 = get(member.guild.roles, id=1050872690795348090)
        sgt3_prevrankrole3 = get(member.guild.roles, id=1050871917072097280)
        sgt4_prevrankrole4 = get(member.guild.roles, id=1050871664038121472)
        prevrankrole = sgt1_prevrankrole
        prevrankrole2 = supervisor_prevrankrole2
        return prevrankrole2
    elif previousrank == "commander":
        command_prevrankrole2 = get(member.guild.roles, id=1050871457653202956)  # category role
        commander_prevrankrole = get(member.guild.roles, id=1050871551353954405)
        prevrankrole = commander_prevrankrole
        prevrankrole2 = command_prevrankrole2
        return prevrankrole2
    elif previousrank == "senior commander":
        command_prevrankrole2 = get(member.guild.roles, id=1050871457653202956)  # category role
        commander_prevrankrole = get(member.guild.roles, id=1050871518302847016)
        prevrankrole = commander_prevrankrole
        prevrankrole2 = command_prevrankrole2
        return prevrankrole2
    elif previousrank == "deputy chief":
        chief_prevrankrole2 = get(member.guild.roles, id=1050868223547019425)  # category role
        chief_prevrankrole = get(member.guild.roles, id=1050871342129496146)
        prevrankrole = chief_prevrankrole
        prevrankrole2 = chief_prevrankrole2
        return prevrankrole2
    elif previousrank == "assistant chief":
        chief_prevrankrole2 = get(member.guild.roles, id=1050868223547019425)  # category role
        chief_prevrankrole = get(member.guild.roles, id=1050871238660206662)
        prevrankrole = chief_prevrankrole
        prevrankrole2 = chief_prevrankrole2
        return prevrankrole2
    else:
        return await ctx.reply(f"Uh-Oh, Something Went Wrong! Exception Raised, Process Terminated.\n> `Variable 'previousrank' does not represent any current rank. Check your spelling and try again.`")
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
        await member.remove_roles(probie_prevrankrole)
        await member.remove_roles(entry_prevrankrole2)
    elif previousrank == "officer":
        await member.remove_roles(officer_prevrankrole)
        await member.remove_roles(swornIn_prevrankrole2)
    elif previousrank == "sergeant":
        await member.remove_roles(sgt1_prevrankrole1)
        await member.remove_roles(sgt2_prevrankrole2)
        await member.remove_roles(sgt3_prevrankrole3)
        await member.remove_roles(sgt4_prevrankrole4)
        await member.remove_roles(supervisor_prevrankrole2)
    elif previousrank == "commander" or "senior commander":
        await member.remove_roles(commander_prevrankrole)
        await member.remove_roles(command_prevrankrole2)
    elif previousrank == "deputy chief" or "assistant chief" or "chief":
        await member.remove_roles(chief_prevrankrole)
        await member.remove_roles(chief_prevrankrole2)
    if newrank == "probationary officer":
        await member.add_roles(probie_newrankrole)
        await member.add_roles(entry_newrankrole2)
    elif newrank == "officer":
        await member.add_roles(officer_newrankrole)
        await member.add_roles(swornIn_newrankrole2)
    elif newrank == "sergeant":
        await member.add_roles(sgt1_newrankrole1)
        await member.add_roles(supervisor_newrankrole2)
    elif newrank == "commander" or "senior commander":
        await member.add_roles(commander_newrankrole)
        await member.add_roles(command_newrankrole2)
    elif newrank == "deputy chief" or "assistant chief" or "chief":
        await member.add_roles(chief_newrankrole)
        await member.add_roles(chief_newrankrole2)
    #### Setting up the Embed
    authorName = ctx.message.author
    authorPhoto = ctx.message.author.display_avatar
    memberAvatar = await avatar(ctx, member=username)
    if prevrankrole2 >= newrankrole2:
        if prevrankrole >= newrankrole:
            embedPromote = discord.Embed(
                title="***LSPD Promotion Logging***\n",
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
            embedPromote.timestamp = datetime.now(tz)
        #### Sending Initial Messages to User
            time.sleep(2)
            #try:
            with open('config.json', 'r') as f:
                data = json.load(f)
                promologid = data['promolog']
            channel = bot.get_channel(promologid)
            await channel.send(embed=embedPromote)
            await ctx.reply('Promotion Sucessfully Logged! :tada:')
            print(f'{username} has been promoted!')
            #except Exception as e:
            #    await ctx.channel.send(f"Uh Oh. Something Went Wrong! Exception Raised, Process Terminated.\n> `{e}`")
            #    print(e)
            #    return
    elif prevrankrole2 <= newrankrole2:
        if prevrankrole <= newrankrole:
            embedDemote = discord.Embed(
                title="***LSPD Demotion Logging***\n",
                description="<:lines:1050287334752526356>" * 15,
                color=0x0599f0
            )
            embedDemote.add_field(
                name="<:userbadge:1050285701482151956> User",
                value="<:lines:1050287334752526356>" * 4 + f"\n<:line_arrow_white:1050286867326705665> *<@{userid}>*",
                inline=False
            )
            embedDemote.add_field(
                name=f":military_medal: Previous Rank {prevrankemoji}",
                value=f"<:lines:1050287334752526356>" * 8 + f"\n<:line_arrow_white:1050286867326705665> *{prevranktext}*",
                inline=False
            )
            embedDemote.add_field(
                name=f":military_medal: New Rank {newrankemoji}",
                value="<:lines:1050287334752526356>" * 7 + f"\n<:line_arrow_white:1050286867326705665> *{newranktext}*",
                inline=False
            )
            embedDemote.add_field(
                name=":pencil: Details",
                value="<:lines:1050287334752526356>" * 5 + f"\n<:line_arrow_white:1050286867326705665> *{details}*",
                inline=False
            )
            embedDemote.set_author(name=authorName, url=None, icon_url=authorPhoto)
            embedDemote.set_thumbnail(url=memberAvatar)
            embedDemote.set_footer(text="𝘛𝘳𝘶𝘴𝘵𝘦𝘥 𝘚𝘦𝘳𝘷𝘪𝘤𝘦 𝘸𝘪𝘵𝘩 𝘙𝘦𝘴𝘱𝘦𝘤𝘵",
                                    icon_url="https://media.discordapp.net/attachments/1025840738388410428/1026548866675392662/Seal_of_LS_Ghost.png",
                                    )
            embedDemote.timestamp = datetime.now(tz)
            #### Sending Initial Messages to User
            time.sleep(2)
            #try:
            with open('config.json', 'r') as f:
                data = json.load(f)
                promologid = data['promolog']
            channel = bot.get_channel(promologid)
            await channel.send(embed=embedDemote)
            await ctx.reply('Demotion Sucessfully Logged! <:check:1050933083442008094>')
            print(f'{username} has been demoted!')
            #except Exception as e:
            #    await ctx.channel.send(f"Uh Oh. Something Went Wrong! Exception Raised, Process Terminated.\n> `{e}`")
            #    print(e)
            #    return
    else:
        await ctx.channel.send(f"Uh Oh. Something Went Wrong! Exception Raised, Process Terminated.\n> `Unkown Excpetion`")
        return


bot.run(token)
