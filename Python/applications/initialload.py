import os
import configparser
from time import sleep
from globalmodules.io.databaseio import MSSQLServerDatabase


def run(config):

    sourcedir=config['application']['sourcedir']
    destinationserver=str(config['application']['dbaddress'])
    destinationdb=str(config['application']['dbname'])

    targetDB=MSSQLServerDatabase(destinationserver, destinationdb)

    for each in os.listdir(sourcedir):
        targetfile = sourcedir + "/" + each
        ##print(targetfile)
        targetDB.bulk_insert("dbo.loans", targetfile, ',', '\\n')



if __name__ == "__main__":
    config=configparser.ConfigParser()
    config.read('config.ini')
    run(config)
