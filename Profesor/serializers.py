from rest_framework import routers, serializers, viewsets


from Profesor.models import Profesor

from drf_dynamic_fields import DynamicFieldsMixin

class ProfesorSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('id','address','name','apellidoPaterno','apellidoMaterno','telefono','edad','sexo','aniosExperiencia','fechaNacimiento')

