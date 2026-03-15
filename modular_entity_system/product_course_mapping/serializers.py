from rest_framework import serializers
from .models import ProductCourseMapping


class ProductCourseMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCourseMapping
        fields = "__all__"

    def validate(self, data):

        product = data.get("product", getattr(self.instance, "product", None))
        primary = data.get("primary_mapping", getattr(self.instance, "primary_mapping", False))

        if primary:

            qs = ProductCourseMapping.objects.filter(
                product=product,
                primary_mapping=True
            )

            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise serializers.ValidationError(
                    "This product already has a primary course mapping."
                )

        return data