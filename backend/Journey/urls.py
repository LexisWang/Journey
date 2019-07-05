"""Journey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework_swagger.views import get_swagger_view
from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from apps.user.views import *
from apps.common.views import *
from apps.conf.views import *
from apps.db.views import *
from apps.query.views import *

router = routers.DefaultRouter()
router.register(r'user', UsersViewSet, base_name="user")
router.register(r'usergroup', UserGroupViewSet, base_name="usergroup")
router.register(r'permissionsgroup', PermissionsGroupViewSet, base_name="permissionsgroup")
router.register(r'mailconfig', MailConfigViewSet, base_name="mailconfig")
router.register(r'querylimit', QueryLimitViewSet, base_name="querylimit")
router.register(r'mysqlinst', MySQLInstViewSet, base_name="mysqlinst")
router.register(r'useraccessmysql', UserAccessMySQLViewSet, base_name="useraccessmysql")
router.register(r'dumpwhitelist', DumpWhiteListViewSet, base_name="dumpwhitelist")

schema_view = get_swagger_view(title="Journey API")

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'docs/', schema_view),
    url(r'^', include(router.urls)),
    url(r'api/', include(router.urls)),
    url(r'api/login',obtain_jwt_token),
    url(r'api/refresh_token',refresh_jwt_token),
    url(r'^api/logout', LogoutViewSet.as_view(({'get':'logout'}))),
    url(r'^api/ldapauth', LdapAuthViewSet.as_view()),
    url(r'^api/mailtest', MailTestViewSet.as_view()),
    url(r'^api/mysqlmeta', MySQLMetaViewSet.as_view()),
    url(r'^api/mysqluser', MySQLUserViewSet.as_view()),
    url(r'^api/mysqlstatus', MySQLStatusViewSet.as_view()),
    url(r'^api/useraccessdb', UserAccessDbViewSet.as_view()),
    url(r'^api/querysql', QuerySqlViewSet.as_view()),
]
