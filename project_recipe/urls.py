from django.contrib import admin
from django.urls import path
from recipe import views  # Імпортуємо наші view-функції

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),  # головна сторінка
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),  # сторінка категорії
]