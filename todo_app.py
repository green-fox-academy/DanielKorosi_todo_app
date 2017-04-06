import sys

class ArgReader():
    def __init__(self):
        if len(sys.argv) == 1:
               print ("Python Todo application\n=======================\n\nCommand line arguments:\n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes an task\n-c   Completes an task")
        else:
            controller = sys.argv[1:]
            if controller[0] == '-l':
                self.list_tasks()
            if controller[0] == '-a':
                print("y")
            if controller[0] == '-r':
                print("z")
            if controller[0] == '-c':
                print("o")

    def list_tasks(self):
        x = open('database.txt', 'r')
        task_list = x.readlines()
        task_list = [i.replace('\n','') for i in task_list]
        task_list = [i.split('#') for i in task_list]

        for i in range (len(task_list)):
            if task_list[i][0] == '1':
                task_list[i][0] = '[x]'
            else:
                task_list[i][0] = '[ ]'
            print((i+1), '-', (task_list[i][0]), task_list[i][1])

print_usage = ArgReader()
