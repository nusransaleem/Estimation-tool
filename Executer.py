from IP_Model.DataHandler import DataHandler as dHandler
from Predictor import NeuralNetwork as nn
import xlsxwriter


class Execute(object):
    lst_estimations = []
    is_file_exists = False

    def __init__(self):
        dh = dHandler()
        dh.ListTableInfo()
        prd = nn()
        e = prd.predicting()
        self.is_file_exists = dh.has_files

        workbook = xlsxwriter.Workbook('File_Locations//out_location//sample.xls')
        worksheet = workbook.add_worksheet()

        i = 0
        worksheet.write(i, 0, 'Specification')
        worksheet.write(i, 1, 'Time (Minutes)')

        for f in dh.lst_files:
            row = (i+1)
            show_estimation = []
            show_estimation.append(f)
            show_estimation.append(e[i])
            self.lst_estimations.append(show_estimation)
            worksheet.write(row, 0, f)
            worksheet.write(row, 1, e[i])
            i = i + 1
        workbook.close()
        '''
        for data in dh.table_info:
            print("Nusran-----", data)
            rows = data[0]
            columns = data[1]
            cells = data[2]
            merge_cells = data[3]
            data_cells = data[4]
        '''
