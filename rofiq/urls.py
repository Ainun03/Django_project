from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    # path('hello/<name>', views.home_page, name='beranda'),
    path('products/', views.products, name='products'),
    path('custumer/<str:pk>', views.custumer, name='custumer'),
    path('update_custumer/<str:pk>', views.updateCustumer, name='update_custumer'),
    path('delete_custumer/<str:pk>', views.deleteCustumer, name='delete_custumer'),
    path('create_order/', views.createOrder, name='create_order'),
    path('create_custumer/', views.createCustumer, name='create_custumer'),
    path('update_order/<str:pk>', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>', views.deleteOrder, name='delete_order'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),
    path('user/', views.userPage, name='user-page'),
    path('account/', views.accountSetting, name='account-page'),

# reset Pass
    # path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complate/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='password_change.html'),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),

]

urlpatterns += staticfiles_urlpatterns()