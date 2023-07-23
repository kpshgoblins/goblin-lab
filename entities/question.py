from .message import Message


class Question:

    def __init__(self, question_seq: int, question_body: str = None):
        self.question_seq = question_seq
        self.question_body = question_body
        self.messages = []
        self.answer = None
        self.back_n_forth = 0

    def set_question_body(self, question_body):
        self.question_body = question_body

    def answer_question(self, answer):
        self.answer = answer
        self.back_n_forth += 1

    def append_message(self, role, message):
        self.messages.append(Message(role=role, content=message))

    @property
    def serialise(self):
        return {'question_seq': str(self.question_seq),
                'question_body': str(self.question_body),
                'answer': str(self.answer)}
