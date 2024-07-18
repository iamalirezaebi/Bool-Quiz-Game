from data import question_data
from question_model import Question

question_bank=[]
for Q in question_data:
    que_text = Q["text"]
    que_answer = Q["answer"]
    s = Question(que_text,que_answer)
    question_bank.append(s)

print(question_bank[7].answer)