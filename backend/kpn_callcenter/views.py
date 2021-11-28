from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(methods=['POST'], detail=False)
    def search(self, request):
        search_filter = self.get_search_filter(request)

        if not search_filter:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset = Customer.objects.filter(**search_filter)
        customer_ids_found = []
        for result in queryset:
            customer_ids_found.append(result.id)

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

        warning_blank_search = False
        for df in search_filter.values():
            if df:
                break
        else:
            warning_blank_search = True

        if warning_blank_search or warning_invalid_search_option:
            return None

        return search_filter
