import os
from collections import defaultdict
import re

dispatches = defaultdict(set)

for root, dirs, files in os.walk('src'):
    for file in files:
        if '.svelte' in file:
            filepath = os.path.join(root, file)
            componentName = file.split('.')[0]
            with open(filepath) as f:
                for line in f.readlines():
                    if 'dispatch(' in line:
                        eventName = line.split('dispatch(')[1][1:]#[2:].split(')')[:-1].strip()
                        eventName = re.split("'|\"",eventName)[0].strip()
                        dispatches[componentName].add(eventName)

import json
for k in dispatches:
    dispatches[k] = list(dispatches[k])
with open('dispatches.json', 'w') as f:
    json.dump(dispatches, f, indent=4)