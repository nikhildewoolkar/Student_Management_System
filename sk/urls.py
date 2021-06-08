from . import views
from django.urls import path

urlpatterns=[
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("signup/",views.signup,name="signup"),
    path("library/",views.library,name="library"),
    path("profile/",views.profile,name="profile"),
    path("portal/",views.portal,name="portal"),
    path("change_password/",views.change_password,name="change_password"),
    path("editprofile/",views.editprofile,name="editprofile"),
    path("ProfilePic/",views.ProfilePic,name="ProfilePic"),
    path("privacy/",views.privacy,name="privacy"),
    path("search/",views.search,name="search"),
    path("file_upload/",views.file_upload,name="file_upload"),
    # path("search/",views.search,name="search"),
]