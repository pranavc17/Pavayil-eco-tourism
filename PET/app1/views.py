from datetime import datetime
from turtle import home
import datetime
from datetime import date
from django.shortcuts import redirect, render,HttpResponse
from requests import request
from django.core.files.storage import FileSystemStorage
from app1.models import resortreview
from app1.models import activityreview
from app1.models import activitybooking1
from app1.models import resortbooking1
from app1.models import homestaybooking1
from app1.models import traveller
from app1.models import homestay
from app1.models import resort
from app1.models import activity,idgen1,login

def sample(request):
    return render(request,"sample.html")
def login1(request):
    return render(request,"login1.html")    
def form(request):
    return render(request,"form.html") 
def index(request):
    return render(request,"index.html") 
def menubar(request):
    return render(request,"menubar.html")
def index_page(request):
    return render(request,"index-page.html")  
def admin_menu(request):
    return render(request,"admin_menu.html")  
def addactivity(request):
    data1 = idgen1.objects.get(id=1)
    id = data1.activity_id
    id = int(id+1)
    activity_id = "ACT_00" + str(id)
    request.session["activity_id"] = id
    return render(request,"addactivity_form.html",{'activity_id':activity_id})
  
                 
# def reg_form(request):
#     return render(request,"reg_form.html") 
def addact(request):
   
    if request.method=='POST':
        data=activity()
        data.activity_id=request.POST.get('id')
        data.activity_name=request.POST.get('name')
        data.description=request.POST.get('desc')
        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.photo=uploaded_file_url
        data.rate=request.POST.get('rate')
        data.status=request.POST.get('status')
        data.save()
       
        data1=idgen1.objects.get(id=1)
        data1.activity_id=request.session['activity_id']
        data1.save()
        return render(request,"admin_menu.html")  

def activity_table(request):
    data=activity.objects.all()
    return render(request,"act_table.html",{'data1':data})   

def removeactivity(request,id1):
    data=activity.objects.get(activity_id=id1)
    data.delete()
    return redirect("/activity_table")
def remlink(request):
    return render(request,"act_tabl.html")    
def viewacttable(request):
    data=activity.objects.all()
    return render(request,"view_act_table.html",{'data1':data})
def addresort(request):
    data1 = idgen1.objects.get(id=1)
    id = data1.resort_id
    id = int(id+1)
    resort_id = "RES_00" + str(id)
    request.session["resort_id"] = id
    return render(request,"addresort_form.html",{'resort_id':resort_id})  
def addresortaction(request):
   
    if request.method=='POST':
        data=resort()
        data.resort_id=request.POST.get('id')
        data.resort_name=request.POST.get('name')
        data.description=request.POST.get('desc')
        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.photo=uploaded_file_url
        data.location=request.POST.get('loc')
        data.contact=request.POST.get('number')
        data.status=request.POST.get('status')
        data.owner=request.POST.get('own')
        data.rate=request.POST.get('rate')
        data.save()

        data1=idgen1.objects.get(id=1)
        data1.resort_id=request.session['resort_id']
        data1.save()
        data2=login()
        data2.username=request.POST.get('id')
        data2.password=request.POST.get('number')
        data2.category="resort"
        data2.save()

        return render(request,"admin_menu.html")  
  
def resort_table(request):
       data=resort.objects.all()
       return render(request,"res_table.html",{'data1':data})            
def removeresort(request,id1):
        data=resort.objects.get(resort_id=id1)
        data.delete()
        data=login.objects.get(username=id1)
        data.delete()
        
        return redirect("/resort_table/") 
def viewrestable(request):
       data=resort.objects.all()
       return render(request,"view_res_table.html",{'data1':data})   
def addhomestay(request):
    data1 = idgen1.objects.get(id=1)
    id = data1.homestay_id
    id = int(id+1)
    homestay_id = "HOM_00" + str(id)
    request.session["homestay_id"] = id
    return render(request,"addhomestay_form.html",{'homestay_id':homestay_id})              
