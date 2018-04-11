import os
import configparser
import csv
from time import sleep
from globalmodules.io.fileio import DelimitedFileIO
from globalmodules.io.databaseio import MSSQLServerDatabase
from globalmodules.analyzers.dataquality import bool_headers_match
from globalmodules.schemas.lendingclub import SchemaLendingClub


def run(config):

    sourcedir=config['application']['sourcedir']
    processingdir = config['application']['processingdir']
    dbserver=config['application']['dbaddress']
    dbname=config['application']['dbname']
    targettable = config['application']['targettable']
    intbatchsize = int(config['application']['batchsize'])

    while True:
        if not os.listdir(sourcedir):
            sleep(60)
            print('empty')
        else:
            for each in os.listdir(sourcedir):
                targetfile = sourcedir+"/"+each
                targetdata = DelimitedFileIO(targetfile)
                targetdb = MSSQLServerDatabase(dbserver, dbname)
                data, size = targetdata.read_file()
                ##Gather total number of rows
                rowcount = size-1
                batchcount = int(rowcount / intbatchsize)
                header = data.__next__()

                ##Test header
                if bool_headers_match(SchemaLendingClub.columnheaders, header):
                    ##Reformat to increase performance and avoid bulk insert problems.
                    for each in range(0, batchcount + 1):
                        inner = []
                        for row in data:
                            print(len(inner))
                            if len(inner) <= intbatchsize:
                                inner.append(row)
                            else:
                                inner.append(row)
                                break
                        filename = processingdir+'\loan' + str(each + 1) + '.csv'
                        destinationfile = DelimitedFileIO(filename)
                        destinationfile.write_file_to_standard(inner, delimiter='|')
                    ##bulk insert
                        targetdb.bulk_insert(targettable, filename, '|')
                    ##Run Merge SP
                        targetdb.run_stored_procedure('dbo.merge_loans')
                    ##Truncate staging
                        targetdb.run_stored_procedure('stg.truncate_loans')
                    ##remove source file at end of loop
                    ##End Processing routine
                else:
                    exit(-1)
        break

if __name__ == "__main__":
    import timeit
    start_time = timeit.default_timer()
    config=configparser.ConfigParser()
    config.read('config.ini')
    run(config)
    print(timeit.default_timer() - start_time)


