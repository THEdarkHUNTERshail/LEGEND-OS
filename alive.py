from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

hell_pic = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
alive_c = f"__**🔥🔥LegendBot ɨs օռʟɨռɛ🔥🔥**__\n\n"
alive_c += f"__↼ Øwñêr ⇀__ : 『 {ALIVE_NAME} 』\n\n"
alive_c += f"•♦• Telethon     :  `{version.__yversion__}` \n"
alive_c += f"•♦• LegendBot      :  __**{LEGENDversion}**__\n"
alive_c += f"•♦• Channel      :  https://tele.me/Legend_Userbot\n"

#-------------------------------------------------------------------------------

@bot.on(hell_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(event):
    if hell.fwd_from:
        return
    await event.get_chat()
    await event.delete()
    await bot.send_file(event.chat_id, LEGEND_pic, caption=alive_c)
    await event.delete()

msg = f"""
**⚡ LEGENDBOT ιѕ σиℓιиє ⚡**
{Config.ALIVE_MSG}
**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**Telethon :**  `{version.__version__}`
**Legend  :**  **{LEGENDversion}**
**Uptime   :**  `{uptime}`
**Sudo      :**  **{is_sudo}**
"""
botname = Config.TG_BOT_USERNAME_BF_HER

@bot.on(admin_cmd(pattern="boot$"))
@bot.on(sudo_cmd(pattern="boot$", allow_sudo=True))
async def hell_a(event):
    try:
        event = await bot.inline_query(botname, "alive")
        await event[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "hell", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
