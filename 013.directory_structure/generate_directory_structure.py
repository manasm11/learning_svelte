import os
import json

def path_to_dict(path):
    d = {os.path.basename(path): []}
    if os.path.isdir(path):
        d[os.path.basename(path)] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    return d

print(json.dumps(path_to_dict('.'), indent=1))