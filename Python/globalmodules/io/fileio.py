import pandas as pd
from globalmodules.log.loghelper import log_action
import csv

class FileIO(object):
    """
    File interface
    """

    @log_action
    def __init__(self, strfilelocation):
        self.strfilelocation=strfilelocation

    @log_action
    def read_to_dataframe(self):
        pass

    @log_action
    def write_from_dataframe(self):
        pass

    def write_file(self):
        pass


class DelimitedFileIO(FileIO):
    """
    Delimited implementation.
    """
    @log_action
    def __init__(self, strfilelocation, delimter=None):
        self.strfilelocation=strfilelocation
        if delimter is None:
            try:
                with open('C:/Users/frede/Downloads/loan.csv/loan.csv', newline='') as f:
                    dialect = csv.Sniffer().sniff(f.read(10 * 1024))
                    self.delimter =dialect.delimiter
            except:
                self.delimter=','
        else:
           self.delimter=delimter

    @log_action
    def write_from_dataframe(self):
        try:
            self.dataframe.to_csv(self.strfilelocation)
        except IOError:
            raise

    @log_action
    def read_to_dataframe(self):
        try:
            df = pd.read_csv(self.strfilelocation)
        except IOError:
            raise
        return df
