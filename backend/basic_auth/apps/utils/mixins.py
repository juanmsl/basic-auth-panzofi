from django.contrib.auth.models import Group
from django.http import Http404
from rest_framework import status, permissions, exceptions
from rest_framework.response import Response


class RetrieveModelMixin:

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        output_serializer = self.OutputSerializer(
            instance
        )

        return Response(
            data=output_serializer.data
        )


class ListModelMixin:

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        output_serializer = self.OutputSerializer(
            queryset, many=True
        )

        return Response(
            data=output_serializer.data
        )


class CreateModelMixin:
    def create(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(
            data=request.data
        )
        input_serializer.is_valid(raise_exception=True)
        instance = input_serializer.save()

        output_serializer = self.OutputSerializer(
            instance
        )

        return Response(
            data=output_serializer.data,
            status=status.HTTP_201_CREATED
        )


class UpdateModelMixin:

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        input_serializer = self.InputSerializer(
            instance,
            data=request.data,
            partial=partial
        )
        input_serializer.is_valid(raise_exception=True)

        instance = input_serializer.save()

        output_serializer = self.OutputSerializer(
            instance
        )

        return Response(
            data=output_serializer.data
        )

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DestroyModelMixin:

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        output_serializer = self.OutputSerializer(
            instance
        )

        instance.delete()

        return Response(
            data=output_serializer.data,
            status=status.HTTP_200_OK
        )
