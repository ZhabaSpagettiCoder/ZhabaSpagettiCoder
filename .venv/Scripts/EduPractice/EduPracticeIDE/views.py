from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from .models import Inputdatauser, Typesofusers, Inputdatarequests, Techt
import json
import random
import datetime
# Create your views here.

#Раздел маршрутизации
def index(request, name):
    if name == 11:
        return HttpResponse("Main")
    else:
        return HttpResponse(f"Error {name}")
def uwu(request, name, age):
    host = request.META["HTTP_HOST"]
    pidr = request.META["HTTP_USER_AGENT"]
    return HttpResponse(f"О пользователе:<p>Имя:<b>{name}<b><p><p>Возраст:{age} <p><p>{host} {pidr}<p>")

def advancedUwU(request):
    Did = request.GET.get("dick",0) #Второй параметр - перегрузка стандартным значением, если не поступило оригинального
    Hd = request.GET.get("head","less") #?dick=text&head=text
    if Hd != "less":    
        return HttpResponse(f"<p><b>My horse is {Did}<b><p> <p><h1>but..<h1><p> <p><b>your horse is {Hd}<b><p>")
    else:
        return HttpResponseBadRequest("Bad entered data, please, try later") #Возвращает ошибку типа 400
    #https://metanit.com/python/django/3.5.php - все виды ошибок

def noncluded(request):
    return HttpResponse(F"Ещё не вложеное")
def included(request):
    return HttpResponse(f"Вложенное")
def redirected(request):
    return HttpResponseRedirect("/UwUs") #Импорт из http HRR. Перенаправляет на другую страницу
#Конец раздела маршрутизации

#Раздел Куки
def CookieThumper(request):
    User = request.GET.get("usr","UNDEFIEND")
    resp = HttpResponse(f"Hello {User}")
    resp.set_cookie("Username",User)
    return resp
def CookieTaker(request):
    User = request.COOKIES["Username"]
    return HttpResponse(f"Hello, {User}")
#Конец раздела Куки

#Следующая разработка проходят в файле settings.py
#Ура, UI!
def StartPage(request):
    return render(request, "Auth.html")

def Registration(request):
    return render(request, "Reg.html")

def DBRegResponse(request):
    FullName = request.POST.get("FullName") 
    Log = request.POST.get("Email")
    Phone = request.POST.get("PhoneNumber")
    Passw = request.POST.get("Password1")
    Type = Typesofusers.objects.get(id = '0')
    DIC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    idd = ""
    for i in range(3):
        idd += DIC[random.randrange(0,26)]
    Newie = Inputdatauser.objects.create(fio = FullName, phone = Phone, login = Log, password = Passw, type = Type, ID = idd)
    Newie.save()
    return HttpResponse("Registration end successfull")

def Menu(request):
    log = request.GET.get("hash")
    Data = request.COOKIES.get("Data")
    Data = json.loads(Data)
    if log == "0":    
        req = Inputdatarequests.objects.filter(clientid=Data[5]).values_list()
        reqL = list()
        for i in req:
            drop = list()
            for j in i:
                drop.append(j)
            drop.pop(7)
            drop[7] = list(Inputdatauser.objects.filter(ID=drop[7]).values_list()[0])[0]
            addInfo = list(Techt.objects.filter(id = drop[4]).values_list()[0])[2]
            drop[4] = addInfo
            reqL.append(drop)
        print(reqL)
        return render(request, "PanelView.html", context={"FIO":Data[0], "Phone":Data[1],"Email":Data[2],"Type": "Пользователь", "request": reqL})
    if log == "3":
        req = Inputdatarequests.objects.all().values_list()
        reqL = list()
        for i in req:
            drop = list()
            for j in i:
                drop.append(j)
            drop.pop(8),drop.pop(7),drop.pop(6),drop.pop(5),drop.pop(3), drop.pop(2), drop.pop(1)
            addInfo = list(Techt.objects.filter(id = drop[1]).values_list()[0])[1]
            drop[1] = addInfo
            reqL.append(drop)
        return render(request, "AdminPanel.html", context={"FIO":Data[0], "Phone":Data[1],"Email":Data[2],"Type": "Администратор","request":reqL})
    else: return HttpResponse("Error")
        
