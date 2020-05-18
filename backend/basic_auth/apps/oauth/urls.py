from django.urls import path

from oauth import views

urlpatterns = [
    path(
        'token',
        views.TokenView.as_view()
    ),
    path(
        'logout',
        views.LogoutView.as_view()
    )
]
