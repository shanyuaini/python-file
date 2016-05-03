#_*_coding:utf-8_*_
__author__ = 'sylar'


from day11.sylarWebFrames.template_handle import env


def render_to_response(request,response,data,status=200):
    if status == 200:
        status = '200 OK'
    if status == 404:
        status = '404 Page not find'

    response_headers = [('Content-type','text/html')]
    response(status, response_headers)
    return [data]

def index(**kwargs):

    request = kwargs.get('request')
    response = kwargs.get('http_response')
    print dir(env)
    html_template = env.get_template('index.html')

    html = '''
    <html>
        <body>
            <div style="height:50px;width:100%;background:yellow">
                TEST TOP MENU
            </div>
        </body>
    </html>
    '''
    name_dic = {'alex':29,'jack':33,'rain':23}

    html= html_template.render(name="alexddd", name_dic=name_dic)
    return  render_to_response(request,response,str(html))



def login(**kwargs):

    request = kwargs.get('request')
    response = kwargs.get('http_response')

    html = '''
    <html>
        <body>
            <div >
                <h3>LOGIN</h3>

                <form >
                    Username<input type='text' name='username'/>
                    Password<input type='password' name='password'/>
                    <input type='submit' value='Login'/>
                </form>
            </div>
        </body>
    </html>
    '''
    return  render_to_response(request,response,html)

