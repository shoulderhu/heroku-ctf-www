from .. import api
from flask import request, jsonify


@api.route("/rot13", methods=["GET", "POST"])
def rot13():
    pass