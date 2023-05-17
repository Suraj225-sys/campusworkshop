"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7s5jhp8u7g2efg77g-a.oregon-postgres.render.com",
        database="todo_qd2o",
        user="root",
        password="AjpDijQmD8PBoEHYKDKRRzx1c4y557Wt")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
