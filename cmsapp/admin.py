from django.contrib import admin
from .models import *



admin.site.register(User)
admin.site.register(College)
admin.site.register(Depart)
admin.site.register(Branch)
admin.site.register(TimeTable)
admin.site.register(Salary)
admin.site.register(Fee)
admin.site.register(Subject)


admin.site.register(Results)
@admin.register(Student)
class StudentDetail(admin.ModelAdmin):
    list_display=['stu_name','clg_name','dep_name','subj_name']
#admin.site.register(Student)
admin.site.register(StaffMembers)
admin.site.register(Lecturer)