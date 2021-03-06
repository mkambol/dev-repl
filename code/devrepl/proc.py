import subprocess
import devrepl.console_output as out
import os

def cmd(cmd, wd=os.getcwd(), display=True, stdout=subprocess.PIPE, stderr=None, shell=False):
    if display:
        out.info(wd)
        out.print_command(' '.join(cmd))

    output = subprocess.Popen(cmd,
                              stdout=stdout,
                              cwd=wd)
    return output.communicate()
