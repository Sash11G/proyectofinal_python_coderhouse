from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    # path("profile/", views.profile, "profile")
    path('unauthorized/', views.unauthorized_access_view, name='unauthorized_access'),
     #### LOGIN ####
    path("registro", views.registro_view, name="registro"),
    path("login", views.login_view, name="login"),
    path("logout", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    #### EDITAR USUARIO ####
    path("editar-perfil/<str:username>/", views.editar_perfil_view, name="editar-perfil"),
    path('profiles/<str:username>/', views.view_profile, name='view-profile'),
    # path('<int:user_id>/password/', views.change_password, name='change-password'),
]
