from flask import Blueprint, render_template, request
from models.language_model import LanguageModel
from deep_translator import GoogleTranslator


language_controller = Blueprint("language", __name__)


@language_controller.route("/")
def initial():
    languages = LanguageModel.list_dicts()
    text_to_translate = "O que deseja traduzir?"
    translate_from = "pt"
    translate_to = "en"
    translated = "What do you want to translate?"

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )


@language_controller.route("/", methods=["POST"])
def languages_translate():
    languages = LanguageModel.list_dicts()
    text_to_translate = request.form["text-to-translate"]
    translate_from = request.form["translate-from"]
    translate_to = request.form["translate-to"]
    translated = GoogleTranslator(
        source=translate_from, target=translate_to
    ).translate(text_to_translate)

    return render_template(
        "index.html",
        languages=languages,
        text_to_translate=text_to_translate,
        translate_from=translate_from,
        translate_to=translate_to,
        translated=translated,
    )
