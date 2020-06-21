import pytest as test
# import CSVtoJSON.csvtojson as c2j
import csvtojson.csvtojson as c2j
from pathlib import Path


def test_check_fp():
    """
    Test that the file check works as intended.
    :return:
    """
    pass


def test_class_CSVtoJSON():
    path = Path("../../resources/CABLES Olex Single Phase 1C Cu Al X-90 Table Database.csv")
    test_cls = c2j.CSVtoJSON(path.resolve())
    test_cls.open_file()
    test_cls.dumps()
    print(f"\n{test_cls._json}")