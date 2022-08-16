from django.db import models

#from digital_index_rough_design import UPI_Val_0, UPI_Vol_0



class historic_index_data(models.Model):
    date = models.DateField()
    index_value = models.FloatField()

class daily_index_data(models.Model):
    date = models.DateField()
    UPI_Vol     = models.FloatField()
    UPI_Val     = models.FloatField()
    IMPS_Vol    = models.FloatField()
    IMPS_Val    = models.FloatField()
    NACH_Vol    = models.FloatField()
    NACH_Val    = models.FloatField()
    NETC_Vol    = models.FloatField()
    NETC_Val    = models.FloatField()
    NEFT_Vol    = models.FloatField()
    NEFT_Val    = models.FloatField()
    RTGS_Vol    = models.FloatField()
    RTGS_Val    = models.FloatField()
    index_value = models.FloatField()

class reference_data(models.Model):
    UPI_Vol     = models.FloatField()
    UPI_Val     = models.FloatField()
    IMPS_Vol    = models.FloatField()
    IMPS_Val    = models.FloatField()
    NACH_Vol    = models.FloatField()
    NACH_Val    = models.FloatField()
    NETC_Vol    = models.FloatField()
    NETC_Val    = models.FloatField()
    NEFT_Vol    = models.FloatField()
    NEFT_Val    = models.FloatField()
    RTGS_Vol    = models.FloatField()
    RTGS_Val    = models.FloatField()
    p0q0        = models.FloatField()
