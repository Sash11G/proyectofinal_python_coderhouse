

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import BlogPostForm
from .models import BlogPost
from accounts.models import Avatar
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test, login_required






from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver




# User authentication



def home(request):
    return render(request, "cliente/index.html")

def render_form(request, form, template_name):
    return render(request, template_name, {"myForm": form})



def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            print(data)  # Debugging

            new_blog_post = BlogPost(
                titulo=data["titulo"],
                subtitulo=data["subtitulo"],
                contenido=data["contenido"],
                post_image=data["post_image"],
                autor=request.user
            )

            new_blog_post.save()

            return redirect('cliente:blogpost-list')  
    else:
        form = BlogPostForm()

    return render(request, 'cliente/blogpost_form.html', {'form': form})



def blogpost_list(request):
    # Retrieve all blog posts
    blog_posts = BlogPost.objects.all()[::-1]

    # Create a list to store tuples of (blog_post, avatar)
    blog_posts_with_avatars = []

    # Iterate through each blog post
    for blog_post in blog_posts:
        avatar = Avatar.objects.filter(user=blog_post.autor).last()
        blog_posts_with_avatars.append((blog_post, avatar))

    context = {
        'blog_posts_with_avatars': blog_posts_with_avatars,
    }

    return render(request, 'cliente/blogpost_list.html', context)




class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'cliente/blogpost_detail.html'  # Change this to the actual template name
    context_object_name = 'blog_post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the avatar for the blog post's author
        
        avatar = Avatar.objects.filter(user=context['blog_post'].autor).last()
        context['avatar'] = avatar
        print(context)
        return context
    
 
class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'cliente/blogpost_update.html'
    success_url = reverse_lazy('cliente:blogpost-list')

    def form_valid(self, form):
        action = self.request.POST.get('action')

        if action == 'Update Post':
            return super().form_valid(form)
        elif action == 'Delete Post':
            self.object.delete()
            return redirect('cliente:blogpost-list')
        else:
            # Handle other actions or provide an error message
            pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_post'] = self.get_object()
        return context

    ## blog delete ##

