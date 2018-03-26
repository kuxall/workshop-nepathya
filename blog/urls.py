from django.conf.urls import url
from .views import post_list, post_new, post_details,edit_post,post_delete


urlpatterns = [
    url(r'^$', post_list, name='postssss'),
    url(r'^new-post/$', post_new, name='postssss'),
    url(r'^post_details/(?P<pk>\d+)/$', post_details, name='post_details'),
    url(r'^edit_post/(?P<pk>\d+)/$', edit_post, name='edit_post'),
    url(r'^post_delete/(?P<pk>\d+)/$', post_delete, name='post_delete'),
]
