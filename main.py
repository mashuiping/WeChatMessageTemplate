# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
import subprocess
urls = (
    '/wx', 'Handle',
)

if __name__ == '__main__':
    subprocess.Popen("python update_access_token.py", shell = True)
    app = web.application(urls, globals())
    app.run()