from flask import Blueprint, jsonify
from models.history_model import HistoryModel


history_controller = Blueprint("history", __name__)


@history_controller.route("/", methods=["GET"])
def history():
    history_list = HistoryModel.list_as_json()

    test = jsonify(history_list)

    print("PRINTTTT::::::", test)

    return jsonify(history_list), 200
