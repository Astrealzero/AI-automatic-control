import os
import subprocess


class software:
    def __init__(self):
        self.filenames = []
        self.file = "../app_folder"

    def folder_list(self):

        if not os.path.exists(self.file):
            print("app_folder不存在")
        else:
            for filename in os.listdir(self.file):
                if os.path.isfile(os.path.join(self.file, filename)):
                    file_name_without_ext = os.path.splitext(filename)[0]
                    self.filenames.append(file_name_without_ext)
            return self.filenames

    def run_routine(self, routine_name):
        subprocess.run(routine_name)


if __name__ == "__main__":
    software = software()
    name = software.folder_list()
    print(name)
