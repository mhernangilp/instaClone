import subprocess

o = subprocess.run('ls', shell=True, capture_output=True)
sol = o.stdout.decode()
print(sol)
