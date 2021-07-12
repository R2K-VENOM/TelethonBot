from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/alive"))
async def alibe(event):
  SMEX_PIC = "https://telegra.ph/file/3979593187378b2b54057.jpg"
  but = [[Button.url("Mʏ ᴍᴀsᴛᴇʀ »»", "t.me/R2K_VENOM")]]
  pm_caption = """
•♦• **𝖨'𝖬 𝖠𝖫𝖨𝖵𝖤 𝖠𝖭𝖣 𝖱𝖤𝖠𝖣𝖸 𝖳𝖮 𝖲𝖤𝖬𝖷**
"""
  await BotzHub.send_file(event.chat_id, file=SMEX_PIC, caption=pm_caption, buttons=but, link_preview=False)
