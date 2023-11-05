from django.shortcuts import render, redirect, get_object_or_404
from .models import UserData
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date

@login_required
def add_user_data(request):
    if request.method == 'POST':
        user = request.user
        user_name = request.POST['user_name']
        mailid = request.POST['mailid']
        linkedin = request.POST['linkedin']
        githublink = request.POST['githublink']
        skills = ','.join(request.POST.getlist('skills'))
        location = request.POST['location']
        profile_pic = request.FILES.get('profile_pic', None)
        resume = request.FILES.get('resume', None)
        dateofbirth = request.POST['dateofbirth']
        about = request.POST.get('about', None)
        phone_no = request.POST['phone_no']
        gender = request.POST['gender']

        UserData.objects.create(
            user=user,
            user_name=user_name,
            mailid=mailid,
            linkedin=linkedin,
            githublink=githublink,
            skills=skills,
            location=location,
            profile_pic=profile_pic,
            resume=resume,
            dateofbirth=dateofbirth,
            about=about,
            phone_no=phone_no,
            gender=gender
        )
        return redirect('user_data_list')
    return render(request, 'user/add_user_data.html')

@login_required
def update_user_data(request, user_data_id):
    user_data = UserData.objects.get(user=User.objects.get(id=user_data_id))
    if request.method == 'POST':
        user_data.user_name = request.POST['user_name']
        user_data.mailid = request.POST['mailid']
        user_data.linkedin = request.POST['linkedin']
        user_data.githublink = request.POST['githublink']
        user_data.skills = ','.join(request.POST.getlist('skills'))
        user_data.location = request.POST['location']
        user_data.profile_pic = request.FILES.get('profile_pic', user_data.profile_pic)
        user_data.resume = request.FILES.get('resume', user_data.resume)
        user_data.dateofbirth = request.POST['dateofbirth']
        user_data.about = request.POST['about']
        user_data.phone_no = request.POST['phone_no']
        user_data.gender = request.POST['gender']
        user_data.save()
        return redirect('user_data_list')
    return render(request, 'user/update_user_data.html', {'user_data': user_data})

@login_required
def delete_user_data(request, user_data_id):
    user_data = get_object_or_404(UserData, pk=user_data_id, user=request.user)
    user_data.delete()
    return redirect('user_data_list')

def user_data_list(request):
    user_data = UserData.objects.filter(user=request.user)
    return render(request, 'user/user_data_list.html', {'user_data': user_data})

import requests
import re
import markdown
def profile(request,usr_id):
    def get_github_username_from_link(github_link):
        # Regular expression pattern to match a GitHub profile link
        pattern = r"https://github.com/([A-Za-z0-9-]+)"

        # Use re.search to find the username in the link
        match = re.search(pattern, github_link)

        if match:
            username = match.group(1)
            return username
        else:
            return None
    def get_github_readme(username):
        try:
            # Define the URL for the README of the repository
            readme_url = f"https://raw.githubusercontent.com/{username}/{username}/main/README.md"

            # Send a GET request to the README URL
            response = requests.get(readme_url)
            response.raise_for_status()  # Raise an exception if there's an HTTP error

            # Get the README content
            readme_content = response.text
            return readme_content

        except requests.exceptions.RequestException as e:
            return f"Error: {e}"
    obj = UserData.objects.get(user=User.objects.get(id=usr_id))
    link = obj.githublink
    user_name = get_github_username_from_link(link)
    if link != "githublink":
        readme = markdown.markdown(get_github_readme(user_name))
    return render(request, 'user/user_profile.html',{'obj':obj,'now_usr':request.user.id,'readme':readme})
