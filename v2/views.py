from ipware.ip import get_ip
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from generator.models import EscImg, MicroblogPost
from v2.serializer import EscenarioSerializer, CreateEscenarioSerializer, \
    MicroblogSerializer

VALID_ORDER_BY_FIELDS = {
    '-criado_em',
    'criado_em',
    '-votos',
    'votos'
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
        data_copy = request.data.copy()
        auto_number = data_copy.pop('autonumber', [''])[0] == 'true'
        form = CreateEscenarioSerializer(data=data_copy)
        if form.is_valid():
            form.validated_data['origem'] = get_ip(request)
            escenario = form.save()
            created = escenario.generate_image(auto_number)
            return Response(
                EscenarioSerializer(created).data,
                status=status.HTTP_201_CREATED
            )
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['post'])
    def like(self, request, *args, **kwargs):
        escenario = self.get_object()
        new_count = escenario.like()
        escenario.save()
        return Response({'new_count': new_count})


class MicroblogViewSet(mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = MicroblogSerializer

    def get_queryset(self):
        return MicroblogPost.objects.order_by('-fixed', '-created_at')
