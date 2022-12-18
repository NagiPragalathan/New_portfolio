from django.shortcuts import render, redirect
import requests
from .models import projects, skill, atchviements, certificate, hackthons
# Create your views here.

def home(request):
    return render(request,'Modified_files/sample.html')

def blog(request):
    project = [["https://imgs.search.brave.com/DaF2J-lw_q55hmQePzAqxD4R1HTalI2o8xRKDtSofqY/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9oZHdh/bGxwYXBlcmltLmNv/bS93cC1jb250ZW50/L3VwbG9hZHMvMjAx/Ny8wOC8yMi84Njkx/MC1hbmltZS1saWdo/dGhvdXNlLWZsb2F0/aW5nX2lzbGFuZC5q/cGc","title","date","para"]]
    return render(request,'Modified_files/blog.html',{'project':project})

def about(request):

    github_username  = "NagiPragalathan"   #specify your User name

    #api url to grab public user repositories
    api_url = f"https://api.github.com/users/{github_username}/repos"

    #send get request
    response = requests.get(api_url)
    #get the json data
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
    for i in hackthons.objects.all():
        store = [i.img,i.topic,i.sub_topic,i.date_place,i.team,i.result]
        hackathon.append(store)
    return render(request,'Modified_files/abt.html',{"repository":repository,"skill_r":skill_r,"skill_l":skill_l,"act" : atc,"certificate":certificates,"hackathon":hackathon})

def edit(request):
    full_data = projects.objects.all()
    skills = skill.objects.all()
    atc = atchviements.objects.all()
    cer = certificate.objects.all()
    hackathon = hackthons.objects.all()
    return render(request,'Modified_files/edit.html',{'data':full_data,'skill':skills,'atc':atc,'cer':cer,'hackathon':hackathon})

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

def delete_cer(request):
    id = request.GET.get('id')
    delete_val = certificate.objects.get(id=id)
    delete_val.delete()
    return render(request,'Modified_files/edit.html')

def delete_hackthons(request):
    id = request.GET.get('id')
    delete_val = hackthons.objects.get(id=id)
    delete_val.delete()
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
