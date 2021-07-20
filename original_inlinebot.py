from math import ceil
from re import compile
import asyncio
import html
import os
import re
import sys

from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.channels import JoinChannelRequest

from userbot import *
from userbot.cmdhelp import *
from LEGENDBOT.utils import *
from userbot.Config import Config
from userbot import ALIVE_NAME
LEGEND_row = Config.BUTTONS_IN_HELP
LEGEND_emoji = Config.EMOJI_IN_HELP
# thats how a lazy guy imports
# LEGENDBOT

def button(page, modules):
    Row = LEGEND_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"{LEGEND_emoji} " + pair + f" {LEGEND_emoji}", data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )
        
    buttons.append(
        [
            custom.Button.inline(
               f"⬅️ 𝐁𝐀𝐂𝐊🎀", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"💝 ❌ 💝", data="close"
            ),
            custom.Button.inline(
               f"🎀𝐍𝐄𝐗𝐓 ➡️", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]
    # Changing this line may give error in bot as i added some special cmds in LEGENDBOT channel to get this module work...

    modules = CMD_HELP
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query == "@LEGEND_Userbot":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            result = await builder.article(
                f"Hey! Only use .help please", 
                text=f"🔰**[{ALIVE_NAME}](https://t.me/Legend_Mr_Hacker)**\n\n📁**No. of plugins installed:** `{len(CMD_HELP)}` \n🗂**Commands:** `{len(apn)}`\n📙**page:** 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[‏‏‎ ‎]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )
        else:
            result = builder.article(
                "@LEGEND_Userbot",
                text="""**Hey! This is [LEGENDBOT.](https://t.me/Legend_Mr_Hacker) \nYou can know more about me from the links given below 👇**""",
                buttons=[
                    [
                        custom.Button.url("🔥 CREATOR 🔥", "https://t.me/Legend_Mr_Hacker"),
                        custom.Button.url(
                            "⚡ OWNER ⚡", "https://t.me/Legend_Mr_Hacker"
                        ),
                    ],
                    [
                        custom.Button.url(
                            "✨ REPO ✨", "https://github.com/LEGEND-OS/LEGENDBOT"),
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Mil Gyi Tasalli..? Kabse mere bot me ungli kr rhe h. Khudka bna lo na agr chaiye to pta nhi kaha se aajate h disturb krne. ©LEGENDBOT™ ",
                cache_time=0,
                alert=True,
            )
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        await event.edit(
            f"🛡️**[{ALIVE_NAME}](https://t.me/Legend_Mr_Hacker)** **Working...**\n\n**📁No. of modules installed :** `{len(CMD_HELP)}`\n🗂**Commands:** `{len(apn)}` \n📙**page:** {page + 1}/{veriler[0]}",
            buttons=veriler[1],
            link_preview=False,
        )
        
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await delete_LEGEND(event,
              "⚜️LEGENDBOT Menu Provider Is now Closed✔️\n\n         **[©LEGENDBOT](t.me/Legend_Mr_Hacker)**", 5, link_preview=False
            )
        else:
            LEGEND_alert = "Oh Common Yarr u think u cand Click on it😁😁😁. Deploy ur Own Bot ©LEGENDBOT"
            await event.answer(_alert, cache_time=0, alert=True)
          
    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)"))
    )
    async def Information(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Mil Gyi Tasalli..? Kabse mere bot me ungli kr rhe h. Khudka bna lo na agr chaiye to pta nhi kaha se aajate h disturb krne. ©LEGENDBOT ",
                cache_time=0,
                alert=True,
            )

        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline(
                    "𖤍 " + cmd[0] + " 𖤍", data=f"commands[{commands}[{page}]]({cmd[0]})"
                )
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer(
                "No Description is written for this plugin", cache_time=0, alert=True
            )

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline("◀️ ᏰᎯᏣᏦ", data=f"page({page})")])
        await event.edit(
            f"**📗 File:** `{commands}`\n**🔢 Number of commands :** `{len(CMD_HELP_BOT[commands]['commands'])}`",
            buttons=buttons,
            link_preview=False,
        )

    @tgbot.on(
        callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)"))
    )
    async def commands(event):
        if not event.query.user_id == bot.uid:
            return await event.answer(
                "Abhi Tak Nhi Samjha Khudka bana lo na toh Use Karna h toh kya ungli kar rhe ho. ©LEGENDBOT ",
                cache_time=0,
                alert=True,
            )

        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")

        result = f"**📗 File:** `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
                result += f"**⚠️ Warning :** {CMD_HELP_BOT[cmd]['info']['warning']}\n\n"
            else:
                result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n\n"
        else:
            result += f"**⬇️ Official:** {'✅' if CMD_HELP_BOT[cmd]['info']['official'] else '❌'}\n"
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**⚠️ Warning:** {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**ℹ️ Info:** {CMD_HELP_BOT[cmd]['info']['info']}\n\n"

        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']}`\n"
        else:
            result += f"**🛠 Commands:** `{COMMAND_HAND_LER[:1]}{command['command']} {command['params']}`\n"

        if command["example"] is None:
            result += f"**💬 Explanation:** `{command['usage']}`\n\n"
        else:
            result += f"**💬 Explanation:** `{command['usage']}`\n"
            result += f"**⌨️ For Example:** `{COMMAND_HAND_LER[:1]}{command['example']}`\n\n"

        await event.edit(
            result,
            buttons=[
                custom.Button.inline("◀️ ᏰᎯᏣᏦ", data=f"Information[{page}]({cmd})")
            ],
            link_preview=False,
        )
