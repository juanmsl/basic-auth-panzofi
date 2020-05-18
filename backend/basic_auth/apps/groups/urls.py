from django.urls import path

from groups import views

urlpatterns = [
    path(
        'groups',
        views.GroupListView.as_view()
    ),
    path(
        'group/<int:group_id>/user/<int:user_id>',
        views.GroupUserView.as_view()
    )
]
