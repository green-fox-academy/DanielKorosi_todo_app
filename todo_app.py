import sys

class arg_reader():
    def __init__(self):
        if len(sys.argv) == 1:
               print ("Python Todo application\n=======================\n\nCommand line arguments:\n-l   Lists all the tasks\n-a   Adds a new task\n-r   Removes an task\n-c   Completes an task")

print_usage = arg_reader()
