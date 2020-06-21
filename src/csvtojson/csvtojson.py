import csv as csv
import json as json
import pathlib as path


class CSVtoJSON:
    """
    A class to convert csv to json. It takes a csv and returns a json representation.
    """
    def __init__(self, fp):
        """

        """
        self._json = ""
        self._fp = path.Path(fp)
        self._csv = []
        self._json = ""

    def check_fp(self):
        """
        A method to confirm that self._fp exists.
        :return:
        """
        pass

    def open_file(self):
        """
        Open the csv file and save the contents as a list of dictionaries.
        :return:
        """
        with open(self._fp, newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self._csv.append(row)


    def dumps(self):
        self._json = json.dumps(self._csv)