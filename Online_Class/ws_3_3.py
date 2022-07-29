infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

count = 0
for info in infos:
    count += info.get('age')

print(count)