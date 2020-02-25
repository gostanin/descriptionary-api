from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
PORT = config('PORT', default=5000, cast=int)

ALLOWED_CORS_ORIGINS = config('ALLOWED_CORS_ORIGINS', default=['*'])
