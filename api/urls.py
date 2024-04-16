from django.urls import path, include

urlpatterns = [
    path("beats/", include('beats.urls')),
    path("accounts/", include('accounts.urls')),

]
