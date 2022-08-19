import os
import shutil
import xlsxwriter

class FileHandler:

    def __init__(self):
        print("Start File Handling...")

    # Read file from folder, :return all file paths in the folder.
    @staticmethod
    def GetFiles(in_dir, file_type):
        path = in_dir
        files = []
        print("dir:", in_dir)
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file_f in f:
                if file_type in file_f:
                    files.append(file_f)
        print("Files in the folder: ", files)
        return files

    # Move file after Model is run.
    @staticmethod
    def MoveFiles(file_name, from_dir, to_dir):
        shutil.move(from_dir+os.sep+file_name, to_dir)
        print(file_name, ": file successfully moved!")

    # Validate count of inputs
    @staticmethod
    def HasFiles(listFiles):
        count = len(listFiles)
        print("File exists: ", count != 0)
        return count != 0

    # Delete file.
    @staticmethod
    def DeleteFiles(file_name, file_dir):
        os.remove(file_dir + os.sep + file_name)
        print(file_name, ": file is deleted from ", file_dir)

    # Move file after Model is run.
    @staticmethod
    def CopyFiles(from_dir, to_dir):
        shutil.copy(from_dir, to_dir)
        print(from_dir, ": file successfully copied!")
