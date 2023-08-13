from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def homepage(request):
  
   if request.method =='POST':

        data = request.POST
        recipe_name =data.get('recipe_name')
        recipe_details=data.get('recipe_details')
        recipe_image=request.FILES.get('recipe_image')
    
        print(recipe_name)
        print(recipe_details)
        
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_details=recipe_details,
            recipe_image =recipe_image,
        )
        return redirect('/')
 
   searchitem =request.GET.get('searchrecipe')
   if searchitem:
       queryset=queryset.filter(recipe_name__icontains =searchitem)
 

   context={'recipes' :queryset}
  
   return render(request,'form.html',context)

@login_required(login_url='/login/')
def delete_recipe(request,id):
    queryset =Recipe.objects.get(id = id)
    print(id)
    queryset.delete()
    return redirect('/')

@login_required(login_url='/login/')
def update_recipe(request,id):
    queryset =Recipe.objects.get(id = id)
    print(id) 
    if request.method=='POST':
        data = request.POST
        recipe_name =data.get('recipe_name')
        recipe_details=data.get('recipe_details')        
        recipe_image=request.FILES.get('recipe_image')
        
        queryset.recipe_name=recipe_name
        queryset.recipe_details=recipe_details

        if recipe_image:
            queryset.recipe_image=recipe_image
        
            
        queryset.save()
        return redirect("/")
    context={'recipes' :queryset}
    
    return render(request,'update.html',context)


@login_required(login_url='/login/')
def logoutpage(request):
  logout(request)
  return redirect('/login/')



def loginpage(request):


 if request.method =='POST':
    data = request.POST
    username=data.get('username')
    password=data.get('password')   

    if not User.objects.filter(username=username).exists():
       messages.error(request, 'Invalid Username')
       return redirect('/login/')
    
    user=authenticate(username=username,password=password) 
    if user is None:
       messages.error(request, 'Invalid password')
       return redirect('/login/')
    else:
       login(request,user)
       return redirect('/')
 return render(request,'login.html')

def registerpage(request):

 if request.method =='POST':
    data = request.POST
    first_name=data.get('first_name')
    last_name=data.get('last_name')
    username=data.get('username')
    password=data.get('password')

    user =  User.objects.filter(username=username)
  
    if user.exists():
        messages.add_message(request, messages.INFO, "User already exist.")
        return redirect('/register/')


    user = User.objects.create(
                
        first_name=first_name,
        last_name=last_name,
        username=username,

    )
    user.set_password(password)
    user.save()
    messages.add_message(request, messages.INFO, "Registeration successful")

    return redirect('/register/')
    

 return render(request,'register.html')

