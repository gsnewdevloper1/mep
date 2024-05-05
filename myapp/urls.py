from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about',views.about, name='about'),
    path('login',views.login_page, name='login'),
    path('mep',views.mep, name='mep'),
    path('logout',views.logout_page, name='logout'),
    path('add',views.add, name='add'),
    path('<int:sno>',views.comment, name='comment'),
    path('delete/<int:sno>',views.delete_page, name='deletedata'),
]
