import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    json_data = json.loads(HistoryModel.list_as_json())

    for item in json_data:
        assert "text_to_translate" in item
        assert "translate_from" in item
        assert "translate_to" in item
