import subprocess

result = subprocess.run(
    "brew info azure-cli",
    shell=True,
    capture_output=True,
    text=True)

print(f"result: {result}")
print(f"return code: {result.returncode}")

print(result.stdout)

