class Question:
    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer


class Exam:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question):
        self.questions.append(question)

    def start(self):
        for q in self.questions:
            answer = input(q.text + " ")
            if answer.lower() == q.correct_answer.lower():
                self.score += 1

    def result(self):
        return f"Natija: {self.score}/{len(self.questions)}"


exam = Exam()
exam.add_question(Question("Python qaysi til? ", "dasturlash"))
exam.add_question(Question("def nima? ", "funksiya"))

exam.start()
print(exam.result())
