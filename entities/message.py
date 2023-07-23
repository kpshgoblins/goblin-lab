import json


class Message(object):

    def get_gpt_message(self):
        return json.dump(self)

    def set_message(self, message):
        self.content = message

    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    @property
    def serialise(self):
        return {'role': self.role,
                'content': self.content}
