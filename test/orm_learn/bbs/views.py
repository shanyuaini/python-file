from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from bbs import models
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from bbs import comment_handler
from bbs import article_forms
import json
# Create your views here.

category_list = models.Category.objects.filter(set_as_top=True).order_by('position_index')
# 通过 set_as_top取到要在前端顶部展示的板块

def index(request):
    category_obj = models.Category.objects.get(position_index=1) #将首页定位到'全部'板块
    article_list = models.Article.objects.filter(status=2)
    return render(request,'bbs/index.html',{'category_list':category_list,
                                            'category_obj':category_obj,
                                            'article_list':article_list,})

def category(request,id):
    category_obj = models.Category.objects.get(id=id)
    #获取到用户在首页点击的顶部板块
    if category_obj.position_index == 1:#position_index 为1标识点的前端的'全部'板块
        article_list = models.Article.objects.filter(status=2)
    else:#如果是其他板块就值选择本板块的文章
        article_list = models.Article.objects.filter(category_id = category_obj.id, status=2)
    #获取板块所属的文章列表,并且状态为发布

    return render(request,'bbs/index.html',{'category_list':category_list,
                                            'category_obj':category_obj,
                                            'article_list':article_list,})


def user_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        #是用authenticate验证用户密码
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(request.GET.get('next') or '/bbs')
            #登录成功返回通过next方法传过来的路径,或者是回到首页
        else:
            login_err = '错误的用户名或密码'
            return render(request,'login.html',{'login_err':login_err})
    return render(request,'login.html')
#


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/bbs')


def article_detail(request,article_id):
    article_obj = models.Article.objects.get(id=article_id)
    #获取文章对象
    return render(request,'bbs/article_detail.html',{'article_obj':article_obj,
                                                     'category_list': category_list,})

def post_comment(request):
     if request.method == 'POST':
        new_comment_obj = models.Comment(
            article_id = request.POST.get('article_id'),
            parent_comment_id = request.POST.get('parent_comment_id'),
            comment_type = request.POST.get('comment_type'),
            user_id = request.user.userprofile.id,
            comment = request.POST.get('comment')
        )
        new_comment_obj.save()
     return HttpResponse('post-comment-success')



def get_comments(request,article_id):
    article_obj = models.Article.objects.get(id=article_id)
    #通过文章id获取文章对象
    comment_tree = comment_handler.build_tree(article_obj.comment_set.select_related())
    #把文章对象给后端处理函数comment_handler.build_tree生成树
    tree_html = comment_handler.render_comment(comment_tree)
    #把评论树对象给html渲染函数,因为前端不能处理递归的数据,所以在后端渲染好返回给前端
    return HttpResponse(tree_html)

#@login_required(login_url='/login/') 在每个需要验证角色的地方指定登录页面或者在settings里设置
@login_required
def new_article(request):
    if request.method == 'GET':
        page_form = article_forms.ArticleModelForm()
        return render(request,'bbs/new_article.html',{'category_list': category_list,
                                                      'article_form' : page_form})
    elif request.method == 'POST':
        page_form = article_forms.ArticleModelForm(request.POST,request.FILES)
        if page_form.is_valid():
            data = page_form.cleaned_data
            data['author_id'] = request.user.userprofile.id
            article_obj = models.Article(**data)
            article_obj.save()
            #应为我们在article_forms.ArticleModelForm中隐藏了author,当前端传回的form时,page_form对象并没有author
            #然而page_form对象不能修改,author_id在models中又是必须的字段.使用cleaned_data将对象转为一个data字典.
            #因为用户以及验证过,直接将用户ID插入字典.
            #最后将字典转为一个models对象进行数据库操作
        else:
            return render(request, 'bbs/new_article.html', {'category_list': category_list,
                                                            'article_form': page_form})




def file_upload(request):
    file_obj = request.FILES.get('filename')
    with open('statics/images/uploads/%s'%file_obj.name, 'wb+') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)
    return render(request, 'bbs/new_article.html')


def get_latest_article_count(request):
    latest_article_id = request.GET.get('latest_id')
    if latest_article_id:
        new_article_count = models.Article.objects.filter(id__gt = latest_article_id).count()
    else:
        new_article_count = 0
    return HttpResponse(json.dumps({'new_article_count' : new_article_count}))