"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexPage.as_view(), name='index'),

    path('register/', views.UserFormView.as_view(), name='register'),

    # /music/<albumID>/favourite
    path('<pk>/', views.DetailPage.as_view(), name='detail'),

    # /music/album/add
    path('album/add', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/<albumID>
    path('album/<pk>', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/<albumID>/delete
    path('album/<pk>/delete', views.AlbumDelete.as_view(), name='album-delete'),

    # # /music/<albumID>/favourite
    # path('<int:albumID>/favourite', views.favourite, name='favourite'),
]
