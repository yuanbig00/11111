from django.contrib import admin
# from front.models import Test,Contact,Tag
from .models import past_hours_hot,person_remarks,events,User

# Register your models here.

# class TagInline(admin.TabularInline):#内联显示
#     model=past_hours_hot
#     model=person_remarks
#     model=Tag

#设置站点标题
admin.site.site_title='管理员首页'
#设置站点头
admin.site.site_header='灾害舆情管理'
#设置首页辩题
admin.site.index_title='灾害舆情传播系统'


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','event_name','event_description','time','comment','transmit','follow','hot']
    search_fields = ['event_name']

    # fields=('name','email')#自定义表单
    # inlines = [TagInline]#Inline
    fieldsets = (           #将输入栏分块
        ['主要信息',{
            'fields':('event_name','event_description','time','comment','transmit','follow','hot',),
        }],
        ['辅要信息',{
            'classes':('collapse',),#css
            'fields':('neutral_remark','positive_remark','negative_remark',
                      'famale','male','age_05','age_00','age_95','age_90','age_85',),
        }]
    )

#admin.site.register(Contact,ContactAdmin)
admin.site.register(events,ContactAdmin)
# admin.site.register([Test])

class HotAdmain(admin.ModelAdmin):
    list_display = ['id','past_onehour_hot','past_twohour_hot','past_threehour_hot',
                    'past_fourhour_hot','past_fivehour_hot','past_sixhour_hot']
    search_fields = ['id']
    # fields = ('id','past_onehour_hot','past_twohour_hot','past_threehour_hot',
    #                 'past_fourhour_hot','past_fivehour_hot','past_sixhour_hot')
    # fieldsets = (
    #     ['ID',{
    #         'fields':('id',),
    #     }],
    #     ['详细信息',{
    #         'classes': ('collapse',),  # css
    #         'fields': ('past_onehour_hot', 'past_twohour_hot', 'past_threehour_hot',
    #                    'past_fourhour_hot', 'past_fivehour_hot', 'past_sixhour_hot',),
    #     }]
    # )

class RemarkAdmin(admin.ModelAdmin):
    list_display = ['id','person1_remark','person2_remark',
                    'person3_remark','person4_remark',
                    'person5_remark','person6_remark']
    search_fields = ['id']
    # classes= ('collapse')
    # fields = ('id','person1_name','person1_remark','person2_name','person2_remark',
    #                 'person3_name','person3_remark','person4_name','person4_remark',
    #                 'person5_name','person5_remark','person6_name','person6_remark')


admin.site.register(past_hours_hot,HotAdmain)
admin.site.register(person_remarks,RemarkAdmin)
# admin.site.register([past_hours_hot,person_remarks])

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','password','email','sex','c_time']
    search_fields = ['name']

admin.site.register(User,UserAdmin)