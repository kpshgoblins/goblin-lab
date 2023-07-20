import unittest
# hack
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
print(sys.path)
from entities import Question
class TestEntities(unittest.TestCase):
    
    def setUp(self) -> None:
        self.first_question = Question('what is your name')
        return super().setUp()



    def test_questions(self):
        second_question = Question('how old are you', self.first_question.interview_id)
        
        self.assertTrue((second_question.question_seq - self.first_question.question_seq) == 1 )
        self.assertEquals(self.first_question.interview_id, second_question.interview_id)

        self.assertTrue(self.first_question.answer is None)
        Question.answer_question(self.first_question.interview_id, self.first_question.question_seq, 'My name is Phil')
        self.assertTrue(self.first_question.answer == 'My name is Phil')


if '__main__' == __name__:
    unittest.main()