# _*_ coding: utf-8 _*_


def add_node(tree_dic,comment):#生成对象的树状结构
    if comment.parent_comment is None:
        #如果我的父层是None,代表自己就是顶层
        tree_dic[comment] = {}
    else:
        for k,v in tree_dic.items():
            if k == comment.parent_comment:
                #如果找到父层就把自己作为值复制一个字典
                tree_dic[comment.parent_comment][comment] = {}
            else:
                add_node(v,comment)
                #没找到就继续递归查找

#评论的结构是一个树形层级结构
# tree_dic = { 1:{2:{4:{},},
#                 5:{9:{}}
#              },
#              3:{6:{7:{}}
#              },
# }


def build_tree(comment_set):
    tree_dic={}
    for comment in comment_set:
        add_node(tree_dic,comment)
    return  tree_dic
    #返回评论数



def render_comment(tree_dic,mar_val=0):
    html = ""
    mar_val+=20
    span_css = '<span style="margin-left:20px">%s </span>'
    add_comment_css = '<span class="glyphicon glyphicon-comment add-comment " aria-hidden="True" style="margin-left:20px" comment-id="%s"></span>'
    # 不知道为什么后端传的html到前端自定义的CSS不生效,用bootstrap的样式又可以..
    for k,v in tree_dic.items():
        if k.parent_comment == None:
            #判断是否有父评论,没有自己就是第一级评论
            div_class = '<div style="border: 1px solid darkcyan; color: #999; margin-bottom: 5px;">'
        else:
            #子级评论都向右移动20px
            div_class = '<div style="border: 1px solid darkcyan; color: #999; margin-bottom: 5px; margin-left:%spx">'%mar_val

        ele = div_class + k.comment  \
            + span_css % k.comm_date \
            + span_css % k.user.name  \
            + add_comment_css %k.id \
            + '</div>'
            #把评论内容,时间,作者,以及id传给前端
        html += ele
        html += render_comment(v,mar_val)
        #循环处理根评论,将子评论给render_tree_node处理
    return html
