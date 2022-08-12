from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    
    
    
    path('register/' ,views.register ,name='register') , 
    path('password_change/' , auth_views.PasswordChangeView.as_view() , name='password_change') , 
    path('password_change/done/' , auth_views.PasswordChangeDoneView.as_view() , name='password_change_done') , 
    path('password_reset/' , auth_views.PasswordResetView.as_view() , name='password_reset') , 
    path('password_reset/done/' , auth_views.PasswordResetDoneView.as_view() , name='password_reset_done') , 


#accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
#accounts/reset/done/ [name='password_reset_complete']

 #path('accounts_reset/<uidb64>/<token>/' ,auth_views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
 #path('accounts_reset/done/' ,auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

