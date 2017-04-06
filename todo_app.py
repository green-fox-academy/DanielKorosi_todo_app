import sys

class ArgReader():
    def __init__(self):
        if len(sys.argv) == 1:
               print ("Python Todo application\n=======================\n\nCommand line arguments:\n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes an task\n-c   Completes an task")
        else:
            self.controller = sys.argv[1:]
            if self.controller[0] == '-l':
                self.listing()
            if self.controller[0] == '-a':
                self.add_new()
            if self.controller[0] == '-r':
                print("z")
            if self.controller[0] == '-c':
                print("o")

    def read(self):
        self.task_list = open('database.txt', 'r')
        task_list = self.task_list.readlines()
        task_list = [i.replace('\n','') for i in task_list]
        task_list = [i.split('#') for i in task_list]
        return task_list
        self.x.close

    def listing(self):
        self.task_list = self.read()
        if len(self.task_list) == 0:
            print('No todos for today! :)')
        else:
            for i in range (len(self.task_list)):
                if self.task_list[i][0] == '1':
                    self.task_list[i][0] = '[x]'
                else:
                    self.task_list[i][0] = '[ ]'
                print((i+1), '-', (self.task_list[i][0]), self.task_list[i][1])

    def add_new(self):
        self.new_member = open("database.txt", "a")
        self.new_member.write(('0#' + str(self.controller[1])+'\n'))
        self.new_member.close()

example = ArgReader()
