import pyexcel

quizzes = [
    {
        'question': 'Con cò có mấy chân?',
        'awnser': 3,
        'choices': [
            '2 chân',
            '3 chân',
            '1 chân',
            '4 chân'
        ]
    },
    {
        'question': 'Con mèo có mấy chân?',
        'awnser': 2,
        'choices': [
            '1 chân',
            '3 chân',
            '2 chân',
            '4 chân'
        ]
    }
]

for quizz in quizzes:
    choice_string = ''
    for choice in quizz['choices']:
        choice_string = choice_string + choice + ','
    quizz['choices'] = choice_string
    print(choice_string)
pyexcel.save_as(records=quizzes, dest_file_name='quiz.xls')