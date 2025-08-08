from django.urls import path
from .views import (
    soil_quality_view, soil_result_view, about_view,
    contact_view, soil_view, login_view, logout_view,signup_view
)

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', soil_quality_view, name='soil_quality'),
    path('result/<int:soil_id>/', soil_result_view, name='soil_result'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('soil/', soil_view, name='contact'),
    path('signup/', signup_view, name='signup'),

]
