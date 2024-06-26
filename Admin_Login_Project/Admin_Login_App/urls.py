from django.urls import path
from .views import (
    admin_login_view, dashboard_view, logout_view, user_logout,
    AdminLoginAPI, get_admin_usernames,
    CourseListCreateView, CourseDetailView,
    course_view, course_page_view, navbar_save_view,
    update_course, delete_course, pdf
)

urlpatterns = [
    path('admin_login/', admin_login_view, name='admin_login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('user_logout/', user_logout, name='user_logout'),
    
    path('api/admin_login/', AdminLoginAPI.as_view(), name='admin_login_api'),
    path('api/get_admin_usernames/', get_admin_usernames.as_view(), name='get_admin_usernames'),
    
    path('api/courses/', CourseListCreateView.as_view(), name='course_list_create'),
    path('api/courses/<int:id>/', CourseDetailView.as_view(), name='course_detail'),
    
    path('courses/', course_view, name='courses'),
    path('course_page/', course_page_view, name='course_page'),
    path('navbar_save_course/', navbar_save_view, name='navbar_save_course'),
    path('update_course/<int:id>/', update_course, name='update_course'),
    path('delete_course/<int:id>/', delete_course, name='delete_course'),
    
    path('pdf/', pdf, name='pdf'),
]

