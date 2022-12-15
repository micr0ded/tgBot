from pyrogram import Client, filters
from pyrogram.enums import ParseMode, ChatType


from tg_userbot.brain import brain, auth_data


def shitty_speaking() -> None:
    app = Client(name="my_acc",
                 api_id=auth_data.API_ID,
                 api_hash=auth_data.API_HASH,
                 phone_number=auth_data.PHONE_NUMBER,
                 parse_mode=ParseMode.HTML)

    @app.on_message(filters.incoming & filters.text & filters.chat(-1001494269417))
    async def speak(client, message):
        brain.do_kek(client, message, app)

