import os

for root, dirs, files in os.walk("路径"):
    for dirs in dirs:
        print(os.path.join(root,dirs))
    for file in files:
        print(os.path.join(root, file))
