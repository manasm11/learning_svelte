import os
from collections import defaultdict

isImportStatement = lambda line: 'import ' in line and '.svelte' in line and ' from ' in line and './' in line

uses = defaultdict(list)

for root, dirs, files in os.walk('src'):
    for file in files:
        if '.svelte' in file:
            filepath = os.path.join(root, file)
            fname = file.split('.')[0].strip()
            with open(filepath) as f:
                for line in f.readlines():
                    line = line.strip()
                    if isImportStatement(line):
                        relativePath = line.split()[-1]
                        filename = relativePath.split('/')[-1]
                        componentName = filename.split('.')[0]
                        uses[fname].append(componentName.strip())

import json

with open('uses.json', 'w') as f:
    json.dump(uses, f, indent=4)