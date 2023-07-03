import os
import pathlib


class MiscellaneousUtility:
    repo_path = os.path.dirname(os.path.abspath(__file__))
    root_path = pathlib.Path(repo_path)
    root_path = root_path.parent
    root_path = str(root_path).replace('WindowsPath(', '').replace(')', '')

    def do_open_directory(self, pathName):
        os.chdir(self.root_path + pathName)
