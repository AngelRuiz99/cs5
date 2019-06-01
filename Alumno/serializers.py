from rest_framework import routers, serializers, viewsets

from Alumno.models import Alumno

from drf_dynamic_fields import DynamicFieldsMixin

class AlumnoSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ('id','id_profesor','address','name','apellidoPaterno','apellidoMaterno','matricula','materia','telefono','edad','sexo','fechaNacimiento')

