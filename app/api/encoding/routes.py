import os
from flask import request, json, jsonify

from .. import api, base_dir
from .base64 import b64encode

json_dir = os.path.join(base_dir, "static", "encoding")


@api.route("/base64", methods=["GET", "POST"])
def base64():
    if request.method == "GET":
        with open(os.path.join(json_dir, "base64.json")) as f:
            return jsonify(json.load(f))
    else:
        req_json = request.get_json()
        ret = {
            "output": b64encode(req_json["input"])
        }
        return jsonify(ret)