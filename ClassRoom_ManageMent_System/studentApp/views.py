from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout 
from django.contrib import messages 
from adminApp.models import Notice,Class,Course
from .models import TeachingClass,JoinedClass,UserProfile
from django.utils.timezone import localtime
from .forms import UserProfileForm

# Create your views here.
def homepage(request):
    notices=Notice.objects.all().order_by('-notice_timestamp')
    length=len(notices)
    course=Course.objects.all()
    classes=Class.objects.all()
    for notice in notices:
        notice.notice_timestamp=localtime(notice.notice_timestamp)
    #length_of_classes=len(classes)
    semesters=set()
    for cls in classes:
        semesters.add(cls.class_semester)

    semster_filtered_classes=[]
    for semester in semesters:
        semster_filtered_classes.append(Class.objects.filter(class_semester=semester))
    #semster_filtered_classes.sort(key=class_semester)
    length_of_classes=len(semster_filtered_classes)
    params={'classes':semster_filtered_classes ,'length_of_classes':length_of_classes,'notices':notices,'length':length}
    return render(request,'studentApp/homepage.html',params)

def handleTeaching(request):
    teaching_classes=TeachingClass.objects.filter(class_author=request.user)
    length=len(teaching_classes)
    teaching_classes={'teaching_classes':teaching_classes,'len':length}
    return render(request,'studentApp/createdClass.html',teaching_classes)
    

#handle classes
def handleClasses(request):
    joined_classes=JoinedClass.objects.filter(student=request.user)
    length=len(joined_classes)
    joined_classes={'joined_classes':joined_classes,'len':length}
    return render(request,'studentApp/myClasses.html',joined_classes)
    

#handle signup
def handleSignUp(request):
    if request.method=='POST':
        # Get the post parameters
        username=request.POST['user-name']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        reg="registration"
        #user=User()

        # check for errorneous input

        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('homepage')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('homepage')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('homepage')
            # Create the user 
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save() 
        userprofile=UserProfile(user=myuser,bio="",reg="",email=myuser.email,dept="",section="",phone="")
        userprofile.save()
        messages.success(request,"signUp successful")
        return redirect('homepage')
    else:
        return HttpResponse("404 - Not found")
# handle login login 
def handleLogIn(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpass']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect('homepage')
        else:
            messages.error(request,'User not found')
            return redirect('homepage')
    return HttpResponse("404 - Not found!!!")

    
#handle logout
def handleLogOut(request):
    logout(request)
    messages.success(request,'successfully loged out')
    return redirect('homepage')
        
def handleCreateClass(request):
    if request.method=='POST':
        class_name=request.POST['classname']
        class_subject=request.POST['class-subject']
        class_section=request.POST['section']
        class_author=request.user
        created_class=TeachingClass(class_name=class_name,class_subject=class_subject,
        class_section=class_section,class_author=class_author)
        created_class.save()
        messages.success(request, "Your class has been created successfully")
        return redirect('homepage')
def handleJoinClass(request):
    if request.method=='POST':
        user=request.user
        class_code=request.POST['classcode']
        print(class_code)
        joined1=TeachingClass.objects.get(class_code=class_code)
        print(joined1)
        joinedclass=JoinedClass(joined_class=joined1,student=user,class_code=class_code)
        joinedclass.save()
        messages.success(request, "You have joined successfully....")
        return redirect('homepage')

#changing profile pic       
def changeProfilePic(request):
    if request.method=='POST':
        profile_pic=request.FILES['profilepic']
        user=request.user
        userProfile=UserProfile.objects.get(user=user)
        userProfile.profile_pic=profile_pic
        userProfile.save()
        messages.success(request, "Your Profile picture have been changed....")
        return redirect('profile')

#handle profile
def handleUpdateProfile(request):
    if request.method=='POST':
        user=request.user
        userProfile=UserProfile.objects.get(user=user)


        userProfile.dept=dept=request.POST['department']
        userProfile.reg=request.POST['reg']
        userProfile.session=request.POST['session']
        userProfile.section=request.POST['section']
        userProfile.bio=request.POST['bio']
        userProfile.phone =request.POST['mobile']
        userProfile.email=request.POST['email']
        user.email=userProfile.email

        #print(email)
        #print(profile_pic)

        userProfile.save()
        #profile.save()
        messages.success(request, "Your Profile Updated Successfully...")
        return redirect('profile')

def insertTeachingClass(request,slug):
    return render(request,'studentApp/teachingClass.html')

def profile(request):
    userProfile=UserProfile.objects.get(user=request.user)
    print(userProfile)
    print(userProfile.bio)
    context={'userProfile':userProfile}
    return render(request,'studentApp/profile.html',context)