import pandas as pd
import csv
from globalmodules.log.loghelper import log_action

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

    @log_action
    def write_file_to_standard(self):
        pass

    @log_action
    def read_file(self):
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
                with open('C:/Users/frede/Downloads/loan.csv/loan.csv', newline='', encoding='utf-8') as f:
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

    @log_action
    def read_file(self):
        contents=[]
        with open(self.strfilelocation, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                contents.append(row)
        return iter(contents), len(contents)

    @log_action
    def write_file_to_standard(self, readerobj, header=True, delimiter='|'):
        with open(self.strfilelocation, 'w', newline='', encoding='utf-8') as target:
            writer = csv.writer(target, delimiter=delimiter)
            writer.writerows(readerobj)