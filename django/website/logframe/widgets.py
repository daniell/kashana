from django.forms import widgets
from django.utils.encoding import force_text
from django.utils.html import format_html
from django.utils.safestring import mark_safe




class ColorSelect(widgets.RadioSelect):
    option_template_name = 'logframe/widgets/color_option.html'
