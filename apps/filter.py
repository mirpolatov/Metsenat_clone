from django_filters import FilterSet, NumberFilter, CharFilter, IsoDateTimeFilter, RangeFilter
from rest_framework.fields import BooleanField, IntegerField, TimeField, CharField

from models import Student
from .models import Sponsor


class SponsorFilter(FilterSet):
    ariza = BooleanField()
    summa = RangeFilter()
    created_at = IsoDateTimeFilter()

    class Meta:
        model = Sponsor
        fields = ['ariza', 'summa', 'created_at']


class StudentFilter(FilterSet):
    student_category = CharField(max_length=255)
    otm = CharField(max_length=255)

    class Meta:
        model = Student
        fields = ['student_category', 'otm']
