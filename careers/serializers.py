from rest_framework.serializers import Serializer
from rest_framework import fields

class IllustrationSerializer(Serializer):
    url = fields.URLField()


class JobSerializer(Serializer):
    illustrations = IllustrationSerializer(many=True)

    pk = fields.IntegerField(read_only=True)
    title = fields.CharField()
    description = fields.CharField()
    modified_on = fields.DateField()
    created_on = fields.DateField()
