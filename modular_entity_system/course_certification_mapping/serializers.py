from rest_framework import serializers
from .models import CourseCertificationMapping


class CourseCertificationMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCertificationMapping
        fields = "__all__"

    def validate(self, data):

        course = data.get("course", getattr(self.instance, "course", None))
        primary = data.get("primary_mapping", getattr(self.instance, "primary_mapping", False))

        if primary:

            qs = CourseCertificationMapping.objects.filter(
                course=course,
                primary_mapping=True
            )

            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise serializers.ValidationError(
                    "This course already has a primary certification mapping."
                )

        return data