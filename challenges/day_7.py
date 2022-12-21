from pprint import pprint


class FileSystem:
    def __init__(self) -> None:
        self.filesystem = {}

    def show(self):
        pprint(self.filesystem)

    def cd(self, dir):
        if dir == '..':
            pass
        else:
            self.current_node = dir
            self.filesystem[dir] = []

    def ls(self):
        pass

def is_command(command):
    return command.startswith('$')

with open('data/day-7-test.csv') as f:
    commands = f.read().split('\n')

fs = FileSystem()

for command in commands:
    if is_command(command):
        action = command.split(' ')[1]
        if action == 'cd':
            directory = command.split(' ')[-1]
            fs.cd(directory)
        elif action == 'ls':
            pass

fs.show()
