from rest_framework import serializers
from .models import VendorProductMapping


class VendorProductMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorProductMapping
        fields = "__all__"

    def validate(self, data):

        vendor = data.get("vendor", getattr(self.instance, "vendor", None))
        primary = data.get("primary_mapping", getattr(self.instance, "primary_mapping", False))

        if primary:

            qs = VendorProductMapping.objects.filter(
                vendor=vendor,
                primary_mapping=True
            )

            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise serializers.ValidationError(
                    "This vendor already has a primary product mapping."
                )

        return data