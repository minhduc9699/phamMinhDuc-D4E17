import pyexcel

quizzes = pyexcel.get_records(file_name='quiz.xls')
for quiz in quizzes:
    quiz['choices'] = quiz['choices'].split(',')
    quiz['choices'].pop(-1)
print(quizzes[1]['choices'])

count = 0 
for quiz in quizzes:
    print(quiz['question'])
    for i in range(len(quiz['choices'])):
        print(f'{i+1}: {quiz["choices"][i]}')
    use_choice = int(input('Enter correct position')) - 1
    if use_choice == quiz['awnser']:
        print('correct!!')
        count = count + 1
    else:
        print('wrong!!')

score = (count * 100) / len(quizzes)
print(f'your score is {score}%')