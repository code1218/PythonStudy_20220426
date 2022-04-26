a = dict()
print(type(a))

a['name'] = 'python'
a[('a',)] = 'python'
a[[1]] = 'python' #키 값이 변경이 안됨
a[250] = 'python'

print(a)