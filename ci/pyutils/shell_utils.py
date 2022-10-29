from subprocess import Popen

def run_cmd(cmd):
    print(cmd)
    with Popen(cmd) as proc:
        proc.communicate()
        print(f"return code {proc.returncode}")