def addhomestayaction(request):
   if request.method=='POST':
        data=homestay()
        data.homestay_id=request.POST.get('id')
        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.photo=uploaded_file_url
        data.house_name=request.POST.get('name')
        data.roof=request.POST.get('roof')
        data.description=request.POST.get('desc')
        data.food=request.POST.get('food')
        data.owner=request.POST.get('own')
        data.contact=request.POST.get('contact')
        data.rate=request.POST.get('rate')
        data.status=request.POST.get('status')
        data.save()

        data1=idgen1.objects.get(id=1)
        data1.homestay_id=request.session['homestay_id']
        data1.save()

        data2=login()
        data2.username=request.POST.get('id')
        data2.password=request.POST.get('contact')
        data2.category="homestay"
        data2.save()

        return render(request,"admin_menu.html")  
def homestay_table(request):
       data=homestay.objects.all()
       return render(request,"hom_table.html",{'data1':data})  
def removehomestay(request,id1):
        data=homestay.objects.get(homestay_id=id1)
        data.delete()
        data=login.objects.get(username=id1)
        data.delete()
        return redirect("/homestay_table/")  
def viewhomtable(request):
       data=homestay.objects.all()
       return render(request,"view_hom_table.html",{'data1':data})                
def publicview(request):
    return render(request,"public_menu.html")  
def justview(request):
    data=activity.objects.all()
    data1=resort.objects.all()
    data2=homestay.objects.all()
    return render(request,"justview.html",{'data1':data,'data2':data1,'data3':data2})  
def sample(request):
    return render(request,"sample.html")     
def log(request):
    if request.method == 'POST':
        dataa=login.objects.all()
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        
        flag=0
            
        for da in dataa:
            if un == da.username and pwd == da.password:
                type=da.category
                
                flag = 1
                if type=="admin":
                    request.session['admin_id']=un
                    return redirect('/admin_menu')   
                elif type=="resort":
                    request.session['resort_id']=un
                    return redirect('/resort_menu') 
                elif type=="traveller":
                    request.session['traveller_id']=un
                    return redirect('/trav_menu')     
                elif type=="homestay":
                    request.session['homestay_id']=un
                    return redirect('/homestay_menu')  
                
                else:
                    return HttpResponse("Invalid accout type")
        if flag==0:
            return HttpResponse("Invalid user")        


def resort_menu(request):
    return render(request,"resort_menu.html")
def homestay_menu(request):
    return render(request,"homestay_menu.html")    
def loginlink(request):
    return render(request,"login1.html") 
def editresort(request):
    r=request.session['resort_id']
    data=resort.objects.get(resort_id=r)
    return render(request,"editresort.html",{'data':data} ) 
def editresort2(request,id1):
    if request.POST.get('photo')=="":
        
        data=resort.objects.get(resort_id=id1)
        data.resort_name=request.POST.get('name')
        data.location=request.POST.get('loc')
        data.description=request.POST.get('desc')
        data.contact=request.POST.get('contact')
        data.status=request.POST.get('status')
        data.owner=request.POST.get('own')
        data.save()

        data2=login.objects.get(username=id1)
        data2.username=request.POST.get('id')
        data2.password=request.POST.get('contact')
        data2.category="resort"
        data2.save()
    else:
        data=resort.objects.get(resort_id=id1)
        data.resort_name=request.POST.get('name')
        data.location=request.POST.get('loc')
        data.description=request.POST.get('desc')
        data.contact=request.POST.get('contact')
        data.status=request.POST.get('status')
        data.owner=request.POST.get('own')
        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.photo=uploaded_file_url    
        data.save()

        data2=login.objects.get(username=id1)
        data2.username=request.POST.get('id')
        data2.password=request.POST.get('contact')
        data2.category="resort"
        data2.save()
    return redirect('/editresort')    
def edithomestay(request):
    r=request.session['homestay_id']
    data=homestay.objects.get(homestay_id=r)
    return render(request,"edithomestay.html",{'data':data} )    
