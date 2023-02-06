from django.forms.widgets import Select

import django_filters

from .data import LANGUAGE_CHOICES_FILTER, OPENTAGS_CHOICES
from .models import Resource


SELECT_CSS_CLASS = "px-3 py-2 rounded-lg w-full text-black bg-white"


class CommonResourceFilter(django_filters.FilterSet):
    language = django_filters.ChoiceFilter(
        field_name="form_language",
        choices=LANGUAGE_CHOICES_FILTER,
        label="Language",
        widget=Select(attrs={"class": SELECT_CSS_CLASS}),
    )
    year = django_filters.ModelChoiceFilter(
        queryset=Resource.objects.values_list("year", flat=True)
        .distinct("year")
        .order_by("-year"),
        distinct=True,
        widget=Select(attrs={"class": SELECT_CSS_CLASS}),
    )


class AssetFilter(CommonResourceFilter):
    opentags = django_filters.ChoiceFilter(
        field_name="opentags_csv",
        choices=OPENTAGS_CHOICES,
        lookup_expr="contains",
        label="Open Tags",
        widget=Select(attrs={"class": SELECT_CSS_CLASS}),
    )

    class Meta:
        title = Resource
        fields = [
            "form_language",
            "opentags_csv",
            "year",
        ]


class EventFilter(CommonResourceFilter):
    class Meta:
        title = Resource
        fields = [
            "form_language",
            "year",
        ]
