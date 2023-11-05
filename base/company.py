from django.shortcuts import render, redirect, get_object_or_404
from .models import JobPost, CompanyDetails, UserData
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def add_job_post(request):
    if request.method == 'POST':
        obj=CompanyDetails.objects.get(user_id=request.user.id)
        company_id = obj.company_id
        job_title = request.POST['job_title']
        job_description = request.POST['job_description']
        posted_date = request.POST['posted_date']
        location = request.POST['location']
        vacancy = request.POST['vacancy']
        job_nature = request.POST['job_nature']
        salary = request.POST['salary']
        application_date = request.POST['application_date']
        skills_req = ','.join(request.POST.getlist('skills_req'))
        experience = request.POST['experience']
        education = request.POST['education']

        JobPost.objects.create(
            job_title=job_title,
            company_id=company_id,
            job_description=job_description,
            posted_date=posted_date,
            location=location,
            vacancy=vacancy,
            job_nature=job_nature,
            salary=salary,
            application_date=application_date,
            skills_req=skills_req,
            experience=experience,
            education=education
        )
        return redirect('job_list')
    return render(request, 'company/add_job_post.html')

@login_required
def update_job_post(request, job_post_id):
    job_post = get_object_or_404(JobPost, pk=job_post_id, company_id=request.user)
    if request.method == 'POST':
        job_post.job_title = request.POST['job_title']  # Update job_title
        job_post.job_description = request.POST['job_description']
        job_post.posted_date = request.POST['posted_date']
        job_post.location = request.POST['location']
        job_post.vacancy = request.POST['vacancy']
        job_post.job_nature = request.POST['job_nature']
        job_post.salary = request.POST['salary']
        job_post.application_date = request.POST['application_date']
        job_post.skills_req = ','.join(request.POST.getlist('skills_req'))
        job_post.experience = request.POST['experience']
        job_post.education = request.POST['education']
        job_post.save()
        return redirect('job_list')
    return render(request, 'company/update_job_post.html', {'job_post': job_post})

@login_required
def delete_job_post(request, job_post_id):
    job_post = get_object_or_404(JobPost, pk=job_post_id, company_id=request.user.id)
    job_post.delete()
    return redirect('job_list')

def job_list(request):
    job_posts = JobPost.objects.filter(company_id=request.user.id)
    return render(request, 'company/job_list.html', {'job_posts': job_posts})

def job_profile(request,id):
    job_posts = CompanyDetails.objects.get(user_id=User.objects.get(id=id))
    return render(request, 'company/job_list.html', {'company_detail': job_posts})


from django.shortcuts import render, redirect, get_object_or_404
from .models import CompanyDetails
from django.contrib.auth.decorators import login_required

@login_required
def add_company_details(request):
    if request.method == 'POST':
        user_id = request.user.id
        company_name = request.POST['company_name']
        company_ceo_name = request.POST['company_ceo_name']
        company_mail = request.POST['company_mail']
        company_site = request.POST['company_site']
        company_description = request.POST.get('company_description', None)
        company_logo = request.FILES.get('company_logo', None)
        company_linkedin = request.POST.get('company_linkedin', None)
        company_location = request.POST.get('company_location', None)
        starting_year = request.POST['starting_year']
        employees = request.POST.get('employees', None)

        CompanyDetails.objects.create(
            user_id=user_id,
            company_name=company_name,
            company_ceo_name=company_ceo_name,
            company_mail=company_mail,
            company_site=company_site,
            company_description=company_description,
            company_logo=company_logo,
            company_linkedin=company_linkedin,
            company_location=company_location,
            starting_year=starting_year,
            employees=employees
        )
        return redirect('company_details_list')
    return render(request, 'company/add_company_details.html')

@login_required
def update_company_details(request, company_id):
    company = get_object_or_404(CompanyDetails, company_id=company_id, user_id=request.user)
    if request.method == 'POST':
        company.company_name = request.POST['company_name']
        company.company_ceo_name = request.POST['company_ceo_name']
        company.company_mail = request.POST['company_mail']
        company.company_site = request.POST['company_site']
        company.company_description = request.POST.get('company_description', None)
        company.company_logo = request.FILES.get('company_logo', None)
        company.company_linkedin = request.POST.get('company_linkedin', None)
        company.company_location = request.POST.get('company_location', None)
        company.starting_year = request.POST['starting_year']
        company.employees = request.POST.get('employees', None)
        company.save()
        return redirect('company_details_list')
    return render(request, 'company/update_company_details.html', {'company': company})

@login_required
def delete_company_details(request, company_id):
    company = get_object_or_404(CompanyDetails, company_id=company_id, user_id=request.user)
    company.delete()
    return redirect('company_details_list')

def company_details_list(request):
    company_details = CompanyDetails.objects.filter(user_id=request.user)
    return render(request, 'company/company_details_list.html', {'company_details': company_details})

from django.shortcuts import render
from .models import JobPost

