from .. import BotzHub
from telethon import events, Button

SMEX_USER = [1809900087]

@BotzHub.on(
    events.NewMessage(pattern="^/remove ?(.*)")
)
async def _(event):
  if event.sender_id in SMEX_USER:
    await bot.send_message(event.chat_id, "SEMX DONE NOW TAKE REST", buttons=Button.clear())
  else:
    await event.reply("**BHAI YAAR THUM GAAND MARAO**")
