import subprocess
import sys

packages = "./requirements.txt"
subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', packages])