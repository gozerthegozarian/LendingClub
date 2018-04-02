from abc import ABC, abstractmethod
import pyodbc

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


class MSSQLServerDatabase(AbstractDatabase):
    """
    Specific implementation of SQL Server.
    """

    def __init__(self, strservername, strdatabasename):
        self.strservername=strservername
        self.strdatabasename=strdatabasename
        self.connect()

    def connect(self):
        strdriver= "Driver={SQL Server Native Client 11.0};"
        strserver="Server={};".format(self.strservername)
        strdb="Database={};".format(self.strdatabasename)
        strtrust="Trusted_Connection=yes;"
        self.connection = pyodbc.connect(strdriver+strserver+strdb+strtrust)

    def bulk_insert(self, strtablename):
        cur = self.connection.cursor()
        dbcmd = "insert command here"
        try:
            response = cur.execute(dbcmd)
        except IOError:
            raise


    def run_stored_procedure(self, strspname):
        """
        Run a stored procedure.
        """
        super().run_stored_procedure()



