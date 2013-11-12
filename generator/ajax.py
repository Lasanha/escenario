from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from models import EscImg


@dajaxice_register
def vote_escimg(request, id):
    escimg = EscImg.objects.get(id=int(id))
    votos = escimg.gostei()
    escimg.save()
    return simplejson.dumps({'message': 'Voto computado! Novo total: %d' % votos})
