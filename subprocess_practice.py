import os
import subprocess

def function(**args):
    print(type(args))


os.chdir('/')
#subprocess.call(['ls', '-lrt'])

test_command=['ls', '-a']
#subprocess.call([*test_command])
print(type(test_command))
print(type([*test_command]))
#subprocess.call(test_command)
function()
