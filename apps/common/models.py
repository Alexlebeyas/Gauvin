from django.db import models


class Language(models.Model):
    id = models.AutoField(db_column="icLangue", primary_key=True)
    description = models.CharField(
        db_column="cDescription", max_length=50, db_collation="SQL_Latin1_General_CP1_CI_AS", blank=True, null=True
    )
    description_en = models.CharField(
        db_column="cDescriptionAn", max_length=50, db_collation="SQL_Latin1_General_CP1_CI_AS", blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = "tblLangue"