def edithomestay2(request,id1):
    if request.POST.get('photo')=="":
        
        data=resort.objects.get(homestay_id=id1)
        data.house_name=request.POST.get('name')
        data.location=request.POST.get('loc')
        data.roof=request.POST.get('roof')
        data.description=request.POST.get('desc')
        data.food=request.POST.get('food')
        data.contact=request.POST.get('contact')
        data.status=request.POST.get('status')
        data.owner=request.POST.get('own')
        data.save()
    else:
        data=resort.objects.get(homestay_id=id1)
        data.resort_name=request.POST.get('name')
        data.location=request.POST.get('loc')
        data.roof=request.POST.get('roof')
        data.description=request.POST.get('desc')
        data.food=request.POST.get('food')
        data.contact=request.POST.get('contact')
        data.status=request.POST.get('status')
        data.owner=request.POST.get('own')
        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.photo=uploaded_file_url    
        data.save()
    return redirect('/edithomestay')
def trav_activity(request):
    data=activity.objects.all()
    return render(request,"trav_activity.html",{'data1':data})      
def trav_resort(request):
    data1=resort.objects.all()
    return render(request,"trav_resort.html",{'data2':data1})   
def trav_homestay(request):
    data2=homestay.objects.all()
    return render(request,"trav_homestay.html",{'data3':data2})   
def trav_menu(request):
    return render(request,"trav_menu.html") 
def addtraveller(request):
    data1 = idgen1.objects.get(id=1)
    id = data1.traveller_id
    id = int(id+1)
    traveller_id = "TVLR_00" + str(id)
    request.session["traveller_id"] = id
    return render(request,"signup.html",{'traveller_id':traveller_id})  
def addtravelleraction(request):
   if request.method=='POST':
        data=traveller()
        data.traveller_id=request.POST.get('id')
        data.first_name=request.POST.get('first_name')
        data.last_name=request.POST.get('last_name')
        data.country=request.POST.get('country')
        data.state=request.POST.get('state')
        data.district=request.POST.get('district')
        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.id_proof=uploaded_file_url
        data.contact=request.POST.get('contact')
        data.email=request.POST.get('email')
        data.save()

        data1=idgen1.objects.get(id=1)
        data1.traveller_id=request.session['traveller_id']
        data1.save()

        data2=login()
        data2.username=request.POST.get('id')
        data2.password=request.POST.get('contact')
        data2.category="traveller"
        data2.save()

        return render(request,"trav_menu.html")  
def homestaybooking(request,id1):
    
    data1 = idgen1.objects.get(id=1)
    id = data1.homestaybooking_id
    id = int(id+1)
    homestaybooking_id = "HBK_00" + str(id)
    request.session["homestaybooking_id"] = id
    
    

    return render(request,"homestaybooking.html",{'data1':homestaybooking_id,'id1':id1,'data4':request.session["traveller_id"]})
def homestaybookingaction(request):
    if request.method=='POST':
        data=homestaybooking1()
        data.homestaybooking_id=request.POST.get('id')
        data.homestay_id_id=request.POST.get('homestay_id')
        data.traveller_id_id=request.POST.get('traveller_id')
        data.booking_date=request.POST.get('date')
        data.no_of_days=request.POST.get('days')
        data.no_of_person=request.POST.get('person')
        data.status="pending"
       
        data.save()
        data1=idgen1.objects.get(id=1)
        data1.homestaybooking_id=request.session['homestaybooking_id']
        data1.save()
    return render(request,"trav_menu.html") 

def resortbooking(request,id1):
    
    data1 = idgen1.objects.get(id=1)
    id = data1.resortbooking_id
    id = int(id+1)
    resortbooking_id = "RBK_00" + str(id)
    request.session["resortbooking_id"] = id
    
    

    return render(request,"resortbooking.html",{'data1':resortbooking_id,'id1':id1,'data4':request.session["traveller_id"]})

