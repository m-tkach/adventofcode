import sys
from iparser import read_input


class FS_Dir:
    def __init__(self, dir_name, parent_dir=None):
        self.dir_name = dir_name
        self.parent_dir = parent_dir
        self.subdirs = {}
        self.files = {}
        self.total_filesize = 0

    def add_file(self, fn, fs):
        if fn not in self.files:
            self.files[fn] = fs
            self.total_filesize += fs

    def add_subdir(self, d):
        self.subdirs[d.get_name()] = d

    def get_name(self):
        return self.dir_name

    def get_filesize(self):
        return self.total_filesize + sum(sd.get_filesize() for sd in self.gen_subdirs())

    def get_subdir(self, sn):
        if sn not in self.subdirs:
            self.subdirs[sn] = FS_Dir(sn, self)
        return self.subdirs[sn]

    def gen_subdirs(self):
        for sd in self.subdirs.values():
            yield sd

    def get_parent_dir(self):
        return self.parent_dir

    def get_smallest_dir_size(self, dir_size_min_bound):
        result = int(1e18)
        if self.get_filesize() >= dir_size_min_bound:
            result = self.get_filesize()
        for sd in self.gen_subdirs():
            result = min(result, sd.get_smallest_dir_size(dir_size_min_bound))
        return result


def process(data):
    root_dir = cur_dir = FS_Dir('/')
    for cmd, val in data:
        if cmd == 'cd':
            if val == '/':
                cur_dir = root_dir
            elif val == '..':
                cur_dir = cur_dir.get_parent_dir()
            else:
                cur_dir = cur_dir.get_subdir(val)
        elif cmd == 'dir':
            _ = cur_dir.get_subdir(val)
        else:
            cur_dir.add_file(cmd, val)
    return root_dir.get_smallest_dir_size(root_dir.get_filesize() - 40000000)


if __name__ == '__main__':
    input_file = 'example.txt' if '--example' in sys.argv[1:] else 'input.txt'
    input_data = read_input(input_file)
    result = process(input_data)
    print(result)
