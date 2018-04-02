import os
import configparser
from time import sleep
from globalmodules.io.fileio import DelimitedFileIO



def run(config):

    sourcedir=config['application']['sourcedir']
    while True:
        if not os.listdir(sourcedir):
            sleep(60)
            print('empty')
        else:
            for each in os.listdir(sourcedir):
                targetfile = sourcedir+"/"+each
                targetdata = DelimitedFileIO(targetfile)
                df = targetdata.read_to_dataframe()
                tst = df.iloc[0]
                print(tst.to_dict())


if __name__ == "__main__":
    config=configparser.ConfigParser()
    config.read('config.ini')
    run(config)


