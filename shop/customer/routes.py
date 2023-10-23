from flask import render_template, redirect, url_for, flash, request
from __init__ import db, app, photos
from flask_login import login_required,current_user,logout_user,login_user


