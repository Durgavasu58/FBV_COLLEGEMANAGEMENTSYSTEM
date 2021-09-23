from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from .forms import SignupForm,LoginForm
from django.contrib.auth import authenticate, login as Allogin
#from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.urls import reverse
from django.contrib import messages
from .models import *
from .forms import LecturerForm,StudentForm,StaffForm,DepartmentForm,CollegeForm,BranchForm,SubjectForm,SalaryForm,ResultForm,TimeTableForm,FeeForm
from django.views.generic import ListView,CreateView,DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .decorator import admin_only,lecturer_only,student_only,staff_only
#from django.contrib.admin.views.decorators import staff_member_required

from django.views import View
def index(request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg  = 'user details invalid'
    else:
        form = SignupForm()
    return render(request,'register.html',{'form':form,'msg':msg})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_admin:
                Allogin(request,user)
                return redirect('adminpage')
            elif user is not None and user.is_lecturer:
                Allogin(request,user)
                return redirect('lecturer')
            elif user is not None and user.is_student:
                Allogin(request,user)
                return redirect('student')
            elif user is not None and user.is_staff:
                Allogin(request,user)
                return redirect('staffmain')
            else:
                return redirect('login')
        else:
            messages.error(request,'Invalid username or password')
    return render(request,'login.html',{'form':LoginForm()})



def logout(request):
    return HttpResponseRedirect(reverse('login'))

@admin_only
def Admin(request):
    return render(request,'registration/home.html')


def lecturer(request):
    if request.user.is_authenticated:
        lect = Lecturer.objects.get(user_id=request.user.id)
        context = {'lect':lect}
        return render(request,'registration/lecturer.html',context)


def student(request):
    if request.user.is_authenticated:
        student = Student.objects.get(user_id=request.user.id)
        context = {'student':student}
        return render(request,'registration/student.html',context)

def StaffMain(request):
    if request.user.is_authenticated:
        staffdata = StaffMembers.objects.get(user_id=request.user.id)
        print(staffdata)
        context = {'staffdata':staffdata}
        return render(request,'registration/Staff.html',context)



# =========================  Department Views    =====================================================

@login_required(login_url='login')
@admin_only
def DepartmentReg(request):
    if request.user.is_authenticated:
        context = {}
        form = DepartmentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('departlist')
        else:
            form = DepartmentForm()
        context['form']=form
        return render(request,'department/departmentreg.html',context)


# class Departlist(ListView):
#     model = Depart
#     context_object_name='departlist'
#     template_name="department/departlist.html"
@admin_only
def Departlist(request):
    departlist = Depart.objects.all()
    context={'departlist':departlist}
    return render(request,'department/departlist.html',context)


# =========================  College Views    =====================================================
@admin_only
def CollegeReg(request):
    if request.user.is_authenticated:
        context = {}
        form = CollegeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('collist')
        else:
            form = CollegeForm()
        context['form']=form
        return render(request,'college/collegereg.html',context)

# class Collegelist(LoginRequiredMixin, ListView):
#         model = College
#         context_object_name='collist'
#         template_name="college/collegelist.html"
@admin_only
def Collegelist(request):
    collist = College.objects.all()
    context={'collist':collist}
    return render(request,'college/collegelist.html',context)     
        
# =========================  Branch Views    =====================================================
@admin_only
def BranchReg(request):
    if request.user.is_authenticated:
        context = {}
        form = BranchForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('Branchlist')
        else:
            form = BranchForm()
        context['form']=form
        return render(request,'branch/branchreg.html',context)


# class Branchlist(ListView):
#         model = Branch
#         context_object_name='branchlist'
#         template_name = 'branch/branchlist.html'
@admin_only
def Branchlist(request):
    branchlist = Branch.objects.all()
    context={'branchlist':branchlist}
    return render(request,'branch/branchlist.html',context)  

# =========================  Subject Views    =====================================================    
@admin_only
def SubjReg(request):
    if request.user.is_authenticated:
        context = {}
        form = SubjectForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('Branchlist')
        else:
            form = SubjectForm()
        context['form']=form
        return render(request,'subject/subjectreg.html',context)


# class Subjlist(ListView):
#         model = Subject
#         context_object_name='subjlist'
#         template_name = 'subject/subjectlist.html'
@admin_only
def Subjlist(request):
    subjlist = Subject.objects.all()
    context={'subjlist':subjlist}
    return render(request,'subject/subjectlist.html',context)          

# =========================  Fee Views    =====================================================
@admin_only
def FeeReg(request):
    if request.user.is_authenticated:
        context = {}
        form = FeeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('Branchlist')
        else:
            form = FeeForm()
        context['form']=form
        return render(request,'Fee/feereg.html',context)


# class Feelist(ListView):
#         model = Fee
#         context_object_name='feelist'
#         template_name = 'Fee/feelist.html'
@admin_only
def Feelist(request):
    feelist = Fee.objects.all()
    context={'feelist':feelist}
    return render(request,'Fee/feelist.html',context) 
# =========================  Salary Views    =====================================================
@admin_only
def SalaryReg(request):
    if request.user.is_authenticated:
        context = {}
        form = SalaryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('salarylist')
        else:
            form = SalaryForm()
        context['form']=form
        return render(request,'Salary/salaryreg.html',context)


# class Salarylist(ListView):
#         model = Salary
#         context_object_name='sallist'
#         template_name = 'Salary/salarylist.html'
@admin_only
def Salarylist(request):
    sallist = Salary.objects.all()
    context={'sallist':sallist}
    return render(request,'Salary/salarylist.html',context)        

# =========================  Result Views    =====================================================
@admin_only
def ResultReg(request):
    if request.user.is_authenticated:
        context = {}
        form = ResultForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('resultlist')
        else:
            form = ResultForm()
        context['form']=form
        return render(request,'Result/resultreg.html',context)


# class Resultlist(ListView):
#         model = Results
#         context_object_name='resultlist'
#         template_name = 'Result/resultlist.html'
@admin_only
def Resultlist(request):
    resultlist = Results.objects.all()
    context={'resultlist':resultlist}
    return render(request,'Result/resultlist.html',context)         

    # =========================  TimeTable Views    =====================================================
@admin_only
def TimetableReg(request):
    if request.user.is_authenticated:
        context = {}
        form = TimeTableForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('timetablelist')
        else:
            form = TimeTableForm()
        context['form']=form
        return render(request,'Timetable/Timetablereg.html',context)


# class Timetablelist(ListView):
#         model = TimeTable
#         context_object_name='tablelist'
#         template_name = 'TimeTable/Timetablelist.html'

@admin_only
def Timetablelist(request):
    tablelist = TimeTable.objects.all()
    context={'tablelist':tablelist}
    return render(request,'Timetable/Timetablelist.html',context) 
# =========================  Lecturer Views    =====================================================
@admin_only
def LecturerReg(request):
    if request.user.is_authenticated:
        context = {}
        form = LecturerForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('lectlist')
        else:
            form = LecturerForm()
        context['form']=form
        return render(request,'lecturer/lectreg.html',context)

# class Lectlist(ListView):
#         model = Lecturer
#         context_object_name='lectlist'
#         template_name = 'lecturer/lectlist.html'
@admin_only
def Lectlist(request):
    lectlist = Lecturer.objects.all()
    context={'lectlist':lectlist}
    return render(request,'lecturer/lectlist.html',context) 

# class LectUpdate(UpdateView):
#         model = Lecturer
#         fields = '__all__'
#         template_name = 'lecturer/lectupdate.html'
#         success_url= reverse_lazy('lectlist')
@admin_only
def LectUpdate(request, pk):
    context ={}
    obj = get_object_or_404(Lecturer, id = pk)
    form = LecturerForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('lectlist')
    context["form"] = form
    return render(request, "lecturer/lectupdate.html", context)


# class LectDelete(DeleteView):
#         model = Lecturer
#         template_name = 'lecturer/lectdelete.html'
#         success_url = reverse_lazy('lectlist')
@admin_only
def LectDelete(request, pk):
    context ={}
    obj = get_object_or_404(Lecturer, id = pk)
    if request.method =="POST":
        obj.delete()
        return redirect('lectlist')
    return render(request, "lecturer/lectdelete.html", context)        

# =========================  Student Views    =====================================================

@admin_only
def Studentreg(request):
    if request.user.is_admin:
        context = {}
        form = StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('studlist')
        else:
            form = StudentForm()
        context['form']=form
        return render(request,'student/studtreg.html',context)


# class StudentList(ListView):
#     model = Student
#     context_object_name='stdlist'
#     template_name = 'student/studentlist.html'
@admin_only
def StudentList(request):
    stdlist = Student.objects.all()
    context={'stdlist':stdlist}
    return render(request,'student/studentlist.html',context) 

@admin_only
def StudentUpdate(request, pk):
    context ={}
    obj = get_object_or_404(Student, id = pk)
    form = StudentForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('studlist')
    context["form"] = form
    return render(request, "student/studentupdate.html", context)

@admin_only
def StudentDelete(request, pk):
    context ={}
    obj = get_object_or_404(Student, id = pk)
    if request.method =="POST":
        obj.delete()
        return redirect('studlist')
    return render(request, "student/studentdelete.html", context)
# class StudentUpdate(UpdateView):
#     model = Student
#     fields = '__all__'
#     template_name = 'student/studentupdate.html'
#     success_url= reverse_lazy('studlist')


# class StudentDelete(DeleteView):
#     model = Student
#     template_name = 'student/studentdelete.html'
#     success_url = reverse_lazy('studlist')

# =========================  Staff Views    =====================================================
@admin_only
def Staffreg(request):
    if request.user.is_authenticated:
        context = {}
        form = StaffForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('other_details')
        else:
            form = StaffForm()
        context['form']=form
        return render(request,'staff/staffreg.html',context)


# class OtherDetails(ListView):
#     model = StaffMembers
#     context_object_name=''
#     template_name = 'staff/stafflist.html'
@admin_only
def OtherDetails(request):
    stf_list = StaffMembers.objects.all()
    context={'stf_list':stf_list}
    return render(request,'staff/stafflist.html',context) 

@admin_only
def StaffUpdate(request, pk):
    context ={}
    obj = get_object_or_404(StaffMembers, id = pk)
    form = StaffForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('other_details')
    context["form"] = form
    return render(request, "staff/staffupdate.html", context)

@admin_only
def StaffDelete(request, pk):
    context ={}
    obj = get_object_or_404(StaffMembers, id = pk)
    if request.method =="POST":
        obj.delete()
        return redirect('other_details')
    return render(request, "staff/staffdelete.html", context)

# class StaffUpdate(UpdateView):
#     model = StaffMembers
#     fields = '__all__'
#     template_name = 'staff/staffupdate.html'
#     success_url= reverse_lazy('other_details')


# class StaffDelete(DeleteView):
#     model = StaffMembers
#     template_name = 'staff/staffdelete.html'
#     success_url = reverse_lazy('other_details')