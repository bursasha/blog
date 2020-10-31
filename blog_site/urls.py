from blog_site.views import PostCreate, TagCreate, PostDetail, TagDetail, PostUpdate, TagUpdate, PostDelete, TagDelete, home_page, tags_list
from django.urls import path

urlpatterns = [
    path('', home_page, name='home_page'),
    path('tags/', tags_list, name='tags_list'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tags/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('posts/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),

]
