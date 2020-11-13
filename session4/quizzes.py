from pymongo import MongoClient

client = MongoClient('localhost', 27017)

quiz_database = client.get_database('quiz')

quizzes_collection = quiz_database.get_collection('quizzes')
score_collection = quiz_database.get_collection('scores')
# quizzes = pyexcel.get_records(file_name='quiz.xls')
quizzes = quizzes_collection.find()
total_quizzes = quizzes_collection.count_documents({})
# for quiz in quizzes:
#     quiz['choices'] = quiz['choices'].split(',')
#     quiz['choices'].pop(-1)
# print(quizzes[1]['choices'])

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

score = (count * 100) / total_quizzes
score_collection.insert_one({
    "name": "Duc",
    "score": score
})
