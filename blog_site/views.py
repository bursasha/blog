from django.shortcuts import redirect, render
from .models import *
from django.views.generic import View
from django.core.paginator import Paginator
from blog_site.forms import PostForm, TagForm
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin

# Create your views here.

def home_page(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)



    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        prev_url = ''

    context = {
        'page_object': page,

        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'blog_site/home_page.html', {'page_object': page})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog_site/tags_list.html', {'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog_site/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog_site/tag_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog_site/post_create.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog_site/tag_create.html'
    redirect_to_tags = True


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog_site/post_update_form.html'

    # def get(self, request, slug):
    #     post = Post.objects.get(slug__iexact=slug)
    #     bound_form = PostForm(instance=post)
    #     context = {'form': bound_form, 'post': post}
    #     return render(request, 'blog_site/post_update_form.html', context)
    #
    # def post(self, request, slug):
    #     post = Post.objects.get(slug__iexact=slug)
    #     bound_form = PostForm(request.POST, instance=post)
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #
    #     context = {'form': bound_form, 'post': post}
    #     return render(request, 'blog_site/post_update_form.html', context)


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog_site/tag_update_form.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog_site/post_delete_form.html'
    redirect_url = 'home_page'

    # def get(self, request, slug):
    #     post = Post.objects.get(slug__iexact=slug)
    #     return render(request, 'blog_site/post_delete_form.html', {'post': post})
    #
    # def post(self, request, slug):
    #     post = Post.objects.get(slug__iexact=slug)
    #     post.delete()
    #     return redirect(reverse('home_page'))


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog_site/tag_delete_form.html'
    redirect_url = 'home_page'
