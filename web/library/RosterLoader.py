import csv

from docker_django.apps.importer.models import Roster
from library.LoadResult import LoadResult


class RosterLoader:

    EXPECTED_COL_COUNT = 10

    def __init__(self, csv_file):
        col_count = self.columns_count(csv_file)
        if col_count != RosterLoader.EXPECTED_COL_COUNT:
            raise ValueError("Expected " + str(RosterLoader.EXPECTED_COL_COUNT) + " columns, but got " + str(col_count) + ".")
        fields = ['col' + str(i) for i in range(1, RosterLoader.EXPECTED_COL_COUNT + 1)]
        self.csv_data = csv.DictReader(open(csv_file), fields)

    @staticmethod
    def columns_count(csv_file):
        with open(csv_file, 'r') as f:
            return len(next(csv.reader(f)))

    def load(self, date):

        result = LoadResult()

        for row_number, row in enumerate(self.csv_data):
            try:
                Roster.objects.create(student_id=row['col1'],
                                      student=row['col2'],
                                      grade_level=row['col3'],
                                      course_id=row['col4'],
                                      section=row['col5'],
                                      period=row['col6'],
                                      course_name=row['col7'],
                                      cavg=row['col8'],
                                      teacher=row['col9'],
                                      teacher_id=row['col10'],
                                      date_posted=date)
                result.increment_success()

            except ValueError as e:
                result.increment_failure(row_number, str(e))

        return result
