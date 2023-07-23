import openai


def talk_to_gpt(api_key, messages, model='gpt-3.5-turbo') -> str:
    openai.api_key = api_key
    serialized_msgs = [x.serialise for x in messages]
    response = openai.ChatCompletion.create(model=model, messages=serialized_msgs)
    return response.choices[0].message.content
    # return 'B.'
