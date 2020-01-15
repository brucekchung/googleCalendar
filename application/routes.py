from __future__ import print_function
from . import app
from flask import jsonify, render_template
from .controllers import GoogleCalendar


@app.route('/')
def view():
    """ Render view """
    return render_template('layout.html') 


@app.route('/events')
def events():
    """ events from Calendar api """
    controller = GoogleCalendar()
    events = controller.get_events()

    if not events:
        return jsonify({ 'data': 'no events' })

    return jsonify({ 'data': events })


@app.route('/calendar-list')
def calendar_list():
    """ calendars from CalendarList api """
    controller = GoogleCalendar()
    calendar_list = controller.get_calendar_list()

    if not calendar_list:
        return jsonify({ 'data': 'no list' })

    return jsonify({ 'data': calendar_list })
