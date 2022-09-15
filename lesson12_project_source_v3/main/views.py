from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import search_by_word

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    search_mas = request.args.get('s', '')
    import logging
    logging.info('complete search')
    try:
        posts = search_by_word(search_mas)
    except FileNotFoundError:
        logging.info('file not found')
        return 'file not found'
    except JSONDecodeError:
        return 'try other file format'

    return render_template('post_list.html', query=search_mas, posts=posts)
