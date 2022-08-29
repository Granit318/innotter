from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from page.models import Page, Post


class PageService:
    def main_page(self, request):
        signed_posts = []
        current_user = request.user
        page = Page.objects.filter(owner=current_user.id).first()
        posts = Post.objects.filter(page_id=page.id)
        signed_authors = list(current_user.follows.all())
        for author in signed_authors:
            signed_posts.append({'posts': list(Post.objects.filter(page_id=author.id).values('created_at', 'content')),
                                 'author_name': author.name})
        return JsonResponse({'posts': list(posts.all().values('created_at', 'content')),
                             'signed_posts': signed_posts})


class PostService:
    def create_post(self, request):
        if request.method == 'GET':
            return render(request, 'posts/create_post.html')
        elif request.method == 'POST':
            current_user = request.user
            page = Page.objects.filter(owner=current_user.id).first()
            post_text = request.POST.get('post')
            post_obj = Post(page=page,
                            content=post_text)
            post_obj.save()
            return HttpResponse('Пост создан')
        else:
            raise NotImplemented
