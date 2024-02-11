from django.db import models

# Create your models here.
class AgentName(models.Model):
    """map to table agentname"""

    name_id = models.IntegerField(primary_key=True, auto_created=True)
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.IntegerField(null=False)

    class Meta:
        db_table = 'agentname'


class AnnouncedLgaResults(models.Model):
    """map to table announced_lga_results"""

    result_id = models.IntegerField(primary_key=True, auto_created=True)
    lga_name = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'announced_lga_results'


class AnnouncedPuResults(models.Model):
    """map to table announced_pu_results"""

    result_id = models.IntegerField(primary_key=True, auto_created=True)
    polling_unit_uniqueid = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)


    class Meta:
        db_table = 'announced_pu_results'


class AnnouncedStateResults(models.Model):
    """map to table announced_state_results"""

    result_id = models.IntegerField(primary_key=True, auto_created=True)
    state_name = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'announced_state_results'


class AnnouncedWardResults(models.Model):
    """map to table announced_ward_results"""

    result_id = models.IntegerField(primary_key=True, auto_created=True)
    ward_name = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'announced_ward_results'


class LGA(models.Model):
    """map to table lga"""

    uniqueid = models.IntegerField(primary_key=True, auto_created=True)
    lga_id = models.IntegerField(null=False)
    lga_name = models.CharField(max_length=50, null=False)
    state_id = models.IntegerField(null=False)
    lga_description = models.TextField(null=True)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'lga'


class Party(models.Model):
    """map to table party"""

    id = models.IntegerField(primary_key=True, auto_created=True)
    partyid = models.CharField(max_length=11, null=False)
    partyname = models.CharField(max_length=11, null=False)


    class Meta:
        db_table = 'party'


class PollingUnit(models.Model):
    """map to table polling_unit"""

    uniqueid = models.IntegerField(primary_key=True, auto_created=True)
    polling_unit_id = models.IntegerField(null=False)
    ward_id = models.IntegerField(null=False)
    lga_id = models.IntegerField(null=False)
    uniquewardid = models.IntegerField(null=True)
    polling_unit_number = models.CharField(max_length=50, null=True)
    polling_unit_name = models.CharField(max_length=50, null=True)
    polling_unit_description = models.TextField(null=True)
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=True)
    user_ip_address = models.CharField(max_length=50, null=False)

    @classmethod
    def get_date_entered(cls, **kwargs):
        try:
            object = cls.objects.get(**kwargs)
            return object.date_entered
        except cls.DoesNotExist:
            return None
        except AttributeError:
            return None

    class Meta:
        db_table = 'polling_unit'

class States(models.Model):
    """map to table states"""

    state_id = models.IntegerField(primary_key=True, auto_created=True)
    state_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'states'


class Ward(models.Model):
    """map to table ward"""

    uniqueid = models.IntegerField(primary_key=True, auto_created=True)
    ward_id = models.IntegerField(null=False)
    ward_name = models.CharField(max_length=50, null=False)
    lga_id = models.IntegerField(null=False)
    ward_description = models.TextField(null=True)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.DateTimeField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'ward'