def resortbookingaction(request):
    if request.method=='POST':
        data=resortbooking1()
        data.resortbooking_id=request.POST.get('id')
        data.resort_id_id=request.POST.get('resort_id')
        data.traveller_id_id=request.POST.get('traveller_id')
        data.booking_date=request.POST.get('date')
        data.no_of_days=request.POST.get('days')
        data.no_of_person=request.POST.get('person')
        data.status="pending"
       
        data.save()
        data1=idgen1.objects.get(id=1)
        data1.resortbooking_id=request.session['resortbooking_id']
        data1.save()
    return render(request,"trav_menu.html")     

def activitybooking(request,id1):
    
    data1 = idgen1.objects.get(id=1)
    id = data1.activitybooking_id
    id = int(id+1)
    activitybooking_id = "ABK_00" + str(id)
    request.session["activitybooking_id"] = id
    
    

    return render(request,"activitybooking.html",{'data1':activitybooking_id,'id1':id1,'data4':request.session["traveller_id"]})

def activitybookingaction(request):
    if request.method=='POST':
        data=activitybooking1()
        data.activitybooking_id=request.POST.get('id')
        data.activity_id_id=request.POST.get('activity_id')
        data.traveller_id_id=request.POST.get('traveller_id')
        data.booking_date=request.POST.get('date')
        data.no_of_days=request.POST.get('days')
        data.no_of_person=request.POST.get('person')
        data.status="pending"
        data.save()
        data1=idgen1.objects.get(id=1)
        data1.activitybooking_id=request.session['activitybooking_id']
        data1.save()
    return render(request,"trav_menu.html")

def viewactivitybkselect(request):
    data=activity.objects.all()
    return render(request,"view_act_bkselect.html",{'data':data})  



def viewactivitybookingbooking1action(request):
    a=request.POST.get('activityname')
    request.session['a1']=a
    data=activitybooking1.objects.filter(activity_id_id=a)
    return render(request,"view_act_booking.html",{'data':data})      

def acceptact(request,id):
    data=activitybooking1.objects.get(activitybooking_id=id)
    data.status="Accepted"
    data.save()
    a=request.session['a1']
    data1=activitybooking1.objects.filter(activity_id_id=a)
    return render(request,"view_act_booking.html",{'data':data1})      

def rejectact(request,id):
    data=activitybooking1.objects.get(activitybooking_id=id)
    data.status="Rejected"
    data.save()
    a=request.session['a1']
    data1=activitybooking1.objects.filter(activity_id_id=a)
    return render(request,"view_act_booking.html",{'data':data1})    

def viewresortbooking(request):
    data=resortbooking1.objects.filter(resort_id_id=request.session['resort_id'])
    return render(request,"view_res_booking.html",{'data':data})  

def acceptres(request,id):
    data=resortbooking1.objects.get(resortbooking_id=id)
    data.status="Accepted"
    data.save()
    a=request.session['resort_id']
    data1=resortbooking1.objects.filter(resort_id_id=a)
    return render(request,"view_res_booking.html",{'data':data1})      

def rejectres(request,id):
    data=resortbooking1.objects.get(resortbooking_id=id)
    data.status="Rejected"
    data.save()
    a=request.session['a1']
    data1=resortbooking1.objects.filter(resort_id_id=request.session['resort _id'])
    return render(request,"view_res_booking.html",{'data':data1})    

def viewhomestaybooking(request):
    data=homestaybooking1.objects.filter(homestay_id_id=request.session['homestay_id'])
    return render(request,"view_hom_booking.html",{'data':data})      

def accepthom(request,id):
    data=homestaybooking1.objects.get(homestaybooking_id=id)
    data.status="Accepted"
    data.save()
    a=request.session['homestay_id']
    data1=homestaybooking1.objects.filter(homestay_id_id=a)
    return render(request,"view_hom_booking.html",{'data':data1})      

def rejecthom(request,id):
    data=homestaybooking1.objects.get(homestaybooking_id=id)
    data.status="Rejected"
    data.save()
    a=request.session['a1']
    data1=homestaybooking1.objects.filter(homestay_id_id=request.session['homestay_id'])
    return render(request,"view_hom_booking.html",{'data':data1})    

