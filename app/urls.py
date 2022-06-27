from django.urls import path
from .import views,HOD_VIEWS,MEMBERS_VIEWS,EMPLOYEE_VIEWS



urlpatterns = [
    path('',views.home,name="home"),
    path('joblisting/',views.joblisting,name="joblisting"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('register/',views.regi,name="register"),
    

    path('success/', views.Success , name='success'),
    path('dologin/', views.doLogin, name="dologin"),
    
    
    path('douserregister/',views.douserregister,name="douserregister"),




    path('HOD/Dashboard',HOD_VIEWS.HOD,name="hod_dashboard"),
    path('HOD/add_role',HOD_VIEWS.ADD_ROLE,name="add_role"),
    path('HOD/manage_role',HOD_VIEWS.MANAGE_ROLE,name="manage_role"),
    path('HOD/edit_role/<str:role_id>', HOD_VIEWS.edit_role,name="edit_role"),
    path('HOD/edit_role', HOD_VIEWS.edit_role_save,name="edit_rolee_save"),
    path('HOD/role/Delete/<str:role_id>', HOD_VIEWS.DELETE_ROLE,name="delete_role"),
    


    path('HOD/add_employee',HOD_VIEWS.ADD_EMPLOYEE,name="add_employee"),
    path('do_employee_signup',HOD_VIEWS.do_employee_signup,name="do_employee_signup"),
    path('manage_employee',HOD_VIEWS.manage_employee,name="manage_employee"),
    path('HOD/edit_employee/<str:employee_id>', HOD_VIEWS.edit_employee,name="edit_employee"),
    path('HOD/edit_employee', HOD_VIEWS.edit_employee_save,name="edit_employee_save"),
    path('HOD/employee/Delete/<str:employee_id>', HOD_VIEWS.DELETE_EMPLOYEE,name="delete_employee"),


    path('HOD/add_instructor',HOD_VIEWS.ADD_INSTRUCTOR,name="add_instructor"),
    path('do_instructor_signup',HOD_VIEWS.do_instructor_signup,name="do_instructor_signup"),
    path('manage_instructor',HOD_VIEWS.manage_instructor,name="manage_instructor"),
    path('HOD/edit_instructor/<str:instructor_id>', HOD_VIEWS.edit_instructor,name="edit_instructor"),
    path('HOD/edit_instructor', HOD_VIEWS.edit_instructor_save,name="edit_instructor_save"),
    # path('HOD/employee/Delete/<str:employee_id>', HOD_VIEWS.DELETE_EMPLOYEE,name="delete_emplo

    path('HOD/manage_members',HOD_VIEWS.manage_members,name="manage_members"),



    ############################# MEMBER URL ###########################################
    path('MEMBERS/Dashboard', MEMBERS_VIEWS.dashboard,name="member_dashboard"),
    path('MEMBERS/payment_information', MEMBERS_VIEWS.payment_information,name="payment_information"),



    ########################## EMPLOYER URL ############################
    path('EMPLOYERS/Dashboard', EMPLOYEE_VIEWS.dashboard,name="dashboard"),
    path('EMPLOYERS/REGISTER', EMPLOYEE_VIEWS.employer_register,name="employer_register"),
    path('EMPLOYERS/doregister', EMPLOYEE_VIEWS.employer_doregister,name="employer_doregister"),
    path('EMPLOYERS/login', EMPLOYEE_VIEWS.employer_login,name="employer_login"),
    path('EMPLOYERS/dologin', EMPLOYEE_VIEWS.employer_dologin,name="employer_dologin"),

]
