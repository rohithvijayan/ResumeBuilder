from django.shortcuts import render,redirect,HttpResponse
from .forms import resumeForm
from .models import resume
# Create your views here.
def home(request):
    return render(request,"home.html")
def resume(request):
    return render(request,'resume.html')

def builder(request):
    form=resumeForm()
    if request.method=="POST":
        form=resumeForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            job = request.POST.get("job")
            address = request.POST.get("address")
            phone_number = request.POST.get("phone_number")
            email = request.POST.get("email")
            website = request.POST.get("website")
            skill1 = request.POST.get("skill1")
            skill2 = request.POST.get("skill2")
            skill3 = request.POST.get("skill3")
            skill4 = request.POST.get("skill4")
            skill5 = request.POST.get("skill5")
            twitter = request.POST.get("twitter")
            ytb = request.POST.get("ytb")
            linkedin = request.POST.get("linkedin")
            lang1 = request.POST.get('lang1')
            lang2 = request.POST.get('lang2')
            about = request.POST.get('about')
            work1 = request.POST.get('work1')
            work1_info = request.POST.get('work1_info')
            work2 = request.POST.get('work2')
            work2_info = request.POST.get('work2_info')
            project1 = request.POST.get('project1')
            project1_info = request.POST.get('project1_info')
            project2 = request.POST.get('project2')
            project2_info = request.POST.get('project2_info')
            project3 = request.POST.get('project3')
            project3_info = request.POST.get('project3_info')
            collegeName = request.POST.get('collegeName')
            college_course = request.POST.get('college_course')
            schoolName = request.POST.get('schoolName')
            school_info = request.POST.get('school_info')
            certificate1 = request.POST.get('certificate1')
            certificate1_info = request.POST.get('certificate1_info')
            certificate2 = request.POST.get('certificate2')
            certificate2_info = request.POST.get('certificate2_info')
            form.save()
            return render(request,'resume.html',context = 
                                                    {'name': name,
                                                    'job': job,
                                                    'address': address,
                                                    'phone_number': phone_number,
                                                    'email': email,
                                                    'website': website,
                                                    'skill1': skill1,
                                                    'skill2': skill2,
                                                    'skill3': skill3,
                                                    'skill4': skill4,
                                                    'skill5': skill5,
                                                    'twitter': twitter,
                                                    'ytb': ytb,
                                                    'linkedin': linkedin,
                                                    'lang1': lang1,
                                                    'lang2': lang2,
                                                    'about': about,
                                                    'work1': work1,
                                                    'work1_info': work1_info,
                                                    'work2': work2,
                                                    'work2_info': work2_info,
                                                    'project1': project1,
                                                    'project1_info': project1_info,
                                                    'project2': project2,
                                                    'project2_info': project2_info,
                                                    'project3': project3,
                                                    'project3_info': project3_info,
                                                    'collegeName': collegeName,
                                                    'college_course': college_course,
                                                    'schoolName': schoolName,
                                                    'school_info': school_info,
                                                    'certificate1': certificate1,
                                                    'certificate1_info': certificate1_info,
                                                    'certificate2': certificate2,
                                                    'certificate2_info': certificate2_info,}
)
    context={'form':form}
    return render(request,"builderForm.html",context)