def justviewhomestaybooking(request):
    data=homestaybooking1.objects.all()
    return render(request,"justviewhomestaybooking.html",{'data':data}) 
def justviewresortbooking(request):
    data=resortbooking1.objects.all()
    return render(request,"justviewresortbooking.html",{'data':data})

def actresponse(request):
    data=activitybooking1.objects.filter(traveller_id=request.session['traveller_id'])
    return render(request,"act_response.html",{'data':data})    
def resresponse(request):
    data=resortbooking1.objects.filter(traveller_id=request.session['traveller_id'])
    return render(request,"res_response.html",{'data':data})     
def homresponse(request):
    data=homestaybooking1.objects.filter(traveller_id=request.session['traveller_id'])
    return render(request,"hom_response.html",{'data':data})   

def travellerlogout(request):
    del request.session['traveller_id']
    return render(request,"login1.html") 

def trav_homestay_logout(request):
    del request.session['traveller_id']
    return render(request,"login1.html") 
def trav_resort_logout(request):
    del request.session['traveller_id']
    return render(request,"login1.html") 
def trav_activity_logout(request):
    del request.session['traveller_id']
    return render(request,"login1.html") 

def homestay_menu_logout(request):
    del request.session['homestay_id']
    return render(request,"login1.html")     

def act_review(request,id1):
    print("dddddddddddddddddddddddddddddddddddddddd")
    print(id1)
    data1 = idgen1.objects.get(id=1)
    id = data1.act_review_id
    id = int(id+1)
    act_review_id = "ACTRW_00" + str(id)
    request.session['act_review_id'] = id
    request.session['activity_id'] = id1
    request.session['review_id'] =  act_review_id 
    return render(request,"act_review.html",{'data':act_review_id})  
def act_reviewaction(request):
   if request.method=='POST':
        data=activityreview()
        data.act_review_id=request.session['review_id']
        data.review=request.POST.get('review')
        data.traveller_id_id=request.session['traveller_id']
        data.activity_id_id=request.session['activity_id']
        print("ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        print(request.session['activity_id'])
        data.review_date=datetime.datetime.now().strftime("%y-%m-%d")
        
        data.save()
        data1=idgen1.objects.get(id=1)
        data1.act_review_id=request.session['act_review_id']
        data1.save()
        id = data1.act_review_id
        id = int(id+1)
        act_review_id = "ACTRW_00" + str(id)
        request.session['act_review_id'] = id
        request.session['review_id'] =  act_review_id 
        data3=activityreview.objects.all()
        return render(request,"act_review.html",{'data':act_review_id,'data':data3})                             
                           
def res_review(request,id1):
    
    data1 = idgen1.objects.get(id=1)
    id = data1.res_review_id
    id = int(id+1)
    res_review_id = "RESRW_00" + str(id)
    request.session['res_review_id'] = id
    request.session['resort_id'] = id1
    request.session['review_id'] =  res_review_id 
    return render(request,"res_review.html",{'data':res_review_id})                             

def hom_review(request,id):
    return render(request,"hom_review.html") 
def adminlogout(request):
    del request.session['admin_id'] 
    return render(request,"login1.html")    
def gotohom(request):
    return render(request,"admin_menu.html")                                
def contact(request):
    return render(request,"contact.html")                                                                                  
def res_reviewaction(request):
   if request.method=='POST':
        data=resortreview()
        data.res_review_id=request.session['review_id']
        data.review=request.POST.get('review')
        data.traveller_id_id=request.session['traveller_id']
        data.resort_id_id=request.session['resort_id']
        
        data.review_date=datetime.datetime.now().strftime("%y-%m-%d")
        
        data.save()
        data1=idgen1.objects.get(id=1)
        data1.res_review_id=request.session['res_review_id']
        data1.save()
        id = data1.res_review_id
        id = int(id+1)
        res_review_id = "RESRW_00" + str(id)
        request.session['res_review_id'] = id
        request.session['review_id'] =  res_review_id 
        data3=resortreview.objects.all()
        return render(request,"res_review.html",{'data':res_review_id,'dataa':data3})                          