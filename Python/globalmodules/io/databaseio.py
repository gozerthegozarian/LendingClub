from abc import ABC, abstractmethod
import pyodbc
import pandas
from globalmodules.log.loghelper import log_action

class AbstractDatabase(ABC):
    """
    Abstract base class to serve as parent for different implementations of databases.
    """

    def __init__(self):
        pass

    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def run_stored_procedure(self):
        pass
    @abstractmethod
    def bulk_insert(self):
        pass

    @abstractmethod
    def read_to_datafame(self):
        pass

    @abstractmethod
    def run_query(self):
        pass


class MSSQLServerDatabase(AbstractDatabase):
    """
    Specific implementation of SQL Server.
    """

    @log_action
    def __init__(self, strservername, strdatabasename):
        self.strservername=strservername
        self.strdatabasename=strdatabasename
        self.connect()

    @log_action
    def connect(self):
        strdriver= "Driver={SQL Server Native Client 11.0};"
        strserver="Server={};".format(self.strservername)
        strdb="Database={};".format(self.strdatabasename)
        strtrust="Trusted_Connection=yes;"
        self.connection = pyodbc.connect(strdriver+strserver+strdb+strtrust, autocommit=True)

    @log_action
    def bulk_insert(self, strtablename, strfilepath, filedelimeter, rowterminator="0x0a", rowsperbatch=100000):
        """
        Use file system for fast loading.
        """
        cur = self.connection.cursor()
        dbcmd = "BULK INSERT {} FROM '{}' WITH (FIELDTERMINATOR ='{}', ROWTERMINATOR ='{}', ROWS_PER_BATCH={});".format(strtablename, strfilepath, filedelimeter,rowterminator, rowsperbatch)
        try:
            print(dbcmd)
            response = cur.execute(dbcmd)
            return response
        except IOError:
            raise

    @log_action
    def run_stored_procedure(self, strspname, params=None):
        """
        Run a stored procedure.
        """
        cur = self.connection.cursor()
        if params is None:
            dbcmd = "EXECUTE {};".format(strspname)
        else:
            dbcmd = "EXECUTE {} {};".format(strspname, params)
        try:
            print(dbcmd)
            return cur.execute(dbcmd)
        except IOError:
            raise

    @log_action
    def read_to_datafame(self, query):
        df = pandas.read_sql(query,coerce_float=self.connection)
        return df

    @log_action
    def run_query(self, strsql):
        """
        Run a stored procedure.
        """
        cur = self.connection.cursor()
        if strsql.startswith('SELECT') or strsql.startswith("select") or strsql.startswith('Select'):
            try:
                print(strsql)
                return cur.execute(strsql)
            except IOError:
                raise
        else:
            Exception("Must be a select statement.  Read only!")
            raise


