# from django.contrib import admin
from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.conf.urls.static import static
from ZKAI import settings
from base.views import *
from base.common import *
from base.company import *
from base.compiler import *
from base.ind_user import *
from base.chabot import chat_home, about, chatbot_res, login_form,signup,logout1,upload_image,text_bard, add_text_entry


urlpatterns = [
    
    path('add_text', add_text_entry, name='add_text_entry'),
    path('job_details/<int:post_id>', job_details, name='job_details'),
    path('job_listing', job_listing, name='job_listing'),
    path('user_listing', user_listing, name='user_listing'),
    path('filter_job_posts', filter_job_posts, name='filter_job_posts'),
    path('contact', contact, name='contact'),
    path('chat_home', chat_home, name='chat_home'),
    
    path('chatbot_res',chatbot_res,name="chatbot_res"),
    path('upload_image', upload_image, name='upload_image'),
    path('text_bard', text_bard, name='text_bard'),
    
    
    path('google_api', chat_home, name='chat_home'),
    path('video_feed', video_feed, name='video_feed'),
    # path('', home, name='home'),
    path('home', home, name='home'),
    path('', home, name='home'),
    path('test_home', Test_home, name='test_home'),
    # path('show_images', show_images, name='show_images'),
    path('report/<int:total_question>/<int:total_mark>', report, name='report'),
    path('compiler/', compiler_view, name='compiler'),
     
     
    path('signup', signup, name='signup'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    
    path('add_job_post', add_job_post, name='add_job_post'),
    path('update_job_post/<int:job_post_id>', update_job_post, name='update_job_post'),
    path('delete_job_post/<int:job_post_id>', delete_job_post, name='delete_job_post'),
    path('job_list', job_list, name='job_list'),
    
    path('add_company_details', add_company_details, name='add_company_details'),
    path('update_company_details/<int:company_id>', update_company_details, name='update_company_details'),
    path('delete_company_details/<int:company_id>', delete_company_details, name='delete_company_details'),
    path('company_details_list', company_details_list, name='company_details_list'),
    path('job_profile/<int:id>', job_profile, name='job_profile'),
    
     path('add_usr', add_user_data, name='add_user_data'),
     path('profile/<int:usr_id>', profile, name='profile'),
    path('update_usr/<int:user_data_id>', update_user_data, name='update_user_data'),
    path('delete_usr/<int:user_data_id>', delete_user_data, name='delete_user_data'),
    path('list_usr', user_data_list, name='user_data_list'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
