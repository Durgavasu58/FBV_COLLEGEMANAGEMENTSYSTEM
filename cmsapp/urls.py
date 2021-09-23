from django.urls import path
from . import views
from .views import *


urlpatterns=[

    path('',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('accounts/login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('adminpg/',views.Admin,name='adminpage'),
    path('lecturer/',views.lecturer,name='lecturer'), #getting individual lecturer data
    path('student/',views.student,name='student'), #getting individual student data
    path('staff/',views.StaffMain,name='staffmain'), #getting individual staff data
    path('dashboard/',views.dashboard,name='dashboard'),

    # ==========================Lecturer Views============================
    path('lectreg/',views.LecturerReg,name='lectreg'),
    path('lectlist/',views.Lectlist,name='lectlist'),
    path('letupdate/<int:pk>/',views.LectUpdate,name='letupdate'),
    path('letdelete/<int:pk>/',views.LectDelete,name='letdelete'),


    # ==========================Student Views============================
    path('studentreg/',views.Studentreg,name='studreg'),
    path('Studlist/',views.StudentList,name='studlist'),
    path('Studupdate/<int:pk>/',views.StudentUpdate,name='stdupdate'),
    path('Studdelete/<int:pk>/',views.StudentDelete,name='stddelete'),

    # ==========================Staff Views============================
    path('staffreg/',views.Staffreg,name='staffreg'),
    path('details/',views.OtherDetails,name='other_details'), #staff list
    path('otherupdate/<int:pk>/',views.StaffUpdate,name='other_update'),
    path('otherdelete/<int:pk>/',views.StaffDelete,name='other_delete'),
    
    # ==========================Department Views============================
    path('DepartReg/',views.DepartmentReg,name='departreg'),
    path('Departlist/',views.Departlist,name='departlist'),

    # ==========================College Views============================
    path('ColReg/',views.CollegeReg,name='colreg'),
    path('Collist/',views.Collegelist,name='collist'),

    # ==========================Branch Views============================
    path('BranchReg/',views.BranchReg,name='Branchreg'),
    path('Branchlist/',views.Branchlist,name='Branchlist'),

    # ==========================Subject Views============================
    path('SubjectReg/',views.SubjReg,name='Subjreg'),
    path('Subjectlist/',views.Subjlist,name='Subjlist'),

    # ==========================Fee Views============================
    path('FeeReg/',views.FeeReg,name='feereg'),
    path('Feelist/',views.Feelist,name='feelist'),

    # ==========================Salary Views============================
    path('SalaryReg/',views.SalaryReg,name='salaryreg'),
    path('Salarylist/',views.Salarylist,name='salarylist'),

    # ==========================Result Views============================
    path('ResultReg/',views.ResultReg,name='resultreg'),
    path('Resultlist/',views.Resultlist,name='resultlist'),

    # ==========================Time Table Views============================
    path('timetableReg/',views.TimetableReg,name='timetablereg'),
    path('timetablelist/',views.Timetablelist,name='timetablelist'),

]