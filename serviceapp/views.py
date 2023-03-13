from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User_Profile, User_Post, Like_Post, Follow, Comment
from itertools import chain
from django.db.models import Q


# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This email is already taken')
                return redirect('register.html')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #Login and redirect user
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                #Create user profile
                user_model = User.objects.get(username=username)
                new_profile = User_Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('/')
        else:
            messages.info(request, 'Your passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    follower = request.user.username
    user_object = User.objects.get(username=request.user.username)
    user_profile = User_Profile.objects.get(user=user_object)
    profiles =  User_Profile.objects.all()  
    posts_list = User_Post.objects.all()
    comments = Comment.objects.all()
    followers = Follow.objects.filter(follower=follower).all()

    following_list = []
    feed = []

    user_following = Follow.objects.filter(follower=request.user.username)

    for users in user_following:
        following_list.append(users.user)
    for usernames in following_list:
        feed_lists = User_Post.objects.filter(user=usernames)
        feed.append(feed_lists)
    
    feed_list = list(chain(*feed))
    people_following = len(following_list)



    context = {
        "user_object":user_object,
        "user_profile":user_profile,
        "posts_list":posts_list,
        "feed_list":feed_list,
        "people_following":people_following,
        "comments":comments,
        "profiles":profiles,
        "followers":followers
    }
    return render( request, 'index.html', context)

@login_required(login_url='login')
def follow(request):
    if request.method == "POST":
        follower = request.POST['follower']
        user = request.POST['user']
        user_id = request.GET.get('post_id')
        print(user_id)

        if Follow.objects.filter(follower=follower, user=user).first():
            delete_follower = Follow.objects.get(follower=follower, user=user)
            delete_follower.delete()
            print(follower)
            return redirect('/profile/'+user)
        else:
            new_follower = Follow.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    else:
        return redirect('/')

@login_required(login_url='login')
def like(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = User_Post.objects.get(id=post_id)
    like_filter = Like_Post.objects.filter(post_id=post_id, username=username).first()

    if like_filter == None:
        new_like = Like_Post.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.likes = post.likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.likes = post.likes-1
        post.save()
        return redirect('/')


def upload(request):
    if request.method == "POST":
        user_object = User.objects.get(username=request.user.username)
        user_profile =  User_Profile.objects.get(user=user_object)
        

        user = request.user.username
        image = request.FILES.get('image')
        profileImg = user_profile.profilePic
        service = request.POST['service']        
        phone = request.POST['phone']
        location = request.POST['location']
        cost = request.POST['cost']
        description = request.POST['description']
        print(phone)
        new_user_post = User_Post.objects.create(user=user, phone=phone, image=image, location=location, cost=cost, profileImg=profileImg, description=description, service=service)
        new_user_post.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='login')
def profile(request, pk):
    user_logged = User.objects.get(username=request.user.username)
    user_profile_logged = User_Profile.objects.get(user=user_logged)
   
    follower = request.user.username
    user = pk

    if Follow.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'
        

    #post_object = User_Post.objects.get(user=pk)
    user_object = User.objects.get(username=pk)
    user_profile = User_Profile.objects.get(user=user_object)
    user_posts = User_Post.objects.filter(user=user_object)

    user_followers = len(Follow.objects.filter(user=pk))
    user_following = len(Follow.objects.filter(follower=pk))
   
    context = {
        "user_profile":user_profile,
        "user_posts":user_posts,
        "user_profile_logged":user_profile_logged,
        "button_text":button_text,
        "user_followers":user_followers,
        "user_following":user_following
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def service(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = User_Profile.objects.get(user=user_object)
    context = {
        "user_profile":user_profile
    }
    return render(request, 'service.html', context) 

@login_required(login_url='login')
def account(request, pk):
    all_users = User_Profile.objects.all()
    user_object = User.objects.get(username=pk)
    user_profile = User_Profile.objects.get(user=user_object)
    user_posts = User_Post.objects.filter(user=pk)
    number_of_posts = len(user_posts)
    print(user_object.username)
    context = {
        "all_users":all_users,
        "user_object":user_object,
        "user_profile":user_profile,
        "user_posts":user_posts,
        "number_of_posts":number_of_posts
    }
    return render(request, 'account.html', context)   

@login_required(login_url='login')
def update(request):
    user_profile = User_Profile.objects.get(user=request.user)

    if request.method == "POST":
        if request.FILES.get('image') == None:
            image = user_profile.profilePic
            location = request.POST['location']
            service = request.POST['service']
            biography = request.POST['biography']
            phone = request.POST['phone']

            user_profile.profilePic = image
            user_profile.location = location
            user_profile.service = service
            user_profile.biography = biography
            user_profile.phone = phone

            user_profile.save()
        if request.FILES.get('image') != None:
            image = request.FILES.get('image')
            location = request.POST['location']
            service = request.POST['service']
            biography = request.POST['biography']

            user_profile.profilePic = image
            user_profile.location = location
            user_profile.service = service
            user_profile.biography = biography
            user_profile.phone = phone

            user_profile.save()

        return redirect('update')

    user_object = User.objects.get(username=request.user.username)
    user_data = User_Profile.objects.get(user=user_object)
   
    context = {
        "user_profile":user_profile,
        "user_data":user_data
    }
    return render(request, 'update.html', context)

def comment(request):
    if request.method == "POST":
        comment = request.POST['comment']
        commenter = request.user.username
        post_id = request.POST['post_owner']

        comment_object = Comment.objects.create(comment=comment, commenter=commenter, post_id=post_id)
        comment_object.save()
        return redirect('/')
    else:
        return redirect('/')

def delete_post(request):
    post_id = request.GET.get('post_id')    
    post = User_Post.objects.get(id=post_id)
    post.delete()
    return redirect('/')

def delete_comment(request):
    comment_id = request.GET.get('comment_id')
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('/')

def single_post(request, pk):
    #post_id = request.GET.get('post_id')
    post = User_Post.objects.get(id=pk)
    user_logged = User.objects.get(username=request.user.username)
    user_profile_logged = User_Profile.objects.get(user=user_logged)

    context={
        "post":post,
        "user_profile_logged":user_profile_logged
    }
    return render(request, 'post.html', context)

#Search results
def search(request):

    user_logged = User.objects.get(username=request.user.username)
    user_profile_logged = User_Profile.objects.get(user=user_logged)

    if request.method == 'GET':
        service_name = request.GET.get('service')
        try:
            results = User_Post.objects.filter(service__icontains = service_name)
            len_of_results = len(results)
            context = {
                "results":results,
                "user_profile_logged":user_profile_logged,
                "len_of_results":len_of_results
            }
        except User_Post.DoesNotExist:
            status = None
        
        return render(request, "search.html", context)
    
    else:
        return render(request, "search.html")

# def search(request):
#     if request.method == "POST":
#         service = request.POST["service"]
#         posts_results = []

#         posts_objects = User_Post.objects.filter(service__icontains=service)

#         for post in posts_objects:
#             posts_results.append(post)
        
#         results = list(chain(* posts_results))

#         print(results.username)

#         return render(request, 'index.html')
#     else:
#         return redirect('/')
