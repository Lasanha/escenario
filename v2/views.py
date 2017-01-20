from ipware.ip import get_ip
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from generator.models import EscImg
from v2.serializer import EscenarioSerializer, CreateEscenarioSerializer

VALID_ORDER_BY_FIELDS = {
    '-criado_em',
    'criado_em'
}

DEFAULT_ORDER_BY_FIELDS = '-criado_em'


class EscenarioViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = EscenarioSerializer

    def get_queryset(self):
        order_by_field = self.request.GET.get('order_by',
                                              DEFAULT_ORDER_BY_FIELDS)
        if order_by_field not in VALID_ORDER_BY_FIELDS:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

        return EscImg.objects.order_by(order_by_field)

    def create(self, request, *args, **kwargs):
        autonumber = request.data.pop('autonumber', False)
        form = CreateEscenarioSerializer(data=request.data)
        if form.is_valid():
            form.validated_data['origem'] = get_ip(request)
            escenario = form.save()
            created = escenario.generate_image(autonumber)
            return Response({'id': created.id}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['post'])
    def like(self, request, *args, **kwargs):
        escenario = self.get_object()
        new_count = escenario.like()
        escenario.save()
        return Response({'new_count': new_count})
