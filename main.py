from flask import Flask
from entities import Interview, Question


app = Flask(__name__)


def preload_question_categories():
    """
        Define some pre-configuration to control the overall prompt process
    :return:
    """
    return dict()


question_dict = preload_question_categories()
interview_dict: dict[str, Interview] = dict()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/start-interview")
def start_interview():
    """
        implement the interview starting process, NO openai call
        1. Construct the starting prompt which is static
        2. Log or save the event to file / DB
    :return:
        {
        "interview_id": "xxxx-xxxx-xxxx",
        "question_seq": "1",
        "question_body": "please briefly introduce a project you worked on"
        }
    """
    interview = Interview()
    interview_dict[interview.interview_id] = interview
    return interview.get_next_question()


@app.route("/interviewee-submit")
def interviewee_submit(submission):
    """
        implement the interviewee submission process
        1. Receive the submission from interviewee
            1.1 Need to pay attention to hack answers, e.g. people try to ask gpt instead of answering it
                We need to detect this and reject the answer.
        2. Construct the chat api prompt
        3. Call chat api and get response
        4. Extract UI response and return
    :param submission:
        {
        "interview_id": "xxxx-xxxx-xxxx",
        "question_seq": x,
        "question_body": "the body text",
        "answer": "the answer text",
        }
    :return:
        {
        "interview_id": "xxxx-xxxx-xxxx",
        "question_seq": "y",
        "question_body": "the body text"
        }
    """
    if not submission['interview_id']:
        raise Exception('invalid interview id')
    interview = interview_dict.get(submission['interview_id'])
    interview.submit_answer(submission)
    return interview.get_next_question()


@app.route("/end-interview")
def end_interview(interview_id):
    """
        implement the interview ending process, NO openai call
        1. Construct the ending prompt which is static
        2. Calculate the ranking or score of the interview result
        3. Log or save the event to file / DB
    :param interview_id: integer
    :return:
        {
        "interview_id": "xxxx-xxxx-xxxx",
        "question_seq": x,
        "question_body": "Interview is finished......"
        }
    """
    end_prompt = dict()
    return end_prompt


@app.route("/generate-avatars")
def generate_avatars():
    """
        call the DALL.E api to randomly generate 2 avatars, one for interviewee the other for the bot
    :return:
        {
        "interview_id": "xxxx-xxxx-xxxx",
        "avatar1": xxx,
        "avatar2": xxx
        }
    """
    avatars = dict()
    return avatars


@app.route("/interview-result")
def interview_result():
    """
        some admin users will call this api to get results and scores of interviews
    :return:
        [
            {
            "interview_id": "xxxx-xxxx-xxxx",
            "avatar1": xxx,
            "avatar2": xxx,
            "total_score": xxx,
            "details": [
                {
                "question_seq": n,
                "question_body": "xxx",
                "answer": "xxx",
                "score/ranking": "xxx"
                },
                {...}
            ]
            }
        ]
    """
    result = dict()
    return result


@app.route("/resume-interview")
def resume_interview(interview_id):
    """
        When the conversation is lost from the UI, call this API to resume
    :param interview_id: integer
    :return: [
                {
                "question_seq": n,
                "question_body": "xxx",
                "answer": "xxx",
                "score/ranking": "xxx"
                },
                {...}
            ]
    """

    result = dict()
    return result