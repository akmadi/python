'''
Created on Jan 3, 2018

@author: amadin001c
'''

import random
from asyncore import write

def main():
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New   Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West   Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    
    
    for x in range(35):
        quizFile = open('QuestionsQuiz%s.txt'%(x+1),'w')
        quizAnswers = open('QuizAnswers%s.txt'%(x+1),'w')
        quizFile.write("Name:\nRollNo:\nClass:\n")
        quizFile.write('Answer below questions:\n')
        states = list(capitals.keys())
        random.shuffle(states)
        print(states)
        
        for y in range(50):
            correctAnswer = capitals[states[y]]
            wrongAnswers = list(capitals.values())
            del wrongAnswers[wrongAnswers.index(correctAnswer)]
            wrongAnswers = random.sample(wrongAnswers,3)
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)
        quizFile.write('%s. What is the capital city of %s \n '%(x+1,states[x]))    
        for z in range(4):
            quizFile.write('%s. %s\n'% ('ABCD'[z],answerOptions[z]))



if __name__ == '__main__':
    main()