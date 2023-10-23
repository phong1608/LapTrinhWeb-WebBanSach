from flask import Flask, flash
from flask import render_template, session, request, redirect, url_for
from __init__ import db, bcrypt, app


@app.route('/admin')
def admin():
    return 'Admin Page'



