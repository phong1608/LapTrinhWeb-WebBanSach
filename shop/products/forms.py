from flask_wtf.file import FileAllowed, FileRequired, FileField, DataRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators, SubmitField


class Add_Product(Form):
    name = StringField('Tên sách', [validators.DataRequired()])
    price = IntegerField('Giá', [validators.DataRequired()])
    stock = IntegerField("Số lượng", [validators.DataRequired()])
    author = StringField('Tác giả', [validators.DataRequired()])
    discount = IntegerField("Khuyến mãi", default=0)
    description = TextAreaField("Mô tả", [validators.DataRequired()])
    image_1 = FileField('Hình ảnh', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'])])


class SearchForm(Form):
    search = StringField('search', [DataRequired()])
    submit = SubmitField('Search',
                         render_kw={'class': 'btn btn-success btn-block'})
