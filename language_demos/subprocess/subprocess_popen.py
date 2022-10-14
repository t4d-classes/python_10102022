import subprocess

p = subprocess.Popen(
    "brew info azure-cli",
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT, shell=True)

retval = p.wait()
print(retval)

if p and p.stdout:
    for line in p.stdout.readlines():
        print(str(line, "UTF-8"))

