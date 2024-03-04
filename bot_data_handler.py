def load_from_file():
    phonebook = {}
    try:
        with open("phonebook.txt", "r") as f:
            data = f.read()
            if data != "":
                lines = data.split("\n")
                for line in lines:
                    if line != "" and ":" in line:
                        line = line.split(":")
                        phonebook.update({line[0].strip(): line[1].strip()})
            else:
                print(Logger.empty())
        if phonebook == {}:
            print(Logger.empty())
    except FileNotFoundError:
        print(Logger.not_found())
    return phonebook


def save_to_file(data):
    output = ""
    for k, v in data.items():
        output += f"{k}: {v}\n"
    output = output.removesuffix("\n")
    with open("phonebook.txt", "w") as f:
        f.write(output)
    return print()


class Logger:
    def empty():
        return "\33[90m[INFO]: Phonebook file found, but it's empty for now.\x1b[0m"

    def not_found():
        return "\33[90m[INFO]: Phonebook file not found, but don't worry, I'll create a new one for you.\x1b[0m"
