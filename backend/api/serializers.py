from rest_framework import serializers
from .models import Savings, EqubGroup, EqubMembership, Blog, Transaction, ProfileUser, UserFormSubmission
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested User data

    class Meta:
        model = ProfileUser
        fields = ['profile_id', 'user', 'age', 'gender', 'country', 'first_name', 'last_name', 'user_image']


class SavingsSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested User data

    class Meta:
        model = Savings
        fields = ['savings_id', 'user', 'account_balance', 'account_type', 'interest_rate', 'created_at']



class EqubGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EqubGroup
        fields = ['equb_id', 'name', 'description', 'group_size', 'cycle_period', 'amount_per_cycle', 'start_date', 'created_at']


class EqubMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested User data
    equb_group = EqubGroupSerializer(read_only=True)  # Nested EqubGroup data

    class Meta:
        model = EqubMembership
        fields = ['membership_id', 'equb_group', 'user', 'join_date', 'role']


class BlogSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)  # Nested User data

    class Meta:
        model = Blog
        fields = ['blog_id', 'author', 'title', 'blog_image', 'content', 'created_at', 'updated_at']


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Nested User data

    class Meta:
        model = Transaction
        fields = ['transaction_id', 'user', 'transaction_type', 'amount', 'transaction_date']

class UserFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFormSubmission
        fields = "__all__"