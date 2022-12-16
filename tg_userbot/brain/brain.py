import random
import re


async def brain(client, message, app):
    text = message.text.lower()
    if message.from_user.id != 588675218:
        text_split = text.split()[-1]
        lex = re.findall(r"(?:[0,)])+", text_split)
        if len(lex) > 0:
            answer = lex[-1]
            print(answer)
            await app.send_message(message.chat.id, answer)

    if random.randint(0, 10) < 1:
        text_da = text.split("да")
        if len(text_da) > 1:
            answer = "Пизда"
            if len(text_da[1]) > 1:
                answer += text_da[1].split()[0]
            await app.send_message(message.chat.id, answer)

    if random.randint(0, 100) < 1:
        await app.send_message(message.chat.id, "/summary")