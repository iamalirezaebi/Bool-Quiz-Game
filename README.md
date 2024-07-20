# Bool-Quiz-Game
the very first part is that this quiz game is an oop project that we create objects unlike the previous project(coffee machine) 
the project consists of four different files:
#### data.py:
  this file contains the questions with their answer in true and false text mode 
#### main.py:
  in this file we convert our dictionary from the other file(data.py) to class object and append them to a list 
  for further developements of preoject
#### question_model.py
  in this file i defined a class named Question and initialised two objects in it; first one is text that represents the   question declaration and the second one is answer that contains answers of the questions in True/False(Boolean) format.
#### quiz_brain.py
  several functions are definerd in this class; at first we initialised question number and score and putheir value        equal to zero; then still_has_questions was initialised to compare the length of question_list with question_number
  next question funzction was defined to move to next question after finishing this level, and check_answer function       lowercases our user's answer and compares it with the right answer.
