import os
from collections import defaultdict

details = defaultdict(lambda: {
    "uses": []
})


def main():
    for component, filepath in svelte_files():
        print(component, filepath)
        for line in lines(filepath):
            if isImportStatement(line):
                subComponent = extractComponentFromImportStatement(line)
                details[component]['uses'].append(subComponent)

def svelte_files(directory='src'):
    for root, _, files in os.walk('src'):
        for file in files:
            if '.svelte' in file:
                file = file.strip()
                yield file.split('.')[0] ,os.path.join(root, file)

def lines(filepath):
    with open(filepath) as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) > 2:
                yield line

def extractComponentFromImportStatement(line):
    relativePath = line.split()[-1]
    filename = relativePath.split('/')[-1]
    componentName = filename.split('.')[0]
    return componentName.strip()

isImportStatement = lambda line: 'import ' in line and '.svelte' in line and ' from ' in line and './' in line

if __name__ == '__main__':
    main()
    print(details)