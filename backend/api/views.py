from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BlogSerializer, EqubGroupSerializer, EqubMembershipSerializer, SavingsSerializer, TransactionSerializer, ProfileSerializer, UserFormSubmissionSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Savings, EqubMembership, Blog, Transaction, ProfileUser, UserFormSubmission
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data

        # Set cookies for access and refresh tokens
        response.set_cookie(
        key='access',
        value=data.get('access'),
        httponly=True,
        secure=False,  # Set to True in production for HTTPS
        samesite='Lax',  # Use 'Lax' to allow cross-origin cookies in non-top-level navigation
        max_age=1800,
        )

        response.set_cookie(
            key='refresh',
            value=data.get('refresh'),
            httponly=True,
            secure=False,  # Set to True in production for HTTPS
            samesite='Lax',
            max_age=86400,
        )


        # Remove tokens from the response body for security
        del response.data['access']
        del response.data['refresh']

        return response

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):

        response = Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        response.delete_cookie('accessToken')
        response.delete_cookie('refreshToken')
        return response
    
class UserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  # User is available via JWT authentication
        if not user.is_authenticated:
            raise AuthenticationFailed('User is not authenticated!')

        # Serialize user data
        return Response({
            'id': user.id,
            'username': user.username,
        })
    
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Fetch the profile associated with the logged-in user
            profile = ProfileUser.objects.get(user=request.user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data, status=200)
        except ProfileUser.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=404)

class UpdateUserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        try:
            # Retrieve the authenticated user's profile
            profile = ProfileUser.objects.get(user=request.user)
            serializer = ProfileSerializer(profile, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ProfileUser.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # Extract refresh token from cookies
        refreshToken = request.COOKIES.get('refreshToken')
        
        if not refreshToken:
            return Response(
                {"detail": "Refresh token is missing in cookies."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        # Inject refresh token into the request data
        request.data['refresh'] = refreshToken
        
        try:
            response = super().post(request, *args, **kwargs)
        except (InvalidToken, TokenError) as e:
            return Response(
                {"detail": "Invalid refresh token."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        # Extract the new access token
        data = response.data
        accessToken = data.get('access')
        
        # Set new access token in cookies
        response.set_cookie(
            key='accessToken',
            value=accessToken,
            httponly=True,  # Prevent client-side JavaScript access
            secure=False,   # Set to True in production with HTTPS
            samesite='Lax', # Adjust based on your app's requirements
            max_age=3600,   # 1 hour
        )
        
        # Optionally, remove the access token from response body
        response.data.pop('access', None)
        response.data['message'] = 'Access token refreshed and set in cookies'
        return response

class SavingListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # Fetch the profile associated with the logged-in user
            savings = Savings.objects.filter(user=request.user)
            serializer = SavingsSerializer(savings, many=True)
            return Response(serializer.data)
        except ProfileUser.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=404)

class UserEqubGroupAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user_membership = EqubMembership.objects.get(user=request.user)
            equb_group = user_membership.equb_group
            serializer = EqubGroupSerializer(equb_group)
            return Response(serializer.data)

        except EqubMembership.DoesNotExist:
            raise NotFound("The user is not a member of any Equb group.")

class UserEqubMembershipAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        try:
            user_membership = EqubMembership.objects.get(user=user)
        except EqubMembership.DoesNotExist:
            raise NotFound("The user is not a member of any Equb group.")
        equb_group = user_membership.equb_group
        other_memberships = EqubMembership.objects.filter(equb_group=equb_group)
        serializer = EqubMembershipSerializer(other_memberships, many=True)
        return Response(serializer.data)

class BlogPostPagination(PageNumberPagination):
    page_size = 10  # Set the number of blog posts per page

class BlogPostListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        blog_posts = Blog.objects.all()
        paginator = BlogPostPagination()
        result_page = paginator.paginate_queryset(blog_posts, request)
        serializer = BlogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class TransactionListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
            transaction = Transaction.objects.filter(user=user)
            serializer = TransactionSerializer(transaction, many=True)
            return Response(serializer.data)
        
        except EqubMembership.DoesNotExist:
            raise NotFound("The user is not a member of any Equb group.")

class UserFormSubmissionView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserFormSubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)