from __future__ import print_function
from . import app
from flask import jsonify
from .controllers import GoogleCalendar


@app.route('/')
@app.route('/test')
def test():
    """ test route """
    return jsonify({ 'data': 'test route' })


@app.route('/events')
def events():
    controller = GoogleCalendar()
    events = controller.get_events()

    if not events:
        return jsonify({ 'data': 'no events' })

    return jsonify({ 'data': events })


# result = service.calendarList().list().execute()
