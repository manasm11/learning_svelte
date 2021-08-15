import os

for root, dirs, files in os.walk('src'):
    for file in files:
        if '.svelte' in file:
            filepath = os.path.join(root, file)
            componentName = file.split('.')[0]
            with open(filepath) as f:
                for line in f.readlines():
                    if '@debug' in line:
                        print(filepath)
                        break 