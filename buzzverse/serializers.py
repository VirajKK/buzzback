from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("User is disabled.")
                return user
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user



class BrandIndicatorSerializer(serializers.Serializer):
    title = serializers.CharField()
    data = serializers.ListField()  # List of dictionaries with 'name' and 'value' keys
    colors = serializers.ListField()

class BrandCardSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()  # Assuming you're storing image paths
    details = serializers.DictField()  # Assuming 'details' is a dictionary


class StatisticsSerializer(serializers.Serializer):
    name = serializers.CharField()
    Revenue = serializers.FloatField()
    InProgress = serializers.FloatField()
    Rejected = serializers.FloatField()

class TalentSerializer(serializers.Serializer):
    image = serializers.CharField()
    name = serializers.CharField()
    roles = serializers.ListField(child=serializers.CharField())
    description = serializers.CharField()
    contactName = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

class RevenueCardSerializer(serializers.Serializer):
    totalRevenue = serializers.FloatField()
    activeDeals = serializers.IntegerField()
    engagementMetric = serializers.IntegerField()
    recentActivity = serializers.CharField()



class RevenueInsightsSerializer(serializers.Serializer):
    name = serializers.CharField()
    value = serializers.FloatField()

class FinancialDataSerializer(serializers.Serializer):
    name = serializers.CharField()
    Revenue = serializers.FloatField()
    Expense = serializers.FloatField()

class RevenueInsightsResponseSerializer(serializers.Serializer):
    revenueInsights = RevenueInsightsSerializer(many=True)
    financialData = FinancialDataSerializer(many=True)



class FinancialDataSerializer(serializers.Serializer):
    name = serializers.CharField()
    Current = serializers.FloatField()
    Previous = serializers.FloatField()

class ForecastDataSerializer(serializers.Serializer):
    month = serializers.CharField()
    revenue = serializers.FloatField()

class FinancialDashboardResponseSerializer(serializers.Serializer):
    revenueData = FinancialDataSerializer(many=True)
    rocsData = FinancialDataSerializer(many=True)
    forecastData = ForecastDataSerializer(many=True)