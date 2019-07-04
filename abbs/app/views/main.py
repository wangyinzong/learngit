from flask import Blueprint, render_template, request, flash, get_flashed_messages
main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    return 'cangbazi wang666'