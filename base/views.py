from django.shortcuts import render, redirect
import requests
from .models import projects, skill, atchviements, certificate, hackthons, resume, Roles
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.

from datetime import date

# def usr(request):
#     user = User.objects.create_user('nagipragalathan', 'nagipragalathan@gmail.com', '7401268091')
#     user.save()
#     print("user saved")
#     return render(request,'Modified_files/sample.html')

def check_pass(request):
    username = request.POST.get('mail')
    password = request.POST.get('pass')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request,user)
        return redirect('edit')
    else:
        return render(request,'Modified_files/login.html')

def login_to_edit(request):
    return render(request,'Modified_files/login.html')

def home(request):
    return render(request,'Modified_files/sample.html')

def resumes(request):
    res = [ i.img for i in resume.objects.all() ]
    try :
        return render(request,'Modified_files/resume.html',{'resume':res[-1]})
    except:
        return render(request,'Modified_files/resume.html',{'resume':res})

def blog(request):
    project = [["https://imgs.search.brave.com/DaF2J-lw_q55hmQePzAqxD4R1HTalI2o8xRKDtSofqY/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9oZHdh/bGxwYXBlcmltLmNv/bS93cC1jb250ZW50/L3VwbG9hZHMvMjAx/Ny8wOC8yMi84Njkx/MC1hbmltZS1saWdo/dGhvdXNlLWZsb2F0/aW5nX2lzbGFuZC5q/cGc","title","date","para"]]
    return render(request,'Modified_files/blog.html',{'project':project})

def about(request):

    github_username  = "NagiPragalathan"

    #api url to grab public user repositories
    api_url = f"https://api.github.com/users/{github_username}/repos"

    response = requests.get(api_url)
    skills = skill.objects.all()
    # skill = {"Python":"60%","Html":"60%","Css":"30%","Sqlite":"20%","Mysql":"40%","C":"50%","MIT Tool":"40%","Blender basics":"30%","2D Devalopment":"30%","3D Devalopment":"40%","Flask":"50%","Pygame":"30%","Java":"30%","Unity":"40%","Figma":"50%","Canva":"60%","Filmora":"40%","JavaScript":"50%","Tkinter":"30%","Swing":"60%"}
    skill_list = {}
    skill_detial = skill.objects.all()
    for i in skill_detial:
        skill_list[i.language] = i.persentage
    skill_r = {}
    skill_l = {}
    data =  response.json()
    repository = {}
    count = 0
    for repositorys in data:
        repository[repositorys["name"]] = repositorys["created_at"]

    for key,val in skill_list.items():
        count=count+1
        if count % 2 == 0 :
            skill_r[key] = val
        else:
            skill_l[key] = val

    atc = []
    for i in atchviements.objects.all():
        store = [i.img,i.topic,i.date_place]
        atc.append(store)
    
    certificates = []
    for i in certificate.objects.all():
        store = [i.img,i.topic,i.date_place]
        certificates.append(store)
    hackathon = []
    hack_count = 0
    winings = 0
    for i in hackthons.objects.all():
        store = [i.img,i.topic,i.sub_topic,i.date_place,i.team,i.result]
        print(i.result,hack_count)
        hack_count = hack_count + 1
        if i.result == 'win' or i.result == 'Win' or i.result == 'WIN' :
            winings = winings + 1
        hackathon.append(store)
    hack_detials = [hack_count,winings]
    roles_pos = Roles.objects.all()

    return render(request,'Modified_files/abt.html',{"repository":repository,"skill_r":skill_r,"skill_l":skill_l,"act" : atc,"certificate":certificates,"hackathon":hackathon,"hack_detials":hack_detials,'roles_pos':roles_pos})

@login_required(redirect_field_name='login')
def edit(request):
    full_data = projects.objects.all()
    skills = skill.objects.all()
    atc = atchviements.objects.all()
    cer = certificate.objects.all()
    res = resume.objects.all()
    hackathon = hackthons.objects.all()
    roles_pos = Roles.objects.all()
    for i in  Roles.objects.all():
        print(i.id)
    return render(request,'Modified_files/edit.html',{'data':full_data,'skill':skills,'atc':atc,'cer':cer,'hackathon':hackathon,'res':res,'roles_pos':roles_pos})

def del_skill(request):
    id = request.GET.get('id')
    delete_val = skill.objects.get(id=id)
    delete_val.delete()
    return render(request,'Modified_files/edit.html')

def delete_prj(request):
    id = request.GET.get('id')
    delete_val = projects.objects.get(id=id)
    delete_val.delete()
    return render(request,'Modified_files/edit.html')

def delete_atc(request):
    id = request.GET.get('id')
    delete_val = atchviements.objects.get(id=id)
    delete_val.delete()
    return render(request,'Modified_files/edit.html')

def delete_res(request):
    id = request.GET.get('id')
    delete_val = resume.objects.get(id=id)
    print(delete_val)
    delete_val.delete()
    return render(request,'Modified_files/edit.html')

def delete_cer(request):
    id = request.GET.get('id')
    print(id)
    delete_val = certificate.objects.get(id=id)
    delete_val.delete()
    return render(request,'Modified_files/edit.html')

def delete_role(request):
    id = request.GET.get('id')
    print(id)
    delete_val = Roles.objects.get(id=id)
    delete_val.delete()
    return render(request,'Modified_files/edit.html')

def delete_hackthons(request):
    id = request.GET.get('id')
    delete_val = hackthons.objects.get(id=id)
    delete_val.delete()
    return render(request,'Modified_files/edit.html')

def add_resume(request):
    img = request.GET.get('resume')
    save_val = resume(img=img,last_date=date.today())
    save_val.save()
    return render(request,'Modified_files/edit.html')


def save_skill(request):
    Persentage = request.GET['Persentage']
    lang = request.GET['lang']
    print(Persentage,lang)
    store_val = skill(language=lang,persentage=Persentage)
    store_val.save()
    return render(request,'Modified_files/blog.html')

def save_atchviements(request):
    title = request.GET['title']
    img = request.GET['img']
    date = request.GET['date']
    store_val = atchviements(img=img,topic=title,date_place=date)
    store_val.save()
    return render(request,'Modified_files/blog.html')

def save_project(request):
    title = request.GET['title']
    img = request.GET['img']
    date = request.GET['date']
    detials = request.GET['detials']

    store_val = projects(img=img,topic=title,date_place=date,paragraph=detials)
    store_val.save()
    return render(request,'Modified_files/blog.html')

def save_certificate(request):
    title = request.GET['title']
    img = request.GET['img']
    date = request.GET['date']
    store_val = certificate(img=img,topic=title,date_place=date)
    store_val.save()
    return render(request,'Modified_files/blog.html')

def save_roles(request):
    company = request.GET['title']
    img = request.GET['img']
    discrption = request.GET['dis']
    link = request.GET['link']
    store_val = Roles(img=img,company=company,discrption=discrption,link=link)
    store_val.save()
    return render(request,'Modified_files/blog.html')

def save_hackthons(request):
    title = request.GET['title']
    img = request.GET['img']
    date = request.GET['date']
    team = request.GET['team']
    sub_topic = request.GET['sub_topic']
    result = request.GET['result']

    store_val = hackthons(img=img,topic=title,date_place=date,sub_topic=sub_topic,team=team,result=result)
    store_val.save()
    return render(request,'Modified_files/blog.html')
