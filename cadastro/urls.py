from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='tabela/')),
    path('tabela/', views.tabela_ends, name = 'tabela-inicio'),
    path('cadastrar/', views.cadastrar_end, name = 'cadastrar-end'),
    path('cadastrar/submit', views.submit_cadastrar, name = 'submit-end'),
    
    path('<int:id>/', views.delete_addres, name = 'tabela-delete'),
    
    
    
   
    
    
]
