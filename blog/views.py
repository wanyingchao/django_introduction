from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
# django分页组件包
from django.core.paginator import Paginator

# Create your views here.


def hello_word(request):
    return HttpResponse('hello word')


def article_content(request):
    articles = Article.objects.all()
    article = articles[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title:%s, brief_content:%s, content:%s, article_id:%s, publish_date:%s' % (title, brief_content, content, article_id, publish_date)
    return HttpResponse(return_str)


def get_index_page(request):
    # 获取请求里面page参数的值
    page = request.GET.get('page')
    if page:
        page = int(page)
    else:
        page = 1
    # 获取所有文章list
    all_article = Article.objects.all()
    # 所有文章分组，5篇一组
    paginator = Paginator(all_article, 5)
    # 获取分组后的组数
    page_num = paginator.num_pages
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page + 1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous_page = page - 1
    else:
        previous_page = page
    return render(request, 'index.html', {
        'article_list': page_article_list,
        'page_num': range(1, page_num + 1),
        'curr_page': page,
        'next_page': next_page,
        'previous_page': previous_page
    })


def get_detail_page(request, article_id):
    curr_article = None
    all_article = Article.objects.all()
    previous_article = None
    next_article = None
    for index, article in enumerate(all_article):
        if index == 0:
            previous_index = 0
            next_index = index + 1
        elif index == len(all_article) - 1:
            previous_index = index - 1
            next_index = index
        else:
            previous_index = index - 1
            next_index = index + 1
        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break
    section_list = curr_article.content.split('\n')
    return render(request, 'detail.html',
                  {
                      'curr_article': curr_article,
                      'section_list': section_list,
                      'previous_article': previous_article,
                      'next_article': next_article
                  })
