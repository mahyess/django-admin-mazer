from django import template

register = template.Library()


@register.filter('field_type')
def field_type(field):
    if field.field.widget.__class__.__name__ == 'AdminTextInputWidget':
        return 'text'
    if field.field.widget.__class__.__name__ == 'AdminFileWidget':
        return 'file'
    if field.field.widget.__class__.__name__ == 'AdminIntegerFieldWidget':
        return 'number'
    if field.field.widget.__class__.__name__ == 'AdminTextareaWidget':
        return 'textarea'
    return field.field.widget.__class__.__name__


@register.filter
def add_class(field, class_name):
    if field.field.widget.__class__.__name__ == 'CheckboxInput':
        class_name = class_name.replace("form-control", "form-check-input")
    if not field.errors:
        class_name = class_name.replace("is-invalid", "")

    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })


@register.filter
def check_errors(field, errors):
    print(field.errors)

    return field


@register.filter('datatype')
def datatype(var):
    print(type(var))
    return type(var)
