from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class ImageSelectWidget(forms.widgets.Widget):
    template_name = "survey/forms/image_select.html"

    class Media:
        js = (
            "http://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.min.js",
            "http://maps.googleapis.com/maps/api/js?sensor=false",
            "js/survey.js",
        )

    def render(self, name, value, *args, **kwargs):
        choices = []
        for index, choice in enumerate(self.choices):
            if choice[0] != "":
                value, img_src = choice[0].split(":", 1)
                choices.append({"img_src": img_src, "value": value, "full_value": choice[0], "index": index})
        context = {"name": name, "choices": choices}
        html = render_to_string(self.template_name, context)
        return html


class RichLabelMixin:
    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        option["label"] = mark_safe(option["label"])
        return option

# Radio
class RichLabelRadioSelect(RichLabelMixin, forms.RadioSelect):
    pass

# Select
class RichLabelSelect(RichLabelMixin, forms.Select):
    pass

# Select Multiple
class RichLabelCheckboxSelectMultiple(RichLabelMixin, forms.CheckboxSelectMultiple):
    pass
