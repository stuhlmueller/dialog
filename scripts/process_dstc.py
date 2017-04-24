import os
import os.path as path

def process_datum(datum):
    for line in datum.split("\n"):
        messages = line.split("\t")
        assert len(messages) in (1, 2)
        user_message = messages[0]
        yield "U: MSG " + user_message[user_message.index(" ") + 1:].strip()
        if len(messages) == 2:
            yield "A: MSG " + messages[1].strip()

def process_data(data):
    for datum in data:
        yield "\n".join(process_datum(datum))

def main():
    root_path = path.abspath(path.join(path.dirname(path.realpath(__file__)), os.pardir))
    data_path = path.join(root_path, "data/dialog-babi-task6/")
    f = open(path.join(data_path, "dialog-babi-task6-dstc2-dev.txt"))
    data = f.read().strip().split("\n\n")
    f.close()
    output = "\n\n".join(process_data(data))
    f = open(path.join(data_path, "dialog-babi-task6-dstc2-dev-workspace.txt"), "w")
    f.write(output)
    f.close()

main()