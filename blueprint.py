import questions
questions_data = questions.question_data
class question:
    no_of_ques = 0
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        question.no_of_ques += 1
    

#creates a list of objects of question class
loq = []

for i in range (len(questions_data)):
    loq.append(question(questions_data[i]["text"], questions_data[i]["answer"]))