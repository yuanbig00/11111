from django.db import models

# Create your models here.


class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

class events(models.Model):
    id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=255,null=False)
    event_description=models.CharField(max_length=255,null=False)
    time=models.DateTimeField()
    # past_hour_hot=models.IntegerField(max_length=255,null=False)#onetomany
    past_hour_hot=models.ForeignKey("past_hours_hot",on_delete=models.CASCADE)
    neutral_remark=models.IntegerField(null=False)
    positive_remark=models.IntegerField(null=False)
    negative_remark=models.IntegerField(null=False)
    comment=models.IntegerField(null=True)
    transmit = models.IntegerField(null=True)
    follow = models.IntegerField(null=True)
   # relative_person_remark=models.CharField(max_length=255,null=False)#onetomany
    relative_person_remark=models.ForeignKey("person_remarks",on_delete=models.CASCADE)
    famale=models.IntegerField(null=False)
    male=models.IntegerField(null=False)
    age_05=models.IntegerField(null=False)
    age_00=models.IntegerField(null=False)
    age_95=models.IntegerField(null=False)
    age_90=models.IntegerField(null=False)
    age_85=models.IntegerField(null=False)
    hot=models.IntegerField(null=True)

    class Meta:
        # ordering = ["-time"]
        db_table='events'

class past_hours_hot(models.Model):
    id=models.AutoField(primary_key=True)
    past_onehour_hot=models.IntegerField(null=False)
    past_twohour_hot=models.IntegerField(null=False)
    past_threehour_hot=models.IntegerField(null=False)
    past_fourhour_hot=models.IntegerField(null=False)
    past_fivehour_hot=models.IntegerField(null=False)
    past_sixhour_hot=models.IntegerField(null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table='past_hours_hot'

class person_remarks(models.Model):
    id=models.AutoField(primary_key=True)
    person1_name=models.CharField(max_length=255,null=False)
    person1_remark=models.CharField(max_length=255,null=False)
    person1_pic = models.CharField(max_length=255, null=False)
    person2_name=models.CharField(max_length=255,null=False)
    person2_remark=models.CharField(max_length=255,null=False)
    person2_pic = models.CharField(max_length=255, null=False)
    person3_name=models.CharField(max_length=255,null=False)
    person3_reamrk=models.CharField(max_length=255,null=False)
    person3_pic = models.CharField(max_length=255, null=False)
    person4_name = models.CharField(max_length=255, null=False)
    person4_reamrk = models.CharField(max_length=255, null=False)
    person4_pic = models.CharField(max_length=255, null=False)
    person5_name = models.CharField(max_length=255, null=False)
    person5_reamrk = models.CharField(max_length=255, null=False)
    person5_pic = models.CharField(max_length=255, null=False)
    person6_name = models.CharField(max_length=255, null=False)
    person6_reamrk = models.CharField(max_length=255, null=False)
    person6_pic = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table='person_remarks'