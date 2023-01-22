from django.urls import include, path  # type: ignore

from libraries.views import index

urlpatterns = [
    
    path('library/' , index , name='index'),
    
]
