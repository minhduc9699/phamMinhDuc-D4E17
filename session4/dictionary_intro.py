person = ['Đức', 96, False, 'Sơn la', 'dev']

person = {
    'name': 'Đức', 
    'yob': 96, 
    'job_title': 'dev', 
    'name': 'not Đức',
}
print(person['name'])
# C R U D
# READ
# print(person['name'])
# READ ALL
name = person['name']
# Create
person['height'] = 175
# Update
person['Height'] = 180
# Delete
del person['Height']
if 'name' in person: # check if key exist
    print('key existed')
for key in person:
    print(key, person[key])
