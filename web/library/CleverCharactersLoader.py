import csv

from docker_django.apps.importer.models import CleverCharacters
from library.LoadResult import LoadResult


class CleverCharactersLoader:

    EXPECTED_COL_COUNT = 10

    def __init__(self, csv_file):
        col_count = self.columns_count(csv_file)
        if col_count != CleverCharactersLoader.EXPECTED_COL_COUNT:
            raise ValueError("Expected " + str(CleverCharactersLoader.EXPECTED_COL_COUNT) + " columns, but got " + str(col_count) + ".")
        fields = ['col' + str(i) for i in range(1, CleverCharactersLoader.EXPECTED_COL_COUNT + 1)]
        self.csv_data = csv.DictReader(open(csv_file), fields)

    @staticmethod
    def columns_count(csv_file):
        with open(csv_file, 'r') as f:
            return len(next(csv.reader(f)))

    def load(self, date):
        result = LoadResult()

        for row_number, row in enumerate(self.csv_data):
            try:
                CleverCharacters.objects.create(school=row['col1'],
                                        student_id=row["col2"],
                                        student_name=row["col3"],
                                        grade=row['col4'],
                                        period=row["col5"],
                                        course=row["col6"],
                                        cavg=row["col7"],
                                        teacher=row["col8"],
                                        misconducts=row["col9"],
                                        attendance=row["col10"],
                                        date_posted=date)
                result.increment_success()
            except ValueError as e:
                result.increment_failure(row_number, str(e))
                print(str(e))

        return result
