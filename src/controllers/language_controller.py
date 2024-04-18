from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from models.history_model import HistoryModel
from deep_translator import GoogleTranslator

language_controller = Blueprint("language", __name__)


def get_default_values():
    return {
        "text_to_translate": "O que deseja traduzir?",
        "translate_from": "pt",
        "translate_to": "en",
        "translated": "What do you want to translate?",
    }


@language_controller.route("/", methods=["GET", "POST"])
def translate():
    languages = LanguageModel.list_dicts()
    default_values = get_default_values()

    if request.method == "POST":
        text_to_translate = request.form["text-to-translate"]
        translate_from = request.form["translate-from"]
        translate_to = request.form["translate-to"]
        translated = GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(text_to_translate)

        data = {
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to,
        }

    else:
        text_to_translate = default_values["text_to_translate"]
        translate_from = default_values["translate_from"]
        translate_to = default_values["translate_to"]
        translated = default_values["translated"]

        data = {
            "text_to_translate": text_to_translate,
            "translate_from": translate_from,
            "translate_to": translate_to,
        }

    HistoryModel(data).save()

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@language_controller.route("/reverse", methods=["GET", "POST"])
def reverse():
    languages = LanguageModel.list_dicts()

    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]

    reversed_translation = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    data = {
        "text_to_translate": text_to_translate,
        "translate_from": translate_from,
        "translate_to": translate_to,
    }

    HistoryModel(data).save()

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=reversed_translation,
        translate_from=translate_to,
        translate_to=translate_from,
        translated=text_to_translate,
    )
