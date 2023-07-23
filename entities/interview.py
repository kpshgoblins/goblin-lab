import uuid
import os
from .question import Question
from dotenv import load_dotenv
from .chat import talk_to_gpt

load_dotenv()
init_question = os.getenv('init_question')

intro_tail_prompt = "Can you ask a technology question based on the above description? " \
                    "And please don't ask anything already provided. " \
                    "Please only give me the question content without any interactive words." \
                    "And I only want one question."

answer_tail_prompt = "Can you check if the above answer to the above question is right?" \
                     "If it's perfect, please give me A without any interactive words." \
                     "If the answer contains partially incorrect statements, please give me B without any interactive words." \
                     "If the most of the statements are wrong, please give me F without any interactive words."

new_question_prompt = "Can you please ask a technology question based on the above conversation?" \
                      "Please don't ask duplicate questions in this conversation." \
                      "Please only give me the question content without any interactive words." \
                      "And I only want one question."

challenge_question_prompt = "Can you please challenge one of the wrong parts from the above answer to the above question?" \
                            "If the answer is wrong and there is no need to challenge, please give me a single word F without any interactive words." \
                            "Please don't ask duplicate questions in this conversation." \
                            "Please only give me the question content without any interactive words." \
                            "And I only want one question."


class Interview(object):
    def __init__(self,
                 interview_id: str = None,
                 api_key: str = None,
                 model: str = 'gpt-3.5-turbo'):
        self.api_key = api_key
        self.model = model

        if not interview_id:
            self.interview_id = self.generate_interview_id()
            self.questions = self.load_init_msg()
        else:
            self.interview_id = interview_id
            self.questions = self.load_hist_msg()

    def generate_interview_id(self) -> str:
        return str(uuid.uuid4())

    def load_hist_msg(self) -> dict:
        # TODO
        return {}

    def load_init_msg(self) -> dict:
        init_q = Question(question_seq=1,
                          question_body=init_question)
        init_q.append_message(role="system",
                              message="You're an interviewer who will interview software engineering candidates")
        return {1: init_q}

    def get_latest_question_seq(self):
        # print("current question length: {}".format(len(self.questions)))
        return len(self.questions)

    def get_latest_question(self) -> Question:
        return self.questions.get(self.get_latest_question_seq())

    def get_all_conversation_history(self) -> list:
        conv = []
        for key in sorted(self.questions.keys()):
            conv.extend(self.questions.get(key).messages)
        return conv

    def generate_next_question(self):
        next_q_seq = self.get_latest_question_seq() + 1
        next_q = Question(question_seq=next_q_seq)
        self.questions[next_q_seq] = next_q

    def submit_answer(self, submission):
        if int(submission['question_seq']) != self.get_latest_question().question_seq:
            raise Exception("question_seq_error")

        answer = str(submission['answer'])
        self.get_latest_question().answer_question(answer)
        self.get_latest_question().append_message(role="user",
                                                  message="Question: {}\n"
                                                          "Answer: {}\n"
                                                  .format(self.get_latest_question().question_body, answer))
        self.get_latest_question().append_message(role="system",
                                                  message=answer_tail_prompt)

        for m in self.get_all_conversation_history():
            print(m.serialise)

        # TODO process gpt response and do further engineering work
        gpt_response_msg = talk_to_gpt(self.api_key, self.get_all_conversation_history())
        print(gpt_response_msg)
        # TODO maybe there is better way for this piece of logic
        if gpt_response_msg in ['A.', 'A', 'a.', 'a']:
            self.generate_next_question()
            self.get_latest_question().append_message('system', new_question_prompt)
        elif gpt_response_msg in ['B.', 'B', 'b.', 'b']:
            if self.get_latest_question().back_n_forth < 3:
                self.get_latest_question().append_message(role="user",
                                                          message="Question: {}\n"
                                                                  "Answer: {}\n"
                                                          .format(self.get_latest_question().question_body, answer))
                self.get_latest_question().append_message('system', challenge_question_prompt)
            else:
                self.generate_next_question()
                self.get_latest_question().append_message('system', new_question_prompt)
        else:
            self.generate_next_question()
            self.get_latest_question().append_message('system', new_question_prompt)

        gpt_response_msg = talk_to_gpt(self.api_key, self.get_all_conversation_history())
        self.get_latest_question().set_question_body(gpt_response_msg)
