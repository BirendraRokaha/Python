import subprocess

# runs inline
subprocess.run('neofetch')

# Store in var
p1 = subprocess.run(['ls', '-la'], capture_output=True)
p2 = subprocess.run(['uname', '-a'], capture_output=True, text=True)
p3 = subprocess.run(['du', '-hc'], stdout=subprocess.PIPE,
                    text=True, check=True)

# print the arguments
print(p1.args)

# if 0 -> no error
print(p1.returncode)

# display in bytes
# print(p1.stdout)
print(p1.stdout.decode())

print('')
print(p2.stdout)

print('')
print(p3.stdout)


# pipe to a file
with open('log.txt', 'w') as f:
    p4 = subprocess.run(['ls', '-lRa', '/home/biren/Desktop'],
                        stdout=f, text=True, check=True)


# print error
# check=True gives python error
p5 = subprocess.run(['ls', '-lRa', '~/Desktop'],
                    capture_output=True, text=True, check=True)
print(p5.stderr)

# Ignore error
p6 = subprocess.run(['ls', '-lRa', '~/Desktop'], 
                    stderr=subprocess.DEVNULL)

print(p6.stderr)
