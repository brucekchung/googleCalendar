from application import app

# command line:
# export FLASK_APP=run.py FLASK_DEBUG=true
# flask run
if __name__ == 'run':
    app.run(debug=True)
else:
    raise ValueError('Bug in run.py')
