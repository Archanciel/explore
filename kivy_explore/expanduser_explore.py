# importing os.path module
import os.path

# Path
path = "~/file.txt"

# Expand an intial ~ component
# in the given path
# using os.path.expanduser() method
full_path = os.path.expanduser(path)

print('NOW')

# print the path after
# expanding the intial ~ component
# in the given path
print(full_path)

# Change the value of
# HOME environment variable
os.environ["HOME"] = "/home / GeeksForGeeks"

# Now, Expand the intial ~ component
# in the same path
# using os.path.expanduser() method
full_path = os.path.expanduser(path)

# print the path after
# expanding intial ~ component
# in the given path
print(full_path)

# While expansion, An initial
# ~user component is looked
# up directly in the password directory.

# Path having an initial
# ~user component
path = "~ihritik / file.txt"

# Expand the intial ~user
# component in the given path
# using os.path.expanduser() method
full_path = os.path.expanduser(path)

# print the path after
# expanding the intial ~user
# component in the given path
print(full_path)