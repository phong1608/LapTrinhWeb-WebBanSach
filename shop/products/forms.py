from flask_wtf.file import FileAllowed, FileRequired, FileField
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators


class Add_Product(Form):
    name = StringField('Name', [validators.DataRequired()])
    price = IntegerField('Price', [validators.DataRequired()])
    stock = IntegerField("Stock", [validators.DataRequired()])
    discount = IntegerField("Discount", default=0)
    description = TextAreaField("Description", [validators.DataRequired()])
    image_1 = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])

