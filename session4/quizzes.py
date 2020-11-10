quizzes = [
    {
        'question': 'Con chó có mấy chân?',
        'awnser': 3,
        'choices': [
            '2 chân', 
            '3 chân', 
            '1 chân', 
            '4 chân'
        ]   
    },
    {
        'question': 'Con vịt có mấy chân?',
        'awnser': 0,
        'choices': [
            '1 chân',
            '3 chân',
            '2 chân',
            '4 chân'
        ]
    }
]

print(quiz['question'])
for i in range(len(quiz['choices'])):
    print(f'{i+1}: {quiz["choices"][i]}')
use_choice = int(input('Enter correct position')) - 1
if use_choice == quiz['awnser']:
    print('correct!!')
else:
    print('wrong!!')