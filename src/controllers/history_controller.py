from flask import Blueprint, jsonify
from models.history_model import HistoryModel


history_controller = Blueprint("history", __name__)


@history_controller.route("/")
def history():
    history_list = HistoryModel.list_as_json()

    return jsonify(history_list), 200
