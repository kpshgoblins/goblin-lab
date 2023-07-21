import openai
import uuid
from .question import Question

class Interview(object):
    def __init__(self,
                 interview_id: str = None,
                 api_key: str = None,
                 model: str = 'gpt-3.5-turbo'):
        self.api_key = api_key
        self.model = model

        if not interview_id:
            self.interview_id = self.generate_interview_id()
            self.messages = [self.get_system_message()]
        else:
            self.interview_id = interview_id
            self.messages = self.load_history()

    def generate_interview_id(self) -> str:
        return str(uuid.uuid4())

    def load_history(self) -> list:
        # TODO
        return []

    def get_system_message(self) -> dict:
        return {'role': 'system',
                'content': 'Helpful assistant.'}

    def get_interview_initial_message(self) -> str:
        return 'Please introduce one of your projects.'

    def get_next_question(self) -> Question:
        # TODO this is Pseudo logic
        return Question("", self.interview_id)

    def submit_answer(self, submission):
        pass
