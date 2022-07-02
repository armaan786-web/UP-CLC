from django.urls import path
from .import views,HOD_VIEWS,MEMBERS_VIEWS,EMPLOYEE_VIEWS,INSTRUCTOR_VIEWS,TRAINING_VIEWS



urlpatterns = [
    path('',views.home,name="home"),
    path('joblisting/',views.joblisting,name="joblisting"),
    path('jobdetails/<int:pk>',views.jobdetails,name="jobdetails"),
    path('course/',views.course,name="course"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('apply/',views.apply,name="apply"),
    
    


    
    
   
    
    
    




    path('HOD/Dashboard',HOD_VIEWS.HOD,name="hod_dashboard"),
    path('HOD/add_role',HOD_VIEWS.ADD_ROLE,name="add_role"),
    path('HOD/manage_role',HOD_VIEWS.MANAGE_ROLE,name="manage_role"),
    path('HOD/edit_role/<str:role_id>', HOD_VIEWS.edit_role,name="edit_role"),
    path('HOD/edit_role', HOD_VIEWS.edit_role_save,name="edit_rolee_save"),
    path('HOD/role/Delete/<str:role_id>', HOD_VIEWS.DELETE_ROLE,name="delete_role"),
    path('HOD/TRAINING',HOD_VIEWS.TRAINING_CENTER,name="training_center"),
    path('HOD/manage_center',HOD_VIEWS.MANAGE_CENTER,name="manage_center"),
    path('HOD/edit_center/<str:center_id>', HOD_VIEWS.edit_center,name="edit_center"),
    path('HOD/edit_center_save', HOD_VIEWS.edit_center_save,name="edit_center_save"),
    path('HOD/center/Delete/<str:center_id>', HOD_VIEWS.DELETE_CENTER,name="delete_center"),
    path('HOD/Location',HOD_VIEWS.LOCATION,name="location"),
    path('HOD/doLocation',HOD_VIEWS.doLocation,name="doLocation"),
    # path('HOD/manage_location',HOD_VIEWS.manage_location,name="manage_location"),
    


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
    
    path('register/',MEMBERS_VIEWS.register,name="register"),
    path('douserregister/',MEMBERS_VIEWS.douserregister,name="douserregister"),
    path('success/', MEMBERS_VIEWS.Success , name='success'),
    path('MEMBERS/member_login', MEMBERS_VIEWS.member_login,name="member_login"),
    path('dologin/', MEMBERS_VIEWS.doLogin, name="dologin"),
    path('logout_user', MEMBERS_VIEWS.logout_user,name="logout"),
   
    path('MEMBERS/Dashboard', MEMBERS_VIEWS.dashboard,name="member_dashboard"),
    path('MEMBERS/payment_information', MEMBERS_VIEWS.payment_information,name="payment_information"),



    ########################## EMPLOYER URL ############################
    path('EMPLOYERS/Dashboard', EMPLOYEE_VIEWS.dashboard,name="dashboard"),
    path('EMPLOYERS/ADDJOBS', EMPLOYEE_VIEWS.employer_addjobs,name="employer_addjobs"),
    path('EMPLOYERS/REGISTER', EMPLOYEE_VIEWS.employer_register,name="employer_register"),
    path('EMPLOYERS/doregister', EMPLOYEE_VIEWS.employer_doregister,name="employer_doregister"),
    path('EMPLOYERS/login', EMPLOYEE_VIEWS.employer_login,name="employer_login"),
    path('EMPLOYERS/dologin', EMPLOYEE_VIEWS.employer_dologin,name="employer_dologin"),


    ########################## INSTRUCTOR URL ############################

    
    path('INSTRUCTOR/register', INSTRUCTOR_VIEWS.INSTRUCTOR_Register,name="INSTRUCTOR_Register"),
    path('INSTRUCTOR/doregister', INSTRUCTOR_VIEWS.INSTRUCTOR_doregister,name="INSTRUCTOR_doregister"),
    path('INSTRUCTOR/login', INSTRUCTOR_VIEWS.instructor_login,name="instructor_login"),
    path('INSTRUCTOR/dologin', INSTRUCTOR_VIEWS.instructor_dologin,name="instructor_dologin"),
    path('INSTRUCTOR/Dashboard', INSTRUCTOR_VIEWS.dashboard,name="instructor_dashboard"),
    path('INSTRUCTOR/add_course', INSTRUCTOR_VIEWS.add_course,name="add_course"),



    ################################## Training URL #####################   

    path('TRAINING/register', TRAINING_VIEWS.TRAINING_Register,name="TRAINING_Register"),
    path('TRAINING/login', TRAINING_VIEWS.TRAINING_login,name="TRAINING_login"),
    path('TRAINING/process', TRAINING_VIEWS.TRAINING_process,name="TRAINING_process"),


]
