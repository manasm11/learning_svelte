import os
from pprint import pprint
from collections import defaultdict
import re
import json

details = defaultdict(lambda: defaultdict(list))


def main():
    for component, filepath in svelte_files():
        details[component]
        for line in lines(filepath):
            if isImport(line):
                subComponent = extractComponentFromImport(line)
                details[component]['uses'].append(subComponent)
            elif isDispatch(line):
                eventName = extractEventName(line)
                details[component]['dispatches'].append(eventName)
            forwardedEvents = getForwardedEvents(line)
            if forwardedEvents:
                details[component]['forwards'].extend(forwardedEvents)
    calculateUsedBy()
    removeRedundancy()
    exportToJSON()

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

def extractComponentFromImport(line):
    relativePath = line.split()[-1]
    filename = relativePath.split('/')[-1]
    componentName = filename.split('.')[0]
    return componentName.strip()

def extractEventName(line):
    eventName = line.split('dispatch(')[1][1:]
    eventName = re.split("'|\"",eventName)[0].strip()
    return eventName

def calculateUsedBy():
    for componentToSearch in details:
        for component in details:
            if 'uses' in details[component].keys() and componentToSearch in details[component]['uses']:
                details[componentToSearch]['usedBy'].append(component)

def exportToJSON():
    with open('component_details.json', 'w') as f:
        json.dump(details, f, indent=4)

isImport = lambda line: 'import ' in line and '.svelte' in line and ' from ' in line and './' in line
isDispatch = lambda line: 'dispatch(' in line

def getForwardedEvents(line):
    events = []
    if ' on:' in line:
        for word in line.split():
            if 'on:' in word and not '=' in word:
                event = word.split(':')[1].strip()
                while event[-1] in '/>':
                    event = event[:-1]
                events.append(event)
    return events

def removeRedundancy():
    for component in details:
        for attribute, items in details[component].items():
            details[component][attribute] = list(set(items))

if __name__ == '__main__':
    main()