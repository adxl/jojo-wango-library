from django.urls import include, path  # type: ignore

from libraries.views import add_library, index

urlpatterns = [
    path('library/' , index , name='library'),
    path('library/add/' , add_library , name='library_add'),
    
]
