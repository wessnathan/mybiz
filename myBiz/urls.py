
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from myBizUsers import views as new_user_views
from myBizDetails.views import UserListView
from myBizUsers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lipanampesa.urls')),
    path('', include('myBizApi.urls')),
    path('', include('myBizDetails.urls')),
    path('/', include('myBizUsers.urls')),
    url(r'^(?P<username>\w+)/$', UserListView.as_view(), name='userdetails'),
    path('activate/user/<int:user_id>', views.user_activate, name='activate_user'),
    path('deactivate/user/<int:user_id>', views.user_deactivate, name='deactivate_user'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



