import datetime
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from MYAPP.models import *

# Create your views here.

def launching(request):
    return render(request,'launching.html')



#---------------Product


def add_product(request):
    return render(request, 'product/add_prduct.html')

def product_post(request):
    name = request.POST['textfield']
    descr = request.POST['textarea']
    branD = request.POST['select']
    pricE = request.POST['textfield2']
    photo = request.FILES['fileField']
    fs = FileSystemStorage()
    s = datetime.datetime.now().strftime("%y%m%d%H%M%S") + ".jpg"
    fn = fs.save(s, photo)
    pobj = product()
    pobj.productname = name
    pobj.description = descr
    pobj.photo = fs.url(s)
    pobj.price =pricE
    pobj.BRAND = branD
    pobj.save()
    return redirect('/myapp/product/')


def view_product(request):
    res = product.objects.all()
    return  render(request,'product/view_product.html',{'data':res})

def delete_product(request,id):
    res = product.objects.get(id=id).delete()
    return redirect('/myapp/view_product/')


def edit_product(request,id):
    res = product.objects.get(id=id)
    return render(request,'product/edit.html',{'data':res})

def edit_post(request):
    pid = request.POST['pid']
    productname = request.POST['textfield']
    description = request.POST['textarea']
    brand = request.POST['select']
    price = request.POST['textfield2']
    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        if photo.name != '':
            fs = FileSystemStorage()
            s = datetime.datetime.now().strftime("%y%m%d%H%M%S") + ".jpg"
            fn = fs.save(s, photo)
            res = product.objects.filter(pk=pid).update(productname=productname, description=description,
                                                        BRAND=brand, price=price, photo=s)
        else:
            res = product.objects.filter(pk=pid).update(productname=productname, description=description,
                                                        BRAND=brand, price=price)
    else:
        res = product.objects.filter(pk=pid).update(productname=productname, description=description, BRAND=brand,
                                                    price=price)
    return HttpResponse('''<script>alert('Update Successfully');window.location="/myapp/view_product/"</script>''')



def loginfun(request):
    return render(request,'login.html')

def login_post(request):
    uname = request.POST['Email']
    pwrd = request.POST['Password']
    if login.objects.filter(username=uname, password=pwrd).exists():
        lg = login.objects.get(username=uname, password=pwrd)
        if lg.type == 'user':
            request.session['id'] = lg.id
            print("LOgIN ID",request.session['id'])
            return redirect(home)
        else:
            print(type)
            return HttpResponse("<script>alert('User Not Found');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert('User Not Found');window.location='/myapp/login/'</script>")




def signup(request):
    return render(request,'signup.html')

def signup_post(request):
    uname = request.POST['Name']
    email = request.POST['Email']
    phone = request.POST['phone']
    pswrd = request.POST['Password']
    cnfpswrd = request.POST['Password2']

    lobj = login()
    lobj.username = email
    lobj.password = cnfpswrd
    lobj.type = 'user'
    lobj.save()

    sobj = user()
    sobj.name = uname
    sobj.email = email
    sobj.phone = phone
    sobj.LOGIN = lobj
    sobj.save()

    return HttpResponse('''<script>alert('Signup Successfully');window.location="/myapp/login/"</script>''')

def home(request):
    return render(request,'home.html')


def userproduct(request):
    res = product.objects.all()
    return render(request,'userproduct.html',{'data':res})


def addtocart(request,id):
    res = product.objects.get(id=id)
    return render(request,'addto_Cart.html',{'data':res})

def cartpost(request):
    lid = request.session['id']
    pid = request.POST['h1']
    qty = request.POST['q1']
    cobj = cart()
    cobj.quantity = qty
    cobj.PRODCUT_id = pid
    cobj.USER = user.objects.get(LOGIN_id=lid)
    cobj.date = datetime.datetime.now()
    cobj.save()
    return redirect(userproduct)

def viewcart(request):
    lid =request.session['id']
    res = cart.objects.filter(USER_id=user.objects.get(LOGIN_id=lid))
    tot=0.0
    tam=0.0

    for i in res:

        tot=float(i.quantity) * float(i.PRODCUT.price)
        tam += tot
    return render(request,'mycart.html',{'data':res,'tot':tam})

def deletcart(request,id):
    res = cart.objects.get(id=id).delete()
    return redirect(viewcart)


def ajax_add_qty(request):
    cid = request.POST['p']
    lid = request.session['id']
    res = cart.objects.get(USER_id=user.objects.get(LOGIN_id=lid),id=cid)
    res.quantity=int(res.quantity)+1
    res.save()
    return JsonResponse({'status':'ok'})

def ajax_sub_qty(request):
    cid = request.POST['mmmm']
    res = cart.objects.get(id=cid)
    if res.quantity == 1:
        res = cart.objects.get(id=cid)
        res.delete()
    else:
        res.quantity=int(res.quantity)-1
        res.save()
    return JsonResponse({'status':'ok'})
    # return redirect(viewcart)




def viewcart_ajax(request):
    lid =request.session['id']
    res = cart.objects.filter(USER_id=user.objects.get(LOGIN_id=lid))
    tot=0.0
    l=[]
    tam=0.0
    for i in res:
        tot = float(i.quantity) * float(i.PRODCUT.price)
        l.append({'id':i.id,'producname':i.PRODCUT.productname,'photo':i.PRODCUT.photo,'price':i.PRODCUT.price,'qty':i.quantity,'total':tot})

        tam += tot
    return JsonResponse({'status': 'ok','data':l,'tot':tam})


#Need to create view function in ajax for that we need to pass data through json dont do anything