todos = open('todos.txt','a')

print('put out the trash', file = todos)
print('feed the cat', file = todos)
print('prepare task return',file= todos)
todos.close()
task = open('todos.txt')
for chore in task:
    print(chore,end='')
task.close()

with open ('todos.txt') as task:
    for chore in task:
        print(chore, end= '')
