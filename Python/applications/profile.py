import pandas as pd
import configparser
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from globalmodules.io.databaseio import MSSQLServerDatabase


def run(config):
    dbserver = config['application']['dbaddress']
    dbname = config['application']['dbname']
    targettable = config['application']['targettable']

    dbLendingClub = MSSQLServerDatabase(dbserver, dbname)

    dfLendingClub = dbLendingClub.read_to_datafame('SELECT * FROM {}'.format(targettable))

    ##Profile data at high level
    ##print(dfLendingClub.describe())

    ##Correlate
    ##print(dfLendingClub.corr('pearson'))

    ##Histogram
    print(dfLendingClub.hist())

    ##Decision Tree









if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('profileconfig.ini')
    run(config)