import csv

from docker_django.apps.importer.models import DataWall
from library.LoadResult import LoadResult


class DataWallLoader:

    EXPECTED_COL_COUNT = 35

    def __init__(self, csv_file):
        col_count = self.columns_count(csv_file)
        if col_count != DataWallLoader.EXPECTED_COL_COUNT:
            raise ValueError("Expected " + str(DataWallLoader.EXPECTED_COL_COUNT) + " columns, but got " + str(col_count) + ".")
        fields = ['col' + str(i) for i in range(1, DataWallLoader.EXPECTED_COL_COUNT + 1)]
        self.csv_data = csv.DictReader(open(csv_file), fields)

    @staticmethod
    def columns_count(csv_file):
        with open(csv_file, 'r') as f:
            return len(next(csv.reader(f)))

    def load(self, date):
        result = LoadResult()

        for row_number, row in enumerate(self.csv_data):
            try:
                DataWall.objects.create(student=row['col1'],
                                        grade_level=row["col2"],
                                        slc=row["col3"],
                                        student_id=row['col4'],
                                        race=row["col5"],
                                        gender=row["col6"],
                                        lunch=row["col7"],
                                        sped=row["col8"],
                                        ell=row["col9"],
                                        demoted=row["col10"],
                                        birthdate=row["col11"],
                                        parent=row["col12"],
                                        address=row["col13"],
                                        city=row["col14"],
                                        state=row["col15"],
                                        zip=row["col16"],
                                        parent_phone=row["col17"],
                                        on_track=row["col18"],
                                        credits=row["col19"],
                                        weighted_gpa=row["col20"],
                                        class_rank=row["col21"],
                                        sl_hours=row["col22"],
                                        nwea_rdg=row["col23"],
                                        epas_comp=row["col24"],
                                        last_points=row["col25"],
                                        current_points=row["col26"],
                                        slc_current_points=row["col27"],
                                        trend=row["col28"],
                                        aca=row["col29"],
                                        slc_aca=row["col30"],
                                        att=row["col31"],
                                        slc_att=row["col32"],
                                        beh=row["col33"],
                                        coach=row["col34"],
                                        action_plan_goal=row["col35"],
                                        date_posted=date)
                result.increment_success()
            except ValueError as e:
                result.increment_failure(row_number, str(e))

        return result
