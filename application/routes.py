from . import app
from flask import render_template, flash, redirect, url_for, jsonify


@app.route('/test')
def test():
    """ test route """
    print('TEST ROUTE')
    return jsonify({ 'data': 'stuff' })
