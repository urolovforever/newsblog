from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('all-news', all_news, name='all_news'),
    path('detail/<int:id>', detail, name='detail'),
    path('category/<int:id>', category, name='category'),
    path('all-categories', all_category, name='all-category'),
    path('region/<int:pk>', region, name='region'),
    path('all-regions', all_region, name='all-region'),
    path('create-post/new',Create_post.as_view(), name='create_post'),
    path('edit-post/<int:pk>',Edit_post.as_view(), name='edit_post'),
    path('delete-post/<int:pk>', Delete_post.as_view(), name='delete_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
