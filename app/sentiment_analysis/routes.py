from flask import render_template, redirect, flash, url_for
from app.sentiment_analysis import bp
from flask import current_app
from app.sentiment_analysis.forms import InputStringForm

from .modeling import *
from .modeling.inference import infer_sentiment
import os
import json


@bp.route("/",methods=['GET','POST'])
@bp.route("/index",methods=['GET','POST'])
def index():
    try:
        form = InputStringForm()
        if form.validate_on_submit():
            response = infer_sentiment(form.input_string.data)
            flash(f"Result: {response}")

            return redirect(url_for('sentiment_analysis.index'))
        return render_template('index.html',title='Sentiment Analysis using CNN',form=form)
    except Exception as e:
        current_app.logger.error(e)

