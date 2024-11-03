immutable_tuple = ('11', '22.0', 'string', False, '[3, B, C]' ) # пункт 2
print(immutable_tuple)

# immutable_tuple [2] = 333    # попытка изменить кортеж(неизменяемый тип данных)
# print(immutable_tuple)



mutable_list = ['1', '2', 'green', True, [4, 5, 6]]  # пункт 4

mutable_list[3] = False
mutable_list.append('sky')
mutable_list.remove('1')
mutable_list.extend(['book', 7])

print(mutable_list)
