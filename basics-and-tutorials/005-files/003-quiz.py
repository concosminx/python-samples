questions = open('003-questions.txt', 'r')
question_list = [line.strip() for line in questions.readlines()]
questions.close()

score = 0   
total = len(question_list)      

for line in question_list:
    q, a = line.split('=')  
    ans = input('{}='.format(q)) #ask the question
    if a == ans:    #check the answer
        score += 1  #if ok, increase the score

result = open('003-result.txt', 'w')    
result.write('Your final score is {}/{}.'.format(score, total))     # write final score to result.txt
result.close()