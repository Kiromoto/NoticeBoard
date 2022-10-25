from django.urls import path
from .views import AdList, AdEdit, AdDetail, AdDelete, MyAdList, ResponseDelete, MyResponsesList
from .views import ad_create, response_create, accept_response, reject_response
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', AdList.as_view(), name='ads_list'),
                  path('create/', ad_create, name='ad_create'),
                  path('<int:pk>', AdDetail.as_view(), name='ad_detail'),
                  path('<int:pk>/edit/', AdEdit.as_view(), name='ad_edit'),
                  path('<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
                  path('responsecreate/<int:pk>/', response_create, name='response_create'),
                  path('myads/', MyAdList.as_view(), name='my_ads'),
                  path('myresponses/', MyResponsesList.as_view(), name='my_responses'),
                  path('accept/<int:pk>/', accept_response, name='accept_response'),
                  path('reject/<int:pk>/', reject_response, name='reject_response'),
                  path('response/delete/<int:pk>', ResponseDelete.as_view(), name='response_delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
