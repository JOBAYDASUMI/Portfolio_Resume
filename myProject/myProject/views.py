from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

 



def basePage(req):
    
    return render(req, "basePage.html")
def logoutPage(req):
    login(req)
    return redirect("loginPage")

def loginPage(req):
    if req.method== 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        
        user=authenticate(username=username,password=password)
        
        if user:
            if user.usertype == 'admin':
                
                return render(req,"homePage.html")
            
            elif user.usertype == 'viewer':
                
                return HttpResponse("viewPage")
            
        else:
            return HttpResponse("User Is Not Valid")
            
    
    return render(req,"loginPage.html")

def signupPage(req):
    if req.method=='POST':
        Username=req.POST.get('username')
        Email=req.POST.get('email')
        Password=req.POST.get('password')
        Confirm_password=req.POST.get('confirmpassword')
        
        if Password==Confirm_password:
            user=CustomUser.objects.create_user(
                username=Username,
                email=Email,
                password=Confirm_password,
            )
            return redirect("loginPage")
    
    return render(req,"signupPage.html")

def createResumePage(request):
    if request.user.usertype == 'viewer':
        current_user=request.user
        if request.method=='POST':
            
            resume, created= ResumeModel.objects.get_or_create(user=current_user)
            
            resume.contact_No=request.POST.get("contact_No")
            resume.Designation=request.POST.get("Designation")
            resume.Profile_Pic=request.FILES.get("Profile_Pic")
            resume.Carrer_Summary=request.POST.get("Carrer_Summary")
            resume.Age=request.POST.get("Age")
            resume.Gender=request.POST.get("Gender")
            resume.save()
            current_user.first_name=request.POST.get("first_name")
            current_user.last_name=request.POST.get("second_name")
            
            current_user.save()
            messages.success(request, "Resume Created Successfully")

        return render(request,"createResumePage.html")
    else:
        return HttpResponse("You are not authorized to access this page")
def addSkillPage(request):
    
    if request.user.usertype == 'admin':
        return render(request,"addSkillPage.html")
    else:
        return HttpResponse("You are not authorized to access this page")

def addEducation(request):
    
    if request.user.usertype == 'admin':
        return render(request,"addEducation.html")
    else:
        return HttpResponse("You are not authorized to access this page")
    
    
def profilePage(request):
    current_user = request.user

    information = get_object_or_404(ResumeModel, user=current_user)
    Language = LanguageModel.objects.filter(user=current_user)

    context = {
        'Information': information,
        'Language': Language
    }
    
    return render(request, "profilePage.html", context)

def addLanugage(request):
    if request.user.usertype == 'viewer':
        all_lan = IntermediateLanguageModel.objects.all()
        current_user = request.user
        if request.method == 'POST':
            Language_Id = request.POST.get("Language_Id")
            Proficiency_Level = request.POST.get("Proficiency_Level")
            MyObj = get_object_or_404(IntermediateLanguageModel, id=Language_Id)
            
            if LanguageModel.objects.filter(user=current_user, Language_Name=MyObj.Language_Name).exists():
                return HttpResponse("Already Exist")
            
            resume = LanguageModel(
                user=current_user,
                Language_Name=MyObj.Language_Name,  
                Proficiency_Level=Proficiency_Level,
            )
            resume.save()
            
            return redirect("LanguageListbyUser")
    
    context = {
        "all_lan": all_lan
    }
    return render(request, "addLanugage.html", context)

def LanguageListbyUser(request):
    
    current_user=request.user
    
    myLanguage=LanguageModel.objects.filter(user=current_user)
    mySkill=SkillModel.objects.filter(user=current_user)
    
    context={
        "myLanguage":myLanguage,
        "mySkill":mySkill,
    }
    
    return render(request,"LanguageListbyUser.html",context)

def LanguageEditbyUser(request, myid):
    all_lan = IntermediateLanguageModel.objects.all()
    myLanguage = LanguageModel.objects.get(id=myid)
    
    if request.user.usertype == 'viewer':
        current_user = request.user
        
        if request.method == 'POST':
            Language_Id = request.POST.get("Language_Id")
            Proficiency_Level = request.POST.get("Proficiency_Level")
            
            Language_Object = get_object_or_404(IntermediateLanguageModel, id=Language_Id)
            
            resume = LanguageModel(
                id=myid,
                user=current_user,
                Language_Name=Language_Object.Language_Name,
                Proficiency_Level=Proficiency_Level,
            )
            resume.save()
            return redirect("LanguageListbyUser")
    
    context = {
        "myLanguage": myLanguage,
        "all_lan": all_lan
    }
    
    return render(request, "LanguageEditbyUser.html", context)

def addSkillPage(request):
    
    if request.user.usertype == 'viewer':
        All_Skill=IntermediateSkillModel.objects.all()
        current_user = request.user
        if request.method=='POST':
            Skill_Id = request.POST.get("Skill_Id")
            Skill_Level = request.POST.get("Skill_Level")
            
            MyObj = get_object_or_404(IntermediateSkillModel, id=Skill_Id)
            
            if SkillModel.objects.filter(user=current_user, Skill_Name=MyObj.My_Skill_Name).exists():
                return HttpResponse("Skill Already Exist")
            else:
                skill = SkillModel(
                user=current_user,
                Skill_Name=MyObj.My_Skill_Name,  
                Skill_Level=Skill_Level,
            )
                skill.save()
                return redirect("LanguageListbyUser")
        context={
        "All_Skill":All_Skill
    }    
    
    return render(request,"addSkillPage.html",context)


def skillListByUser(request):
    current_user=request.user
    MY_Skill=SkillModel.objects.filter(user=current_user)
    
    context={
        "MY_Skill":MY_Skill
    }
    
    return render(request,"skillListByUser.html",context)

def skillEditByUser(request,myid):
    
    MY_Skill=SkillModel.objects.get(id=myid)
    
    ALL_Skill= IntermediateSkillModel.objects.all()
    
    current_user = request.user
    
    if request.method=='POST':
            Skill_Id = request.POST.get("Skill_Id")
            Skill_Level = request.POST.get("Skill_Level")
            
            MyObj = get_object_or_404(IntermediateSkillModel, id=Skill_Id)
            
            skill = SkillModel(
                id=myid,
                user=current_user,
                Skill_Name=MyObj.My_Skill_Name,  
                Skill_Level=Skill_Level,
            )
            skill.save()
            return redirect("LanguageListbyUser")
    
    context={
        "MY_Skill":MY_Skill,
        "ALL_Skill":ALL_Skill,
        "Proficiency_Level_Choices":SkillModel.Skill_Level_Choices
    }
    
    return render(request,"skillEditByUser.html",context)


def deleteSkillByUser(request,myid):
    
    
    MY_Skill=SkillModel.objects.get(id=myid).delete()
    
    return redirect("LanguageListbyUser")