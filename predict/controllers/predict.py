from flask import request, Blueprint, jsonify

from predict.controllers.utils import throw_http_error
from model.model import model_predict


predict = Blueprint('predict', __name__)


@predict.route('/', methods=['GET'])
def predict_word():
    if not request.args:
        throw_http_error(message='No arguments have been passed', code=400)
    if not request.args.get('description'):
        throw_http_error(message='Empty description has been passed', code=400)

    try:
        response = jsonify(data=model_predict(request.args.get('description'), request.args.get('top')))
    except Exception as e:
        throw_http_error(message=f'Unexcpected error occured during the execution of the model {e}')

    return response 
