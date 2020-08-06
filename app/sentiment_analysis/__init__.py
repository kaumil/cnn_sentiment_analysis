from flask import Blueprint

bp = Blueprint("sentiment_analysis",__name__,template_folder="templates")

from app.sentiment_analysis import routes