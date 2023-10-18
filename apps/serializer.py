from rest_framework.fields import HiddenField, CurrentUserDefault, IntegerField, CharField
from rest_framework.serializers import ModelSerializer

from apps.models import Sponsor, Users, Student


class LoginModelSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'fullname', 'password']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class SponsorModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Sponsor
        fields = ('user', 'fullname', 'phone_number', 'summa', 'tashkilot_nomi')


class StudentModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Student
        fields = ('user', 'fullname', 'phone_number', 'otm', 'student_category', 'summa')


class SponsorUpdateSerializer(ModelSerializer):
    id = CharField(read_only=True)
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Sponsor
        fields = ('id', 'user', 'fullname', 'phone_number', 'summa', 'tashkilot_nomi')
