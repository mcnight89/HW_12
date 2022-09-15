import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import add_post
from loader.utils import save_picture

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def post_page():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return "not found picture or content "

    if picture.filename.split('.')[-1] not in ['jpeg', 'png', 'jpg']:
        logging.info("upload file not picture")
        return 'wrong filename'

    try:
        picture_path = '/' + save_picture(picture)
    except FileNotFoundError:
        return "file not found"
    except JSONDecodeError:
        return 'try other file format'
    post = add_post({'pic': picture_path, 'content': content})

    return render_template('post_uploaded.html', post=post)
