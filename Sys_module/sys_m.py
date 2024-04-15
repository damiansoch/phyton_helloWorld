import sys

# run it from terminal -> python Sys_module\sys_m.py damiansoch dsadsa

print(sys.path)
print(sys.argv)

if len(sys.argv) < 3:
    raise IOError("Not all args provided")

# username = sys.argv[1]
# password = sys.argv[2]

_, username, password = sys.argv

print(f"Username: {username}\n"
      f"Password: {password}")

print(sys.version_info)
print(sys.version)
