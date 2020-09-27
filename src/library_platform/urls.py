"""library_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


# MY VIEWS

from users.views import(dash_view, home_screen_view, registration_view, logout_view, login_view, all_students_view, profile_view, profileedit_view)
from transactions.views import(all_txn_view, add_txn_view)
from items.views import(all_item_view, add_item_view,item_detail_view)

urlpatterns = [
    path('admin/', admin.site.urls),


    # users 
    path('dash/', dash_view, name="dash"),
    path('all_students/', all_students_view, name="students"),
    path('register/', registration_view, name="register"),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login"),
    path('profile/', profile_view, name='profile'),
    path('profileedit/', profileedit_view, name='profileedit'),

    # transactions
    path('txn/', all_txn_view, name="txn"),
    path('add_txn/', add_txn_view, name="add_txn"),


    # Items
    path('', all_item_view, name="home"),
    path('items/', all_item_view, name="all_items"),
    path('add_item/', add_item_view, name="add_item"),
    path('detail/<int:book_id>/', item_detail_view, name="item_detail")


]


if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)