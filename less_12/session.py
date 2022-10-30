from contextlib import contextmanager
from typing import ContextManager
import sqlite3


class Cursor:
    def __init__(self, path=":memory:"):
        self._connect = sqlite3.connect(path)
        self._curs = self._connect.cursor()

    def __del__(self):
        self.close()
        self._curs = None
        self._connect = None

    def close(self):
        try:
            self._curs.close()
            self._connect.close()
        except:
            pass

    def execute(self, *args, **kw):
        return self._curs.execute(*args, **kw)

    def executemany(self, *args, **kw):
        return self._curs.executemany(*args, **kw)

    def fetchall(self):
        return self._curs.fetchall()

    def commit(self):
        return self._connect.commit()


glob_cursor = Cursor('hwdb.sqlite')


@contextmanager
def open_db_cursor() -> ContextManager[sqlite3.Cursor]:
    yield glob_cursor
    glob_cursor.close()
