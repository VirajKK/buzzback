from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    UserSerializer, LoginSerializer, BrandIndicatorSerializer, 
    BrandCardSerializer, StatisticsSerializer, TalentSerializer, 
    RevenueCardSerializer, RevenueInsightsResponseSerializer, 
    FinancialDashboardResponseSerializer
)
from .BuzzMatch import match_talents_with_brands, match_brands_with_talents

# Helper function to get JSON response for errors
def get_error_response(message, status_code=status.HTTP_400_BAD_REQUEST):
    return Response({"error": message}, status=status_code)

# User Signup
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return get_error_response(serializer.errors)

# User Logout
@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)

# Get User Profile
@api_view(['GET'])
def get_user_profile(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return get_error_response("User not found.", status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

# User Login
@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    # Hardcoded user validation
    if email == 'user@gmail.com' and password == 'user123':
        # Create a JWT token manually
        refresh = RefreshToken.for_user(None)  # Normally, you would pass a user instance here

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': 'Login successful',
        })

    return Response({'message': 'Invalid credentials'}, status=400)


# JWT Token Logout
@api_view(['POST'])
def logout_with_token(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
    except KeyError:
        return get_error_response("Refresh token is required.")
    except Exception as e:
        return get_error_response(str(e))

# Match Talents with Brands
@api_view(['GET'])
def get_matches_talents_brands(request):
    matches = match_talents_with_brands()
    return Response(matches, status=status.HTTP_200_OK)

# Match Brands with Talents
@api_view(['GET'])
def get_matches_brands_talents(request):
    matches = match_brands_with_talents()
    return Response(matches, status=status.HTTP_200_OK)

# Brand Indicator View
class BrandIndicatorView(APIView):
    def get(self, request):
        chart_data = [
            {
                "title": "Ethical Stance",
                "data": [
                    {"name": "Sustainability Efforts", "value": 30},
                    {"name": "Community Involvement", "value": 25},
                    {"name": "Ethical Practices", "value": 20},
                    {"name": "Transparency Level", "value": 15},
                    {"name": "Transparency Level", "value": 10},
                ],
                "colors": ["#00C49F", "#00A3A1", "#00869E", "#006B96", "#005088"],
            },
            {
                "title": "Performance Indicators",
                "data": [
                    {"name": "Market Share", "value": 35},
                    {"name": "Growth Rate", "value": 25},
                    {"name": "Customer Satisfaction", "value": 20},
                    {"name": "Brand Awareness", "value": 15},
                    {"name": "Financial Health", "value": 5},
                ],
                "colors": ["#00C49F", "#00A3A1", "#00869E", "#006B96", "#005088"],
            },
            {
                "title": "Brand Personality",
                "data": [
                    {"name": "Brand Archetype", "value": 30},
                    {"name": "Emotional Appeal", "value": 25},
                    {"name": "Storytelling Approach", "value": 20},
                    {"name": "Customer Experience", "value": 15},
                    {"name": "Brand Differentiators", "value": 10},
                ],
                "colors": ["#9ACD32", "#BADA55", "#7FFF00", "#90EE90", "#ADFF2F"],
            },
            {
                "title": "Audience demographic",
                "data": [
                    {"name": "Primary Audience", "value": 35},
                    {"name": "Age Group", "value": 25},
                    {"name": "Audience Split", "value": 15},
                    {"name": "Audience Interest", "value": 10},
                    {"name": "Audience location", "value": 10},
                    {"name": "Audience Engagement", "value": 5},
                ],
                "colors": ["#FF6347", "#FF4500", "#FF6961", "#FF7F50", "#FA8072", "#FFA07A"],
            },
            {
                "title": "Customer Insights",
                "data": [
                    {"name": "Customer Age Range", "value": 30},
                    {"name": "Customer Gender Split", "value": 25},
                    {"name": "Customer Interests", "value": 20},
                    {"name": "Customer Geographic Spread", "value": 15},
                    {"name": "Customer Loyalty", "value": 10},
                ],
                "colors": ["#FFA500", "#FFD700", "#FFFF00", "#FAFAD2", "#FFFACD"],
            },
            {
                "title": "Social media Strategy",
                "data": [
                    {"name": "Active Platforms", "value": 30},
                    {"name": "Brand Voice", "value": 25},
                    {"name": "Content Themes", "value": 20},
                    {"name": "Engagement Strategies", "value": 15},
                    {"name": "Influencer Partnerships", "value": 10},
                ],
                "colors": ["#00BFFF", "#1E90FF", "#87CEFA", "#4169E1", "#6495ED"],
            },
        ]
        serializer = BrandIndicatorSerializer(chart_data, many=True)
        return Response(serializer.data)

# Brand Card View
class BrandCardView(APIView):
    def get(self, request):
        card_data = [
            {
                "title": "Brand Identity",
                "image": "../src/assets/logo.svg",
                "details": {
                    "Brand Value": "Elegance",
                    "Industry": "Watches",
                    "Market Position": "Industry Leader",
                    "Target Demographics": "Professionals",
                }
            },
            {
                "title": "Marketing Goals",
                "image": "../src/assets/marketinggoals.svg",
                "details": {
                    "Key Messages": "Timeless Elegance",
                    "Desired Image": "Premium Lifestyle",
                    "Marketing Goals": "Brand Loyalty",
                    "Objectives": "Increase Engagement",
                    "Product Lines": "Watches, Jewellery, Eyewear",
                    "Service Offerings": "Customization Services & Eye Testing - service",
                }
            },
            {
                "title": "Corporate Culture",
                "image": "../src/assets/corporateculture.svg",
                "details": {
                    "Workplace Culture": "Dynamic, Inclusive",
                    "Innovation Focus": "Continuous Improvement",
                    "Leadership Style": "Visionary Leadership",
                    "Employee Diversity": "Generational, Ability",
                    "Company Size": "Global Presence",
                }
            },
            {
                "title": "Communication Style",
                "image": "../src/assets/communicationstyle.svg",
                "details": {
                    "Media Relations": "Press Outreach",
                    "PR Strategies": "Brand Positioning",
                    "Crisis Management": "Crisis Response",
                    "Community Engagement": "Social Responsibility",
                }
            },
        ]
        serializer = BrandCardSerializer(card_data, many=True)
        return Response(serializer.data)

# Statistics Data View
class StatisticsDataView(APIView):
    def get(self, request):
        statistics_data = [
            { "name": "Jan", "Revenue": 75, "InProgress": 55, "Rejected": 15 },
            { "name": "Feb", "Revenue": 62, "InProgress": 48, "Rejected": 25 },
            { "name": "March", "Revenue": 45, "InProgress": 60, "Rejected": 20 },
            { "name": "April", "Revenue": 50, "InProgress": 40, "Rejected": 35 },
            { "name": "May", "Revenue": 80, "InProgress": 70, "Rejected": 10 },
            { "name": "June", "Revenue": 68, "InProgress": 30, "Rejected": 22 },
            { "name": "July", "Revenue": 55, "InProgress": 65, "Rejected": 18 },
            { "name": "Aug", "Revenue": 60, "InProgress": 25, "Rejected": 28 },
            { "name": "Sept", "Revenue": 90, "InProgress": 85, "Rejected": 12 },
            { "name": "Oct", "Revenue": 40, "InProgress": 95, "Rejected": 20 },
            { "name": "Nov", "Revenue": 70, "InProgress": 15, "Rejected": 30 },
            { "name": "Dec", "Revenue": 70, "InProgress": 20, "Rejected": 25 },
        ]
        serializer = StatisticsSerializer(statistics_data, many=True)
        return Response(serializer.data)

# Talent Card View
class TalentCardView(APIView):
    def get(self, request):
        talent_data = {
            "image": "/talent.svg",
            "name": "Actor Name",
            "roles": ["Actor", "Producer", "Special Appearances", "Voice Cast"],
            "description": "Indian actor and film producer...",
            "contactName": "Dr Ashwin",
            "email": "ashwin@gmail.com",
            "phone": "+91-74XX-XXX-XXX",
        }
        serializer = TalentSerializer(talent_data)
        return Response(serializer.data)

# Revenue Card View
class RevenueCardView(APIView):
    def get(self, request):
        revenue_data = {
            "totalRevenue": 10000000,
            "activeDeals": 10,
            "engagementMetric": 234,
            "recentActivity": "Signed Deals with Brands XYZ",
        }
        serializer = RevenueCardSerializer(revenue_data)
        return Response(serializer.data)

# Revenue Insights View
class RevenueInsightsView(APIView):
    def get(self, request):
        revenue_insights_data = [
            { "name": "Brand", "value": 40 },
            { "name": "Film", "value": 30 },
            { "name": "Appearances", "value": 30 },
            { "name": "Endorsements", "value": 30 },
        ]

        financial_data = [
            { "name": "Jan", "Revenue": 1.5, "Expense": 1 },
            { "name": "Feb", "Revenue": 1.7, "Expense": 1.2 },
            { "name": "Mar", "Revenue": 1.6, "Expense": 1.3 },
            { "name": "Apr", "Revenue": 1.8, "Expense": 1.4 },
            { "name": "May", "Revenue": 2.0, "Expense": 1.5 },
        ]

        response_data = {
            "revenueInsights": revenue_insights_data,
            "financialData": financial_data,
        }

        serializer = RevenueInsightsResponseSerializer(response_data)
        return Response(serializer.data)

# Financial Dashboard View
class FinancialDashboardView(APIView):
    def get(self, request):
        revenue_data = [
            { "name": "Mon", "Current": 1000, "Previous": 800 },
            { "name": "Tue", "Current": 1200, "Previous": 1000 },
            { "name": "Wed", "Current": 1400, "Previous": 1200 },
            # Add remaining data...
        ]

        rocs_data = [
            { "name": "Mon", "Current": 2000, "Previous": -2000 },
            { "name": "Tue", "Current": 2200, "Previous": -1800 },
            # Add remaining data...
        ]

        forecast_data = [
            { "month": "Jan", "revenue": 32 },
            { "month": "Feb", "revenue": 10 },
            # Add remaining data...
        ]

        response_data = {
            "revenueData": revenue_data,
            "rocsData": rocs_data,
            "forecastData": forecast_data,
        }

        serializer = FinancialDashboardResponseSerializer(response_data)
        return Response(serializer.data)
