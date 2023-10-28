import os
from src import constants
import csv
from src.parsed_file import ParsedFile

class CSVParser:
    def __init__(self, csv_file_route):
        self.csv_file_route = csv_file_route
        self.state = constants.FILE_NOT_EXISTS
        self.file = ParsedFile()
        self.pendientes = 0
    
    def parse_file(self):
        with open(self.csv_file_route, encoding='utf-8') as csvFile:
            CSVdata = csv.reader(csvFile, delimiter=',')
            row_count = 0
            for row in CSVdata:
                if row_count == 0:
                    self.file.headers = row
                else:
                    self.file.data = self.file.data + [row]
                row_count += 1
            csvFile.close()

    def reload_file(self):
        pass

    def get_file_state(self):
        return self.state

    def check_file_permissions(self) -> int:
        # Check if file exists
        if not os.path.exists(self.csv_file_route):
            self.state = constants.FILE_NOT_EXISTS
            return self.state
        else:
            self.state = constants.FILE_EXISTS

        # Check if we have permissions to read the file
        if os.access(self.csv_file_route, os.R_OK):
            self.state = constants.FILE_PERMISSIONS_OK
        else:
            self.state = constants.FILE_PERMISSIONS_NOT_OK
        
        return self.state
    
    def get_numero_pendientes(self) -> int:
        for row in self.file.data:
            if constants.PENDIENTE_STRING in row:
                self.pendientes +=1
        return self.pendientes
