# from entities import talk_to_gpt
import openai
import sys


def talk_to_gpt(api_key, messages, model='gpt-3.5-turbo') -> str:
    # openai.api_key = api_key
    response = openai.ChatCompletion.create(model=model, messages=messages)
    return response.choices[0].message.content


ak = str(sys.argv[1])
intro_tail_prompt = "Can you ask a technology question based on the above description? " \
                    "And please don't ask anything already provided. " \
                    "Please only give me the question content without any interactive words." \
                    "And I only want one question."
msg = {"role": "user",
       "content": "My project is written in Java and SpringBoot as a RESTful service\n" + intro_tail_prompt}
gpt_answer = talk_to_gpt(api_key=ak,
                         messages=[msg])
print(gpt_answer)


answer_tail_prompt = "Can you check if the above answer to the above question is right?" \
                     "If it's perfect, please give me A without any interactive words." \
                     "If the answer contains partially incorrect statements, please give me B without any interactive words." \
                     "If the most of the statements are wrong or irrelevant, please give me F without any interactive words."

msg1 = {"role": "user",
        "content": "Question: Can you list some primitive types in Java language?\n"
                   "Answer: It's used to display html\n" + answer_tail_prompt}
gpt_answer = talk_to_gpt(api_key=ak,
                         messages=[msg1])

print(gpt_answer)


msg2 = {"role": "user",
        "content": "Question: Can you list some primitive types in Java language?\n"
                   "Answer: int, float, double, String\n" + answer_tail_prompt}
gpt_answer = talk_to_gpt(api_key=ak,
                         messages=[msg2])

print(gpt_answer)


msg3 = {"role": "user",
        "content": "Question: Can you list some primitive types in Java language?\n"
                   "Answer: int, byte, short, long, float, double, boolean and char\n" + answer_tail_prompt}
gpt_answer = talk_to_gpt(api_key=ak,
                         messages=[msg3])

print(gpt_answer)