def filter_job_posts(request):
    # Get filter parameters from the request (you need to customize this based on your UI)
    selected_category = request.GET.get('category', None) #BE
    selected_job_type = request.GET.getlist('job_type', []) #FUll Time
    skills = request.GET.getlist('skill', [])
    selected_location = request.GET.get('location', None) # LOcation 1
    selected_experience = request.GET.get('experience', None) # 10
    min_salary = request.GET.get('from', None)
    max_salary = request.GET.get('to', None)

    print(selected_category,selected_job_type,selected_location,selected_experience,min_salary,max_salary)
    
    # Start with all job posts
    job_posts = JobPost.objects.all()

    # Apply filters based on the selected criteria
    if selected_category:
        job_posts = job_posts.filter(education=selected_category)
    if selected_job_type:
        job_posts = job_posts.filter(job_nature__in=selected_job_type)
    if selected_location:
        job_posts = job_posts.filter(location=selected_location)
    if selected_experience:
        job_posts = job_posts.filter(experience__in=selected_experience)
    if min_salary:
        job_posts = job_posts.filter(salary__gte=min_salary)
    if max_salary:
        job_posts = job_posts.filter(salary__lte=max_salary)
    if skills:
        datas = datas.filter(skills__in=skills)
    
    company_data = []
    for i in job_posts:
        print(i,i.company_id)
        try:
            obj = CompanyDetails.objects.get(company_id=i.company_id)
            print(obj.company_mail,obj.company_name)
            company_data.append(obj)
        except:
            pass
        
    
    print("Job Posts : ",job_posts)

    # Now, you have a queryset of filtered job posts
    return render(request, 'new_temp/job_listing.html', {'job_posts': zip(job_posts,company_data),'size':len(job_posts)})

import requests

def rank_github_profiles(profile_urls):
    # Function to calculate the profile score
    def calculate_profile_score(profile_url):
        # Extract the username from the GitHub profile URL
        username = profile_url.split("/")[-1]

        # Fetch user data from the GitHub API
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)

        if response.status_code != 200:
            return (profile_url, None)

        profile_data = response.json()

        public_repos = profile_data["public_repos"]
        followers = profile_data["followers"]
        stars = fetch_stars_count(profile_url)
        contributions = fetch_contributions(username)
        consistency = calculate_consistency(public_repos, contributions)

        # Define your scoring algorithm
        score = public_repos + followers + stars + contributions + consistency

        return (profile_url, score)

    # Function to fetch starred repositories count
    def fetch_stars_count(profile_url):
        url = f"{profile_url}?tab=stars"
        response = requests.get(url)

        if response.status_code != 200:
            return 0

        stars = response.text.count('aria-label="Star"')
        return stars

    # Function to fetch user contributions
    def fetch_contributions(username):
        # Fetch public events of the user
        url = f"https://api.github.com/users/{username}/events/public"
        response = requests.get(url)

        if response.status_code != 200:
            return 0

        events = response.json()
        contributions = sum(1 for event in events if event["type"] in ("PushEvent", "IssuesEvent", "PullRequestEvent"))

        return contributions

    # Function to calculate consistency score
    def calculate_consistency(public_repos, contributions):
        # Define your consistency scoring algorithm
        if public_repos == 0:
            return 0
        else:
            return contributions / public_repos

    # Fetch profile data, calculate scores, and rank profiles
    profile_scores = {}
    for profile_url in profile_urls:
        profile_score = calculate_profile_score(profile_url)
        if profile_score[1] is not None:
            profile_scores[profile_score[0]] = profile_score[1]

    # Rank profiles based on scores
    ranked_profiles = sorted(profile_scores.items(), key=lambda x: x[1], reverse=True)

    return ranked_profiles


def user_listing(request):
    datas = UserData.objects.all()
    if request.method == "GET":
        gender = request.GET.get('gender', None)
        location = request.GET.get('location', None)
        skills = request.GET.getlist('skill', [])
        dob_from = request.GET.get('from', None)
        dob_to = request.GET.get('to', None)
        
        # Filter the data based on the form inputs
        if gender:
            datas = datas.filter(gender=gender)
        if location:
            datas = datas.filter(location=location)
        if skills:
            datas = datas.filter(skills__in=skills)
        if dob_from:
            datas = datas.filter(dateofbirth__gte=dob_from)
        if dob_to:
            datas = datas.filter(dateofbirth__lte=dob_to)
        githubs = []
        list_datas = []
        for i in datas:
            githubs.append(i.githublink)
        rank_git = rank_github_profiles(githubs)
        print(rank_git)
        for i in datas:
            for j in rank_git:
                if j[0] == i.githublink:
                    list_datas.append(i)
        print(list_datas)
        if not request.user.is_authenticated:
            return render(request, "user/user_listing.html", {'msg': 'no_login'})
        else:
            return render(request, "user/user_listing.html", {'datas': list_datas})
    if not request.user.is_authenticated:
        return render(request, "user/user_listing.html", {'msg': 'no_login'})
    else:
        return render(request, "user/user_listing.html", {'datas': list_datas})
    
    