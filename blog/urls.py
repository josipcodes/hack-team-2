from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.BlogList.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.BlogDetail.as_view(), name='blog_post'),
    path('add_blog/', views.AddBlogView.as_view(), name='add_blog'),
    path('edit_blog/<slug:slug>/', views.EditBlog.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>/', views.DeleteBlog.as_view(), name='delete_blog'),
    path('edit_comment/<int:comment_id>/', views.EditCommentView.as_view(), name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.DeleteCommentView.as_view(), name='delete_comment'),
]