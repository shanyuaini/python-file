from django.shortcuts import render,HttpResponse

# Create your views here.




def login(request):
    html_content = '''
    Username: <input username = 'username' />
    Password: <input passwd = 'password' />
    '''
    #f= file('you_html_file')
    #html_data = f.read()
    return HttpResponse(html_content)
    #return HttpResponse(html_data)
def article(request,year,month,article_id):
    print '---Year---',year
    return HttpResponse('ddd')

def index(request):
    name_info = {
        'name':'sylar',
        'age': 18,
        'job': 'it'
    }

    return render(request,'index.html',{
        'yourPorn':'sylar',
        'name_info':name_info
    })

def host(request):
    return render(request,'host.html')