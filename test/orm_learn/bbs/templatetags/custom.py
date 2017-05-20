# _*_ coding: utf-8 _*_

from django import template


register = template.Library()

@register.filter
def truncate_url(img_obj):
    print(dir(img_obj))
    return img_obj.name.split('/',maxsplit=1)[-1]
#models中返回的img的存储位置是statics/images/uploads/startproject_RTEbObC.png,
#setting时中定义了静态文件是用static别名,不能直接从statics路径去访问
#所以将前端后去的img对象传到这里将statics截取掉返回给前端.在前端重写一下图片的正确路径.

@register.simple_tag
def filter_comment(article_obj):
    query_set = article_obj.comment_set.select_related()
    comments = {
        'comment_count' : query_set.filter(comment_type=1).count(),
        'thumb_count' : query_set.filter(comment_type=2).count()
    }
    return comments
#分别计算评论数和点赞总数


@register.filter
def lower(val):
    return val.lower()

@register.simple_tag
def handle_page_num(current_page,loop_num):
    if current_page == loop_num:
        return "active"