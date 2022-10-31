# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from vantexproject import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from vantexproject.helpers.misc import create_botlog, git, heroku

MSG_ON = """
🔥 **Vantex-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Owner :** [Vantex](https://t.me/phobiakaliann)
➠ **Channel :** [Validc0de](https://t.me/validc0de)
━━
**Ketik** `{}alive` **untuk Mengecheck Bot**
"""
PIC_ON = "https://telegra.ph/file/3d06084267acd8431b7b8.jpg"

async def main():
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("validc0de")
            await bot.join_chat("vantexub")
            try:
                await bot.send_photo(
                    BOTLOG_CHATID, photo=PIC_ON, caption=MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("ProjectMan").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("Vantex").info(f"Vantex-UserBot v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    if bot1 and str(BOTLOG_CHATID).startswith("-100"):
        bot1.me = await bot1.get_me()
        chat = await bot1.get_chat(BOTLOG_CHATID)
        desc = "Group Log untuk Vantex-UserBot.\n\nHARAP JANGAN KELUAR DARI GROUP INI.\n\n✨ Powered By ~ @validc0de ✨"
        lolo = f"LOGS | FOR {bot1.me.first_name}"
        if chat.description != desc:
            await bot1.set_chat_description(BOTLOG_CHATID, desc)
        if chat.title != lolo:
            await bot1.set_chat_title(BOTLOG_CHATID, lolo)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Vantex").info("Starting Vantex-UserBot")
    install()
    git()
    heroku()
    LOOP.run_until_complete(main())
