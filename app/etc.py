import sys,os,time

etc = {}
etc['debug'] = False
etc['error'] = False
etc['servs'] = 'AL/1.0.%s' % int(time.time())

etc['root_path'] = sys.path[0]
etc['login_url'] = '/login'
etc['xsrf_cookies'] = True
etc['cookie_secret'] = 'guoqingshan'
etc['template_path'] = os.path.join(etc['root_path'],'app','views','')
etc['database_path'] = os.path.join(etc['root_path'],'var','datas','')