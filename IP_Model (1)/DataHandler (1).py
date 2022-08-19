from IP_Model.FileHandler import FileHandler as fHandle
from IP_Model.TableExtractor import TableExtractor as tblExtract
import os
from numpy import exp, array, random, dot


class DataHandler(object):
    file_location = ""
    IN_FOLDER = ""
    OUT_FOLDER = ""
    TEMP_FOLDER = ""
    TRAINING_DATA = ""
    table_info = []
    lst_files = []
    has_files = False
    training_inputs = []
    training_outputs = []
    lstDataSets = []
    lstOutputs = ""

    def __init__(self):

        file_location = "File_Locations" + os.sep
        self.IN_FOLDER = file_location + "in_location"
        self.OUT_FOLDER = file_location + "out_location"
        self.TEMP_FOLDER = file_location + "temp_location"
        self.TRAINING_DATA = file_location + "training_data"
        self.table_info = []
        self.lstDataSets = fHandle.GetFiles(self.TRAINING_DATA, '.json')
        self.lstOutputs = fHandle.GetFiles(self.TRAINING_DATA, '.txt')

        self.lst_files = fHandle.GetFiles(self.IN_FOLDER, '.pdf')
        self.has_files = fHandle.HasFiles(self.lst_files)

    def ListTableInfo(self):
        if self.has_files:
            for f in self.lst_files:
                fHandle.MoveFiles(f, self.IN_FOLDER, self.TEMP_FOLDER)
                file_path = self.TEMP_FOLDER + os.sep + f
                json_path = tblExtract.ExtractTableToJason(file_path)
                table = tblExtract.LoadTable(json_path)
                info = tblExtract.ReadTableInfo(table)
                #fHandle.MoveFiles(f, self.TEMP_FOLDER, self.OUT_FOLDER)
                fHandle.DeleteFiles(f, self.TEMP_FOLDER)
                fHandle.DeleteFiles(f.replace("pdf", "json"), self.TEMP_FOLDER)
                self.table_info.append(info)

    def GetTrainingDataSets(self):
        for f in self.lstOutputs:
            file1 = open(self.TRAINING_DATA + os.sep + f, "r+")
            r = file1.read()
            w = r.split(",")
            results = [int(i) for i in w]
            self.training_outputs = results

        for ds in self.lstDataSets:
            json_path = self.TRAINING_DATA + os.sep + ds
            table = tblExtract.LoadTable(json_path)
            info = tblExtract.ReadTableInfo(table)
            self.training_inputs.append(info)
