from django.contrib import admin
from django.urls import path, include  # include رو فراموش نکن

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # ← این خط خیلی مهمه
]