import os

def get_all_files(dirname):
    l = []
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            l.append(os.path.join(root, filename))
    return l


def search_dup(files_paths):
    d = dict()
    for path in files_paths:
        cmd = 'md5sum ' + path
        fp = os.popen(cmd)
        print('fp: ', fp)
        res = fp.read()
        r = res.split()
        key = r[0]
        d.setdefault(key, [])
        d[key].append(path)
    return d


list_of_files = get_all_files('/Users/conniecanelon/dev/chapter14')
print(search_dup(list_of_files))

"""
#Create a dict. 
#Keys: checksum of each file. Values: Path of each file. 
#If a file has the same checksum than other, the program should include the path as a value of that key.
"""