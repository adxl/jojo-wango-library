from django.urls import include, path  # type: ignore

from libraries.views import add_library, index

urlpatterns = [
    
    path('library/' , index , name='index'),
    path('library/add/' , add_library , name='index'),
    
]
