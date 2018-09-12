from docker_django.apps.importer.models import DataWall


class DataWallLoader:

    def load(self, csv_data, date):

        for row in csv_data:
                DataWall.objects.create(student='blah',
                                        grade_level=row["GL"],
                                        slc=row["SLC"])

        # row.student = models.TextField()
        # row.grade_level = models.PositiveSmallIntegerField()
        # row.slc = models.TextField()
        # row.id = models.TextField()
        # row.race = models.TextField()
        # row.gender = models.TextField()
        # row.lunch = models.TextField()
        # row.sped = models.TextField()
        # row.ell = models.TextField()
        # row.demoted = models.TextField()
        # row.birthdate = models.DateField()
        # row.parent = models.TextField()
        # row.address = models.TextField()
        # row.city = models.TextField()
        # row.state = models.TextField()
        # row.zip = models.TextField()
        # row.parent_phone = models.TextField()
        # row.on_track = models.TextField()
        # row.credits = models.FloatField()
        # row.weighted_gpa = models.FloatField()
        # row.class_rank = models.SmallIntegerField()
        # row.sl_hours = models.SmallIntegerField()
        # row.nwea_rdg = models.SmallIntegerField()
        # row.epas_comp = models.SmallIntegerField()
        # row.last_points = models.SmallIntegerField()
        # row.current_points = models.SmallIntegerField()
        # row.slc_current_points = models.SmallIntegerField()
        # row.trend = models.SmallIntegerField()
        # row.aca = models.SmallIntegerField()
        # row.slc_aca = models.SmallIntegerField()
        # row.att = models.TextField()
        # row.slc_att = models.TextField()
        # row.beh = models.SmallIntegerField()
        # row.coach = models.SmallIntegerField()
        # row.action_plan_goal = models.SmallIntegerField()
