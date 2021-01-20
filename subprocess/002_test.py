# test piping

import subprocess

p1 = subprocess.run(['cat', 'log.txt'], capture_output=True,
                    text=True, check=True)
# print(p1.stdout)

p2 = subprocess.run(['grep', '-in', 'randomfighter.py'], capture_output=True,
                    text=True, check=True, input=p1.stdout)
print(p2.stdout)
