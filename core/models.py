from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core import validators
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MaxValueValidator

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


# Create your models here.
def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'


def get_default_profile_image():
    return "not exist"

class Types(models.TextChoices):
    MANAGER = "MANAGER", "manager"
    INTERN = "INTERN", "intern"

class Status(models.TextChoices):
    PENDING = "PENDING", "pending"
    IN_PROGRESS = "IN PROGRESS", "In progress"
    FIXED = "FIXED","fixed"
    COMPLETED = "COMPLETED","completed"

class Account(AbstractUser):
    user_type = models.CharField(("Type"),max_length=50,choices=Types.choices,default=Types.INTERN,blank=False)
    user_id = models.AutoField(primary_key = True)
    email = models.EmailField(
        validators=[validators.validate_email], unique=True, blank=False
    )
    password = models.CharField(max_length=66,blank=False)
    username = models.CharField(max_length=66,blank = False,unique=True)
    profile_image = models.ImageField(
        max_length=255,
        upload_to=get_profile_image_filepath,
        null=True,
        blank=True,
        default=get_default_profile_image,
    )
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16,blank=True)
    date_joined = models.DateField(verbose_name="date joined",auto_now_add=True,blank=True)


class LoginLogoutLog(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE,null=False)
    session_key = models.CharField(max_length=100, blank=False,null=False)
    host = models.CharField(max_length=100, blank=False,null=False)
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)

class Task(models.Model):
    task_id = models.AutoField(primary_key = True)
    manager_id = models.ForeignKey(Account,on_delete=models.CASCADE,null=False,default=None,related_name="managid")
    intern_id = models.ForeignKey(Account,on_delete=models.CASCADE,null=False,default=None,related_name="intid")
    deadline = models.DateTimeField(auto_now_add=False,null=False)
    task_name = models.CharField(max_length=66,null=False)
    description = models.TextField(blank = True,null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

class Blocker(models.Model):
    blocker_id = models.AutoField(primary_key = True)
    manager_id = models.ForeignKey(Account,on_delete=models.CASCADE,null=False,related_name="to")
    intern_id = models.ForeignKey(Account,on_delete=models.CASCADE,null=False,related_name="internid")
    blocker_task_id = models.ForeignKey(Task,on_delete=models.CASCADE,related_name="taskid")
    label = models.CharField(max_length=66)
    query = models.TextField(blank=False)


class Blocker_Answer(models.Model):
    blocker = models.OneToOneField(Blocker,on_delete=models.CASCADE,null=True)
    answer = models.TextField()


class Progress(models.Model):
    progress_id = models.AutoField(primary_key = True)
    progress_task_id = models.ForeignKey(Task,on_delete=models.CASCADE,null=False,related_name="progress_task_id")
    intern_id = models.ForeignKey(Account,on_delete=models.CASCADE,null=False,related_name="intern")
    points = models.FloatField(blank=True,default=0.00)
    status = models.CharField(("Status"), max_length=50, choices=Status.choices, default=Status.PENDING)