def AuthTry(request):
    pasw = request.POST.get('pass')
    Login = request.POST.get("login")
    try:    
        Check = AutoGetDataFromDB(Login)
    except(IndexError): return HttpResponse("Can't find login in Database. Please, check your spell")
    print(Check)
    if pasw == Check[3]:
        resp = HttpResponseRedirect(f"Menu/?hash={Check[4]}")
        resp.set_cookie("Data",json.dumps(Check))
        return resp
    else: return HttpResponse("Password is incorrect!")
    
def AutoGetDataFromDB(log):
    Check = Inputdatauser.objects.filter(login=log)
    Check = list(Check.values_list())
    Check = Check[0]
    return Check

def Add(request):
    return render(request, "RequestUser.html")

def AddSuper(request):
    return render(request, "RequestAdmin.html")

def DBAddAdminResponse(request):
    de = request.POST.get("description")
    na = request.POST.get("name")
    ty = request.POST.get("type")
    idm = request.POST.get("masterID")
    idc = request.POST.get("clientID")
    dt = request.POST.get("date")
    prt = request.POST.get("parts")
    stts = request.POST.get("status")
    Techid = Techt.objects.get_or_create(orgtechtype = ty, orgtechmodel = na)
    Data = request.COOKIES.get("Data")
    Data = json.loads(Data)
    Typeof = Typesofusers(id = 0)
    usr = Inputdatauser(fio=Data[0], phone= Data[1], login = Data[2], password = Data[3], type = Typeof, ID = Data[5])
    Techid = Techt(id = list(Techt.objects.filter(orgtechtype = ty, orgtechmodel = na).values_list()[0])[0])
    print(Techid, usr.ID)
    NewRequest = Inputdatarequests.objects.create(startdate = datetime.date.today(),
                            problemdescryption = de,
                            requeststatus = stts, 
                            techid = Techid, 
                            completiondate = dt, 
                            repairparts = prt, 
                            clientid = idc, 
                            masterid = idm)
    print(NewRequest)
    return HttpResponse("Your request is now in proceed")

def DBAddResponse(request):
    de = request.POST.get("description")
    na = request.POST.get("name")
    ty = request.POST.get("type")
    Techid = Techt.objects.get_or_create(orgtechtype = ty, orgtechmodel = na)
    Data = request.COOKIES.get("Data")
    Data = json.loads(Data)
    Typeof = Typesofusers(id = 0)
    usr = Inputdatauser(fio=Data[0], phone= Data[1], login = Data[2], password = Data[3], type = Typeof, ID = Data[5])
    Techid = Techt(id = list(Techt.objects.filter(orgtechtype = ty, orgtechmodel = na).values_list()[0])[0])
    print(Techid, usr.ID)
    NewRequest = Inputdatarequests.objects.create(startdate = datetime.date.today(),
                            problemdescryption = de,
                            requeststatus = "Регистрация заявки", 
                            techid = Techid, 
                            completiondate = None, 
                            repairparts = None, 
                            clientid = usr.ID, 
                            masterid = usr.ID)
    print(NewRequest)
    return HttpResponse("Your request is now in proceed")

def InfoShow(request):
    row = int(request.GET.get("id"))
    Data = Inputdatarequests.objects.all().values_list()[row-1]
    return render(request, "Info.html", context={"request":Data[0],"date":Data[1],"comment":Data[2],"status":Data[3],"tech":Data[4],"enddate":Data[5],"parts":Data[6],"clientID":Data[7],"masterID":Data[8]})

def Submit(request):
    request_number = request.POST.get('request')
    creation_date = request.POST.get('creationDate')
    comment = request.POST.get('comment')
    status = request.POST.get('status')
    completion_date = request.POST.get('completionDate')
    parts = request.POST.get('parts')
    id_master = request.POST.get('idmaster')
    id_user = request.POST.get('iduser')
    techt = Techt.objects.get(id = request.POST.get('equipment'))
    # Например, если у вас есть модель Request:
    req = Inputdatarequests.objects.get(requestid=request_number)
    req.startdate = creation_date
    req.problemdescryption= comment
    req.requeststatus= status
    req.techid = techt
    req.completiondate = completion_date
    req.repairparts= parts
    req.masterid= id_master
    req.clientid= id_user
    req.save()
    return HttpResponse("Edition end successfuly")

def Delete(request):
    request_number = request.GET.get('id')
    print("\n\n\n" + request_number +"\n\n\n")
    Inputdatarequests.objects.get(requestid = request_number).delete()
    return HttpResponse(f"Request №{request_number} was deleted")