import time

from telethon import version
from userbot import ALIVE_NAME, StartTime, LEGENDversion
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

async def reply_id(event):
    reply_to_id = None
    if event.sender_id in Config.SUDO_USERS:
        reply_to_id = event.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


DEFAULTUSER = ALIVE_NAME or "LEGEND"
LEGEND_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "Legend's Choice LEGENDBOT"

USERID = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - StartTime))


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  LEGEND_IMG:
        LEGEND_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        
        LEGEND_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        LEGEND_caption += f"**┏━━━━━━━━━━━━━┓**\n"
        LEGEND_caption += f"        __**𖤍BOT STATUS𖤍**__\n"
        LEGEND_caption += f"**🇮🇳 Telethon version :** `{version.__version__}`\n"
        LEGEND_caption += f"**🇮🇳 LEGENDBOT :**`{LEGENDversion}`\n"
        LEGEND_caption += f"**🇮🇳 Uptime :** `{uptime}`\n"
        LEGEND_caption += f"**🔱 Master:** {mention}\n"
        LEGEND_caption += f"**🔱 OWNER :** [LEGEND](t.me/Legend_Mr_Hacker)\n"
        LEGEND_caption += f"**┗━━━━━━━━━━━━━┛**\n"
        
        LEGEND_caption += " [✨REPO✨](https://github.com/LEGEND-OS/LEGENDBOT) 🔹 [📜License📜](https://github.com/LEGEND-OS/LEGENDBOT/blob/master/LICENSE)"
        await alive.client.send_file(
            alive.chat_id, LEGEND_IMG, caption=LEGEND_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"**┏━━━━━━━━━━━━━┓**\n"
            f"         __**𖤍BOT STATUS𖤍**__\n"
            f"**🇮🇳 Telethon Version :** `{version.__version__}`\n"
            f"**🇮🇳 LEGENDBOT:** `{LEGENDversion}`\n"
            f"**🇮🇳 Uptime :** `{uptime}`\n"
            f"**🔱 Master:** {mention}\n"
            f"**🔱 OWNER :** [LEGEND](t.me/Legend_Mr_Hacker)\n"
            f"**┗━━━━━━━━━━━━━┛**\n",
        )

CmdHelp("botstatus").add_command(
    'bot', None, 'Use and See'
).add()
