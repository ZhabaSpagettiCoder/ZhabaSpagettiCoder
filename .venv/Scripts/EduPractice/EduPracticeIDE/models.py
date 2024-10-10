# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Inputdatarequests(models.Model):
    requestid = models.AutoField(db_column='requestID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    problemdescryption = models.TextField(db_column='problemDescryption', blank=True, null=True)  # Field name made lowercase.
    requeststatus = models.TextField(db_column='requestStatus', blank=True, null=True)  # Field name made lowercase.
    techid = models.ForeignKey('Techt', models.DO_NOTHING, db_column='TechID', blank=True, null=True,db_constraint=False)  # Field name made lowercase.
    completiondate = models.DateField(db_column='completionDate', blank=True, null=True)  # Field name made lowercase.
    repairparts = models.TextField(db_column='repairParts', blank=True, null=True)  # Field name made lowercase.
    clientid = models.TextField(db_column='clientID')  # Field name made lowercase.
    masterid = models.TextField(db_column='masterID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'InputDataRequests'


class Inputdatauser(models.Model):
    fio = models.TextField()
    phone = models.TextField(blank=True, null=True)
    login = models.TextField(primary_key=True)
    password = models.TextField()
    type = models.ForeignKey('Typesofusers', models.DO_NOTHING, db_column='type', blank=True, null=True)
    ID = models.TextField(max_length=3)
    class Meta:
        managed = False
        db_table = 'InputDataUser'


class Statistic(models.Model):
    countofrequests = models.IntegerField(db_column='countOfRequests', blank=True, null=True)  # Field name made lowercase.
    kindofproblem = models.TextField(db_column='kindOfProblem', blank=True, null=True)  # Field name made lowercase.
    dateofproblem = models.DateField(db_column='dateOfProblem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Statistic'


class Techt(models.Model):
    orgtechtype = models.TextField(db_column='orgTechType', blank=True, null=True)  # Field name made lowercase.
    orgtechmodel = models.TextField(db_column='orgTechModel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TechT'


class Typesofusers(models.Model):
    
    name = models.TextField()
    class Meta:
        managed = False
        db_table = 'TypesOfUsers'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Inputdatacomments(models.Model):
    commentid = models.AutoField(db_column='commentID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    message = models.TextField()
    masterid = models.ForeignKey(Inputdatauser, models.DO_NOTHING, db_column='masterID', blank=True, null=True)  # Field name made lowercase.
    requestid = models.ForeignKey(Inputdatarequests, models.DO_NOTHING, db_column='requestID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inputDataComments'
