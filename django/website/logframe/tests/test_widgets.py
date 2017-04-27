from ..widgets import ColorSelect
import re


def test_color_choice_input_widget_not_escaped_when_rendering_color_select():
    color_choices = (('blue', 'Blue',), ('green', 'Green'))
    color_select = ColorSelect(choices=color_choices)
    output = color_select.render('color', None)
    escaped_html = re.search('(&lt;|&gt;|&quot;)', output)
    assert escaped_html is None
