from typing import List, Tuple


import re

class FileSystem:

    def __init__(self):
        self.path_re = re.compile(r'/([a-z0-9]*)')
        self.fs = {}

    def ls(self, path: str) -> List[str]:
        base = self.fs
        path_parts = self.path_re.findall(path)
        if path_parts != ['']:
            for part in path_parts:
                if isinstance(base[part], dict):
                    base = base[part]
                else:
                    return [part]
        return sorted(base.keys())

    def mkdir(self, path: str) -> None:
        base = self.fs
        for part in self.path_re.findall(path):
            base = base.setdefault(part, {})

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_parts = self.path_re.findall(filePath)
        base = self.fs
        for part in path_parts[:-1]:
            base = base[part]
        base[path_parts[-1]] = base.get(path_parts[-1], "") + content

    def readContentFromFile(self, filePath: str) -> str:
        path_parts = self.path_re.findall(filePath)
        base = self.fs
        for part in path_parts[:-1]:
            base = base[part]
        return base[path_parts[-1]]



fs = FileSystem()
# fs.mkdir("/zijzllb")
# print(fs.ls("/"))
# print(fs.ls("/zijzllb"))
# fs.mkdir("/r")
# print(fs.ls("/"))
# print(fs.ls("/r"))


fs.mkdir("/goowmfn")
print(fs.ls("/goowmfn"))
print(fs.ls("/"))
fs.mkdir("/z")
print(fs.ls("/"))
print(fs.ls("/"))
fs.addContentToFile("/goowmfn/c", "shetopcy")
print(fs.ls("/z"))
print(fs.ls("/goowmfn/c"))
print(fs.ls("/goowmfn"))



# fs.addContentToFile("/a/b/c/d", "hello")
# fs.addContentToFile("/a/b/c/d", " hello hello")
# print(fs.ls("/a/b"))
# print(fs.readContentFromFile("/a/b/c/d"))
# print(fs.fs)




# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

# funcs = ["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
# arguments = [[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]

    return failed


if __name__ == "__main__":
    import sys
    sys.exit(test())

