from rest_framework.generics import GenericAPIView

from utils import mixins


class RetrieveModelView(
    mixins.RetrieveModelMixin,
    GenericAPIView
):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ListModelView(
    mixins.ListModelMixin,
    GenericAPIView
):
    def get(self, request):
        return self.list(request)


class CreateModelView(
    mixins.CreateModelMixin,
    GenericAPIView
):
    def post(self, request):
        return self.create(request)


class UpdateModelView(
    mixins.UpdateModelMixin,
    GenericAPIView
):
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class DestroyModelView(
    mixins.DestroyModelMixin,
    GenericAPIView
):
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListCreateModelView(
    ListModelView,
    CreateModelView
):
    pass


class RetrieveUpdateDestroyModelView(
    RetrieveModelView,
    UpdateModelView,
    DestroyModelView
):
    pass
