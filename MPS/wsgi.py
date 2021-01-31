
from whitenoise.django import DjangoWhiteNoise
application = get_wsgi_application()
application = DjangoWhiteNoise(application)
