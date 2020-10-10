import os
import json
from pathlib import Path, PurePath

STATE_FILE = ".optimize_queue.json"

def save_state_to_file(commands):
    with open(STATE_FILE, "w") as f:
        contents = {
            "commands": commands
        }
        f.write(json.dumps(contents))

def get_commands_queue():
    with open(STATE_FILE, 'r') as f:
        state_file_contents = json.loads(f.read())
        return state_file_contents['commands']

def setup_optimize_list():
    commands_queue = get_command_list()
    save_state_to_file(commands_queue)
    complete_task()


def complete_task():
    commands_queue = get_commands_queue()
    while len(commands_queue) > 0:
        command = commands_queue.pop(0)
        os.system(command)
        save_state_to_file(commands_queue)


def get_command_list():
    optimize_Command_list = []
    queue = []
    cwd = '.'
    for root, dirs, files in os.walk(cwd):
        for name in dirs:
            queue.append(name)
    # print(queue)
    p = Path("./optimized")
    p.mkdir(parents=True, exist_ok=True)
    for item in queue:
        if item == 'optimized':
            continue
        print("Looking in folder ", item)
        new_p = Path(PurePath.joinpath(p, item))
        new_p.mkdir(parents=True, exist_ok=True)
        for root, dirs, files in os.walk(os.path.join(cwd, item)):
            for name in files:
                if name.endswith(".mp4"):
                    org_f = os.path.join(root, name)
                    new_f = PurePath.joinpath(new_p, name)
                    # print("video: "+new_f)
                    # Path.touch(new_f, exist_ok=True)
                    command = """ffmpeg -i '%s' -vcodec libx265 -crf 28 -preset fast '%s'""" % (org_f, new_f)
                    # print(command)
                    optimize_Command_list.append(command)
    return optimize_Command_list
    

if __name__ == '__main__':
    if os.path.isfile(STATE_FILE):
        complete_task()
    else:
        setup_optimize_list()
