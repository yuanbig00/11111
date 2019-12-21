from django.db import models


# Create your models here.

# class Test(models.Model):
#     name=models.CharField(max_length=20)
#     class Meta:
#         verbose_name_plural='测试'#末尾不加s
#         verbose_name='测试'#末尾加s
#
# class Contact(models.Model):#
#     name=models.CharField(max_length=200)
#     age=models.IntegerField(default=0)
#     email=models.EmailField()
#     def __unicode__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural='事件'#末尾不加s
#         verbose_name='事件'#末尾加s
#         db_table = 'ContactEvent'
#
# class Tag(models.Model):#评论
#     contact=models.ForeignKey(Contact,on_delete=models.CASCADE)
#     name=models.CharField(max_length=50)
#
#     def __unicode__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural='标签'#末尾不加s
#         verbose_name='标签'#末尾加s

class events(models.Model):
    id=models.AutoField(primary_key=True)
    event_name=models.CharField(max_length=255,null=False,verbose_name='事件名称')
    event_description=models.CharField(max_length=255,null=False,verbose_name='事件简介')
    time=models.DateField(verbose_name='事件事时间')
    # past_hour_hot=models.IntegerField(max_length=255,null=False)#onetomany
    past_hour_hot=models.ForeignKey("past_hours_hot",on_delete=models.CASCADE,default=50,verbose_name='过去一小时热度')
    neutral_remark=models.IntegerField(null=False,verbose_name='中性评论')
    positive_remark=models.IntegerField(null=False,verbose_name='积极评论')
    negative_remark=models.IntegerField(null=False,verbose_name='消极评论')
    comment = models.IntegerField(null=True,verbose_name='评论量')
    transmit = models.IntegerField(null=True,verbose_name='转发量')
    follow = models.IntegerField(null=True,verbose_name='点赞量')
   # relative_person_remark=models.CharField(max_length=255,null=False)#onetomany
    relative_person_remark=models.ForeignKey("person_remarks",on_delete=models.CASCADE,default=50,verbose_name='评论数')
    famale=models.IntegerField(null=False,verbose_name='女性')
    male=models.IntegerField(null=False,verbose_name='男性')
    age_05=models.IntegerField(null=False,verbose_name='05后')
    age_00=models.IntegerField(null=False,verbose_name='00后')
    age_95=models.IntegerField(null=False,verbose_name='95后')
    age_90=models.IntegerField(null=False,verbose_name='90后')
    age_85=models.IntegerField(null=False,verbose_name='85后')
    hot = models.IntegerField(null=True,verbose_name='热度')

    def __unicode__(self):
        return self.id

    class Meta:
        db_table='events'
        verbose_name_plural = '事件'  # 末尾不加s
        verbose_name = '事件'  # 末尾加s

    #设置返回主机名
    def __str__(self):
        return "<events:事件id：{id},事件名称：{event_name}>".format(id=self.id,event_name=self.event_name)

class past_hours_hot(models.Model):
    id=models.AutoField(primary_key=True)
    past_onehour_hot=models.IntegerField(null=False,verbose_name='过去一小时的热度')
    past_twohour_hot=models.IntegerField(null=False,verbose_name='过去两小时的热度')
    past_threehour_hot=models.IntegerField(null=False,verbose_name='过去三小时的热度')
    past_fourhour_hot=models.IntegerField(null=False,verbose_name='过去四小时的热度')
    past_fivehour_hot=models.IntegerField(null=False,verbose_name='过去五小时的热度')
    past_sixhour_hot=models.IntegerField(null=False,verbose_name='过去六小时的热度')

    def __unicode__(self):
        return self.id

    class Meta:
        db_table='past_hours_hot'
        verbose_name_plural = '事件热度'  # 末尾不加s
        verbose_name = '事件热度'  # 末尾加s

    def __str__(self):
        return str(self.id)

class person_remarks(models.Model):
    id=models.AutoField(primary_key=True)
    person1_name=models.CharField(max_length=255,null=False,verbose_name='用户1')
    person1_remark=models.CharField(max_length=255,null=False,verbose_name='评论1')
    person1_pic = models.CharField(max_length=255, null=False,verbose_name='用户头像')
    person2_name=models.CharField(max_length=255,null=False,verbose_name='用户2')
    person2_remark=models.CharField(max_length=255,null=False,verbose_name='评论2')
    person2_pic = models.CharField(max_length=255, null=False, verbose_name='用户头像')
    person3_name=models.CharField(max_length=255,null=False,verbose_name='用户3')
    person3_remark=models.CharField(max_length=255,null=False,verbose_name='评论3')
    person3_pic = models.CharField(max_length=255, null=False, verbose_name='用户头像')
    person4_name = models.CharField(max_length=255, null=False,verbose_name='用户4')
    person4_remark = models.CharField(max_length=255, null=False,verbose_name='评论4')
    person4_pic = models.CharField(max_length=255, null=False, verbose_name='用户头像')
    person5_name = models.CharField(max_length=255, null=False,verbose_name='用户5')
    person5_remark = models.CharField(max_length=255, null=False,verbose_name='评论5')
    person5_pic = models.CharField(max_length=255, null=False, verbose_name='用户头像')
    person6_name = models.CharField(max_length=255, null=False,verbose_name='用户6')
    person6_remark = models.CharField(max_length=255, null=False,verbose_name='评论6')
    person6_pic = models.CharField(max_length=255, null=False, verbose_name='用户头像')

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table='person_remarks'
        verbose_name_plural = '事件评论'  # 末尾不加s
        verbose_name = '事件评论'  # 末尾加s

    def __str__(self):
        return str(self.id)



class User(models.Model):
#class User(AbstractUser):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    name = models.CharField(max_length=128, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=256, verbose_name='用户密码')
    email = models.EmailField(unique=True, verbose_name='电子邮件')
    sex = models.CharField(max_length=32, choices=gender, default="男", verbose_name='用户性别')
    c_time = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __str__(self):
        return "<User:用户名：{name}>".format(name=self.name)

