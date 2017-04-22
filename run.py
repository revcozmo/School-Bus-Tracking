'''
Import flask 'app' module from BusTrack  __init__.py
'''

from BusTrack import app

app.config.from_object('config')
app.config.from_pyfile('config.py')

'''
This is start up file for project
'''

if __name__=='__main__':
    app.run(host='0.0.0.0')
