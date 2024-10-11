from django.urls import path
from .views import signup, user_logout, get_user_profile, login, logout, match_talents_brands_view, match_brands_talents_view
from .views import BrandIndicatorView, BrandCardView, StatisticsDataView, TalentCardView, RevenueCardView, RevenueInsightsView, FinancialDashboardView

urlpatterns = [
    path('api/signup/', signup, name='signup'),
    path('api/logout/', user_logout, name='logout'),
    path('api/user/<int:id>/', get_user_profile, name='get_user_profile'),
    path('api/login/', login, name='login'),
    path('api/logout/', logout, name='logout'),
    path('api/match-talents-brands/', match_talents_brands_view, name='match_talents_brands'),
    path('api/match-brands-talents/', match_brands_talents_view, name='match_brands_talents'),
    path('api/brand-indicators/', BrandIndicatorView.as_view(), name='brand_indicators'),
    path('api/brand-cards/', BrandCardView.as_view(), name='brand_cards'),
    path('api/statistics-data/', StatisticsDataView.as_view(), name='statistics_data'),
    path('api/talent-card/', TalentCardView.as_view(), name='talent_card'),
    path('api/revenue-card/', RevenueCardView.as_view(), name='revenue_card'),
    path('api/revenue-insights/', RevenueInsightsView.as_view(), name='revenue_insights'),
    path('api/financial-dashboard/', FinancialDashboardView.as_view(), name='financial_dashboard'),
]
