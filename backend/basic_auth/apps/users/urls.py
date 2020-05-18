from django.urls import path

from users import views


urlpatterns = [
    path(
        'users',
        views.UserListView.as_view()
    ),
    path(
        'user/<int:id>',
        views.UserDetailView.as_view()
    ),
    path(
        'user/count/<str:label>',
        views.CounterView.as_view()
    ),
    path(
        'user/basicdata',
        views.BasicDataView.as_view()
    )
]
