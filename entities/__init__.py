import uuid
import collections
class Question(object):
    # persist?
    question_seq_dict = collections.defaultdict(list)

    @classmethod
    def generate_question_seq(cls, interview_id):
        return len(cls.question_seq_dict[interview_id])
        
    @classmethod
    def get_question(cls, interview_id, question_seq):

        questions = cls.question_seq_dict[interview_id]
        return questions[question_seq] if len(questions) > question_seq else None

    def __init__(self, question_body:str, interview_id:str = None):
        self.interview_id = interview_id if interview_id else str(uuid.uuid4())
        self.question_seq = self.generate_question_seq(self.interview_id)
        self.question_body = question_body
        self.answer = None
        self.question_seq_dict[self.interview_id].append(self)
    
    @classmethod
    def answer_question(cls, interview_id, question_seq, answer):
        cls.get_question(interview_id, question_seq).answer = answer
