from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect, Http404
from django.views import View, generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Blog, Comment, BlogCategory
from .forms import CommentForm, BlogForm

def home(request):
    latest_blogs = Blog.objects.order_by('-created_on')[:3]
    categories = BlogCategory.objects.all()
    return render(request, 'index.html', {'latest_blogs': latest_blogs, 'categories': categories})

# def blog(request):
#     return HttpResponse("Hello, Blogland!")

class BlogList(generic.ListView):
    model = Blog
    queryset = Blog.objects.order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 12

class BlogDetail(View):

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Blog, slug=slug)
        comments = post.comments.all().order_by('created_on')

        return render(
            request,
            "blog_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Blog, slug=slug)
        comments = post.comments.all().order_by('created_on')

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.blogpost = post
            comment.user = request.user
            comment.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('blog_post', slug=post.slug)

        return render(
            request,
            "blog_post.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": comment_form,
            },
        )

class AddBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'add_blog.html'
    fields = ['title', 'content', 'excerpt', 'image', 'blog_category']
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        if not self.request.user.is_staff:
            raise Http404
        blog = form.save(commit=False)
        blog.slug = slugify(blog.title)
        blog.author = self.request.user
        blog.save()
        messages.success(self.request, f"Blog post '{blog.title}' added successfully.")
        return super().form_valid(form)

class EditBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'edit_blog.html'

    def get_success_url(self):
        slug = self.object.slug
        messages.success(self.request, f"Blog post '{self.object.title}' updated successfully.")
        return reverse_lazy('blog_post', kwargs={'slug': slug})

class DeleteBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('blog')

    def get_success_url(self):
        messages.success(self.request, f"Blog post '{self.object.title}' deleted successfully.")
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['delete_title'] = "Delete Blog Post"
        context['confirm_message'] = f"Are you sure you want to delete this blog post '{self.object.title}'?"
        context['cancel_url'] = reverse_lazy('blog_post', kwargs={'slug': self.object.slug})
        return context

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class EditCommentView(View):
    template_name = 'edit_comment.html'

    def get(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(instance=comment)
        context = {'comment': comment, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            post_slug = comment.blogpost.slug
            messages.success(request, 'Comment edited successfully.')
            return redirect('blog_post', slug=post_slug)

        context = {'comment': comment, 'form': form}
        return render(request, self.template_name, context)

class DeleteCommentView(View):
    template_name = 'delete.html'

    def get(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        context = {
            'delete_title': "Delete Comment",
            'confirm_message': "Are you sure you want to delete this comment?",
            'cancel_url': reverse_lazy('blog_post', kwargs={'slug': comment.blogpost.slug}),
            'comment': comment
        }
        return render(request, self.template_name, context)

    def post(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        post_slug = comment.blogpost.slug
        comment.delete()
        messages.success(request, 'Comment deleted successfully.')
        return redirect('blog_post', slug=post_slug)