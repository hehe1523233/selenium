import subprocess


def run():
    p = subprocess.Popen(f"pytest -s", shell=True, stdout=subprocess.PIPE)
    res = str(p.stdout.read(), encoding='utf-8')
    print(res)


if __name__ == '__main__':
    run()