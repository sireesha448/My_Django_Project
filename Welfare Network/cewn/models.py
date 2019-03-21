from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    type = models.CharField(max_length=20)



class ApprovalUsers(models.Model):
    employee_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    address = models.TextField()
    email_id = models.EmailField(max_length=30)
    contact_no = models.IntegerField()
    date_of_birth = models.DateField(default=False)
    company_name = models.CharField(max_length=30)
    status = models.CharField(max_length=20, default=False)


class AcceptedUsers(models.Model):
    employee_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    address = models.TextField()
    email_id = models.EmailField(max_length=30)
    contact_no = models.IntegerField()
    # date_of_birth = models.DateField()
    company_name = models.CharField(max_length=30)
    status = models.CharField(max_length=20, default=False)


class RejectedUser(models.Model):
    employee_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    address = models.TextField()
    email_id = models.EmailField(max_length=30)
    contact_no = models.IntegerField()
    # date_of_birth = models.DateField()
    company_name = models.CharField(max_length=30)
    status = models.CharField(max_length=20, default=False)


class Thoughts(models.Model):
    username=models.CharField(max_length=30)
    description=models.CharField(max_length=100)
    contact_no=models.IntegerField(primary_key=True)


class Events(models.Model):
    username = models.CharField(max_length=30)
    startdate = models.DateField()
    enddate = models.DateField()
    description = models.TextField(max_length=100)
    contact_no = models.IntegerField(primary_key=True)


class Technical(models.Model):
    username = models.CharField(max_length=30)
    technology = models.CharField(max_length=30)
    description = models.TextField(max_length=30)
    contact_no = models.IntegerField()



class WorkExperience(models.Model):
    username = models.CharField(max_length=30)
    technology = models.CharField(max_length=30)
    workExperience = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    contact_no = models.IntegerField()



class Property(models.Model):
    username = models.CharField(max_length=30)
    property_type = models.CharField(choices=(('--select--','--select--'),('SALE','sale'),('RENT','rent')),max_length=10)
    property_title = models.CharField(max_length=30)
    area_in_size = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    address = models.TextField()
    contact_no = models.IntegerField()
    email_id = models.EmailField()




class ShareMarket(models.Model):
    username = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    share_value = models.IntegerField()
    description = models.TextField()



class Reference(models.Model):
    username = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    description = models.TextField()
    last_date = models.DateField()



class Matrimonial(models.Model):
    bride_or_bridegromname = models.CharField(max_length=30)
    gender = models.CharField(choices=(('MALE','male'),('FEMALE','female')),max_length=5)
    date_of_birth = models.DateField()
    description = models.TextField()
    contact_no = models.IntegerField()



class Celebrations(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    contact_no = models.IntegerField()
    email_id= models.EmailField()
    date_of_birth = models.DateField()


class Travel(models.Model):
    username = models.CharField(max_length=30)
    travel_date = models.DateField()
    location = models.TextField()
    description = models.TextField()
    contact_no = models.IntegerField()