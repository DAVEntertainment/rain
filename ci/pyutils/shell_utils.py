"""
shell utils
"""
import shlex

from subprocess import Popen, PIPE
from platform import system

def run_cmd(cmd, **kwargs):
    """
    run cmd with log

    signature:
        run_cmd(cmd)

    params:
        cmd         command to execute
    """
    print(cmd)
    with Popen(
        cmd if system() == "Windows" else shlex.split(cmd),
        **kwargs
    ) as proc:
        proc.communicate()
        print(f"return code {proc.returncode}")
        return proc.returncode

def run_cmd_with_log(cmd, **kwargs):
    """
    run cmd with log

    signature:
        run_cmd_with_log(cmd)

    params:
        cmd         command to execute
    """
    print(cmd)
    with Popen(
        cmd if system() == "Windows" else shlex.split(cmd),
        stdout = PIPE, stderr = PIPE,
        shell = (system() == "Windows"),
        **kwargs
    ) as proc:
        stdout, stderr = proc.communicate()
        print(f"return code {proc.returncode}")
        return proc.returncode, stdout, stderr
