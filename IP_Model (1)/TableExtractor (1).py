import tabula
import json


class TableExtractor:

    # Extract table from pdf and save as json file.
    @staticmethod
    def ExtractTableToJason(file_path):
        pdf_path = file_path
        json_path = file_path.replace("pdf", "json")
        print("PDF:", pdf_path, "JSON:", json_path)
        tabula.convert_into(
            pdf_path, json_path,
            output_format="json",
            pages='all'
        )
        return json_path

    # Load saved json file to the system.
    @staticmethod
    def LoadJasonFile(json_file):
        data = []
        with open(json_file) as f:
            for line in f:
                data.append(json.loads(line))
        return data

    # Load contents of the table from json file.
    @staticmethod
    def LoadTable(json_file):
        table = TableExtractor.LoadJasonFile(json_file)
        lst_data = table[0][0]['data']
        return lst_data

    def p(self):
        print("Nus")

    # Get table information.
    @staticmethod
    def ReadTableInfo(table):

        rows = 0
        cells = 0
        merge_cells = 0
        data_cells = 0
        temp_cells = 0
        for r in table:
            columns = 0
            for c in r:
                top = c['top']
                left = c["left"]
                width = c["width"]
                height = c["height"]
                text = c["text"]
                columns = columns + 1
                temp_cells = temp_cells + 1
                print("Column:", columns, "Cell: (", rows + 1, ",", columns, ")")
                print(c)
                is_merge = ((not text) and top == 0.0 and left == 0.0 and width == 0.0 and height == 0.0)
                if text:
                    data_cells = data_cells + 1
                if is_merge:
                    merge_cells = merge_cells + 1
                    print(">>This cell is merged with other cell or not align with cell in the previous row.>>")
            rows = rows + 1
            print("Row:", rows, "------------------------------------------------------------------------------")
        cells = temp_cells - merge_cells
        print("============= Output ======================")
        print("Number of rows: ", rows)
        print("Number of columns: ", columns)
        print("number of cells: ", cells)
        print("Number of Merge/Not Align cells: ", merge_cells)
        print("Number of Data cells: ", data_cells)
        print("===========================================")

        return rows, columns, cells, merge_cells, data_cells
