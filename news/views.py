from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def PostNewsList(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	paginator = Paginator(posts, 9)
	page = request.GET.get('page')
	try:
		posts_list = paginator.page(page)
	except PageNotAnInteger:
		posts_list = paginator.page(1)
	except EmptyPage:
		posts_list = paginator.page(paginator.num_pages)


	return render(request, 'news/list_news.html', {'posts':posts_list})

def PostNewsDetail(request, id):
	post = get_object_or_404(Post, id=id)
	return render(request, 'news/detail_news.html', {'post':post})

	