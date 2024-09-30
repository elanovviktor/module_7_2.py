
def  custom_write(file_name, strings):
    ban = {}
    file = open(file_name, 'a', encoding='utf-8')
    nm = 1

    for i in strings:
        cur_tell = file.tell()
        file.write(f'{i}\n')
        ban.update({(nm, cur_tell) : i})
        nm += 1
    file.close()
    return ban

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

