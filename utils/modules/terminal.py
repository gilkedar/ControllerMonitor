import subprocess


class Terminal:

    def __init__(self):
        pass

    def run(self, command):
        cmd = command.split()
        output_str = ""
        try:
            output, err = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
            output_str = output.decode()
        except Exception as ex:
            print(ex)
        return output_str


if __name__ == '__main__':
    t = Terminal()
    ans = t.run("lsusb")
    print(ans)