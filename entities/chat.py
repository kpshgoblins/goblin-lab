import openai


def talk_to_gpt(api_key, messages, model='gpt-3.5-turbo') -> str:
    openai.api_key = api_key
    response = openai.ChatCompletion.create(model=model, messages=messages)
    return response.choices[0].message.content
