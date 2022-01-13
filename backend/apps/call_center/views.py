import logging

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Customer
from .serializers import CustomerSerializer


logger = logging.getLogger(__name__)


class CustomerViewSet(
        CreateModelMixin,
        RetrieveModelMixin,
        GenericViewSet
):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        logger.info(
            "User id %s requests to view customer id %s.",
            request.user.id,
            instance.id,
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        logger.info(
            "User id %s called create with %s.",
            request.user.id,
            request.data,
        )
        if request.data["date_birth"] == "":
            request.data["date_birth"] = None
        zip_code = request.data["zip_code"]
        zip_code = zip_code.upper()
        if len(zip_code) == 6:
            zip_code = zip_code[:4] + " " + zip_code[4:]
        request.data["zip_code"] = zip_code

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        logger.info(
            "User id %s created %s.",
            request.user.id,
            serializer.data,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['POST'], detail=False)
    def search(self, request):
        search_filter = self.get_search_filter(request)

        if not search_filter:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset = Customer.objects.filter(**search_filter)
        customer_ids_found = []
        for result in queryset:
            customer_ids_found.append(result.id)

        logger.info("Customer ids found: %s.", customer_ids_found)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_search_filter(self, request):
        search_filter = {}
        warning_invalid_search_option = False
        search_option = request.data.get('search_option')
        if search_option == 'zipCodeHouseNumber':
            zip_code = request.data.get('zip_code')
            house_number = request.data.get('house_number')
            search_filter = {
                'zip_code__icontains': zip_code,
                'house_number__icontains': house_number,
            }
        elif search_option == 'email':
            email = request.data.get('email')
            search_filter = {
                "email__icontains": email,
            }
        elif search_option == 'telephoneNumber':
            telephone_number = request.data.get('telephone')
            search_filter = {
                "telephone__icontains": telephone_number,
            }
        else:
            warning_invalid_search_option = True
            logger.warning(
                "Invalid search request: %s.",
                search_option
            )
        logger.info(
            "User id %s searched for %s with %s.",
            request.user.id,
            search_option,
            search_filter,
        )

        warning_blank_search = False
        for df in search_filter.values():
            if df:
                break
        else:
            warning_blank_search = True
            logger.warning("Blank searches not allowed.")

        if warning_blank_search or warning_invalid_search_option:
            return None

        return search_filter
