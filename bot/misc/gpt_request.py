import g4f
from aiogram import types

from bot.db.methods.fetch import fetch

GPT_MODEL = {
    "gpt-3.5-turbo": "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k": "gpt-3.5-turbo-16k",
    "gpt-4": g4f.models.gpt_4
}


async def gpt_request(message: types.Message) -> str:
    """method that sends and receives a GPT request"""
    try:
        chat_id = message.chat.id
        message_text = message.text

        # query to get user gpt model from database
        fetch_gpt_model_query = """SELECT gpt_model FROM users WHERE chat_id = ?"""
        gpt_model = fetch(fetch_gpt_model_query, (chat_id,))[0][0]

        model = GPT_MODEL.get(gpt_model)

        response = g4f.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": message_text}],
            temperature=0.2,
            topp=0.1,
            n=1,
            provider=g4f.Provider.DeepAi,
        )

        result = "".join(response)

        return result

    except Exception as e:
        print(f"An error has occurred: {e}")
