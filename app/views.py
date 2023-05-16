from multiprocessing import context
import os
from unicodedata import category
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login
from app.models import Notes,Category,Cart,Tutor




# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    catgrs = Category.objects.all()
    context={
        'catgrs':catgrs,
    }
    return render(request,'signup.html',context)
   

def loginpage(request):
    return render(request,'login.html') 

def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        img=request.FILES['image']
        catgors = request.POST.get('category')
        cts = Category.objects.get(id=catgors)

        if password==cpassword:  
            if User.objects.filter(username=username).exists(): #check Username Already Exists..
                messages.info(request, 'This username already exists!!!!!!')
              
                return redirect('signup')
            else:
                user1=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
            
                imags = Cart(category=cts,photo=img,user=user1)
                image2 = Tutor(user=user1)
                imags.save()
                image2.save()
                

                #messages.info(request, 'SuccessFully completed.......')
                print("Successed...")
        else:
            messages.info(request, 'Password doesnt match!!!!!!!')
            print("Password is not Matching.. ") 
            return redirect('signup')   
        return redirect('loginpage')
    else:
        return render(request,'signup.html')



def userlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'Welcome {username}')
                return render(request,'home.html', {'std':user})
                    # return redirect('userhomepage')
        else:
            messages.info(request,'Invalid username and password')
            return redirect('loginpage')
    else:
        return render(request,'login.html')


def product(request):
    return render(request,'addproduct.html')



def profile(request):
	currentuser = Cart.objects.all()
	return render(request, 'profile.html', {'user1': currentuser})

def profileuser(request):
	currentuser = Cart.objects.all()
	return render(request, 'profileuser.html', {'user1': currentuser})




def deletedetails(request,pk):
    stud=User.objects.get(id=pk)
    stud.delete()
    # stud.course.delete()
    return redirect('profile')





def logout(request):
	auth.logout(request)
	return redirect('home')


def addcategory(request):
    return render(request,'addcategory.html')


def add_category(request):
    if request.method=='POST':
        cors=request.POST['cate']

        print(cors)
        crs=Category(category_name=cors)
        crs.save()
        print("hii")
        return redirect('addimage')


def addimage(request):
    catgrs = Category.objects.all()
    context={
        'catgrs':catgrs,
    }
    return render(request,'add.html',context)



def add(request):
    if request.method == 'POST':
        catgors = request.POST.get('category')
        cts = Category.objects.get(id=catgors)
        img = request.FILES.get('image')
        desc = request.POST.get('desc')
        name = request.POST.get('name')
        
        imags = Notes(category=cts,image=img,subject=name,description=desc)
        imags.save()
       
        

        print("save")
        return redirect('gallery')
    return render(request,'add.html')



def gallery(request):
    ctgs = request.GET.get('category')
    imgs = Notes.objects.all()
    if ctgs is not None:
        imgs =  Notes.objects.filter(category__category_name=ctgs)
    catgrs = Category.objects.all()
    
    context = {
        'catgrs':catgrs,
        'imgs':imgs,
        }
    return render(request,'gallery.html',context)





def showimage(request,pk):
    img =  Notes.objects.get(id=pk)

    context={
        'img':img,
    }
    return render(request,'image.html',context)


def show(request):
    imgs =  Notes.objects.all()
    context = {
        'img':imgs
        }
    return render(request,'base.html',context)


#def addcart(request,pk,k):
    #cart = Cart.objects.get(id=pk)
    #context = { 'cart':cart }
    #return render(request,'cart.html',context)


def cartitem(request,pk,k):
    cartprod= Notes(id=pk)
    cartuser= User(id=k)
    t=Cart(product=cartprod,user=cartuser)
    t.save()
    return redirect('home')


def loadcartitems(request,pk):
    ctgs = request.GET.get('category')

    c=Cart.objects.filter(user=pk)
    b=Notes.objects.filter(category__category_name = ctgs)
    context = {
        'cartitems':c,
        'b':b

    }
    return render(request,'cart.html',context)


#def ordered_items(request):
    #item=Cart.objects.all()
    #return render(request,'item.html',{'item':item})

    




def addTutors(request):
    
    if request.method == 'POST':
            name = request.POST['name']
            address=request.POST['address']
            phone=request.POST['phone']
            subject=request.POST['subject']
            catgors = request.POST.get('category')
            cts = Category.objects.get(id=catgors)
            if request.FILES.get('file') is not None:
                image=request.FILES['file']
            else:
                image="static/image/default.png"
            
            tut=Tutor(name=name,address=address,phone=phone,subject=subject,image=image,category=cts)
            tut.save()
            print("hiii")
            return redirect('showTutors')
    return render(request,'addtutor.html')


def showTutors(request):
    tut = Tutor.objects.all()
    u=Cart.objects.all()
    ct=u.category
    c=User.objects.filter(category = ct)
    context = {'std':c,
    'tut':tut }

    return render(request,'showtutor.html',context)


def delete_tutors(request,pk):
    tut=Tutor.objects.get(id=pk)
    tut.delete()
    return redirect('showTutors')


def edit_tutor_page(request,pk):
    t=Tutor.objects.get(id=pk)
    return render(request,'edittutors.html',{'t':t})

    
def edit_tutor_data(request,pk):
    if request.method=='POST':
        tut = Tutor.objects.get(id=pk)
        tut.name = request.POST.get('name')
        tut.address = request.POST.get('address')
        tut.phone = request.POST.get('phone')
        tut.subject = request.POST.get('subject')
        if request.FILES.get('file') is not None:
            if not tut.image == "static/image/default.png":
                os.remove(tut.image.path)
                tut.image = request.FILES['file']
            else:
                tut.image = request.FILES['file']
        else:
            os.remove(tut.image.path)
            tut.image = "static/image/default.png" 
        tut.save()
        return redirect('showTutors')
    return render(request, 'edit_tutors.html')









#Notes
def up(request):
    u=Cart.objects.get(user=request.user)
    return render(request,'up.html',{'u':u })

def mn(request,pk):
    u=Cart.objects.get(user=pk)
    ct=u.category
    c=Notes.objects.filter(category = ct)
    return render(request,'cart.html',{'std':c})



def students(request):
    u=Tutor.objects.all()
    ct=u.category
    c=Cart.objects.filter(category = ct)
    return render(request,'showtutor.html',{'std':c})



   


