from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# 1. El Router para el ViewSet
# Esto crea automáticamente las rutas para 'Post':
# /api/posts/ (para GET - listar todo, y POST - crear nuevo)
# /api/posts/<pk>/ (para GET - ver uno, PUT - actualizar, DELETE - borrar)
router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

# 2. Las URL para tus vistas personalizadas (login, etc.)
urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('verify/', views.verify_token, name='verify_token'),
    
    # 3. Incluye las rutas del router que creamos arriba
    path('', include(router.urls)),
]