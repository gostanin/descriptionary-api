import logging

from flask import jsonify, abort, make_response


logger = logging.getLogger(__name__)


def throw_http_error(message, code=500, exc_info=False):
    logger.error(message, exc_info=exc_info)
    abort(make_response(jsonify(message=message), code))
