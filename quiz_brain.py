class QuizBrain:

    score = 0

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list




    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer= input(f"Q{self.question_number}: {current_question.text}. (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        if len(self.question_list) == self.question_number:
            return False
        return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            QuizBrain.score += 1
            print (f'You got it right!')

        else:
            print(f'You are wrong.')
        print(f'The correct answer is {correct_answer}')
        print(f'Your score is {QuizBrain.score}/{self.question_number}')
        print('\n')





