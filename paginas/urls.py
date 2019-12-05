from django.urls import path
from .views import TrabalhoPageView, ONGsDeAnimaisPageView, ONGsDeAnimaisPedroIIView, VoluntariadoView, ListadeEventosView, oqEView
urlpatterns = [
    path('', TrabalhoPageView.as_view(), name ='trabalho'),
    path('ongsdeanimais/', ONGsDeAnimaisPageView.as_view(), name ='ongsdeanimais'),
    path('ongsdeanimaispedroii/', ONGsDeAnimaisPedroIIView.as_view(), name ='ongsdeanimaispii'),
    path('voluntariado/', VoluntariadoView.as_view(), name ='voluntariado'),
    path('eventos/', ListadeEventosView.as_view(), name ='eventos'),
    path('oqe/', oqEView.as_view(), name ='oqe'),
]
