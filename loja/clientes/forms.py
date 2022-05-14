from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, SubmitField, IntegerField, StringField, BooleanField, TextAreaField, validators,DecimalField, PasswordField






class CadastroClienteForm(Form):
    name = StringField('Nome: ')
    username = StringField('Usuario: ',[validators.DataRequired()])
    email = StringField('Email: ',[validators.DataRequired()])
    passoword = PasswordField('Senha: ',[validators.DataRequired(), validators.EqualTo('confirm',message='AS DUAS SENHA DEVEM SER IGUAIS')])
    confirm = PasswordField('Confirme: ',[validators.DataRequired()])
    country = StringField('Pais: ',[validators.DataRequired()])
    state = StringField('Estado: ',[validators.DataRequired()])
    city = StringField('Cidade: ',[validators.DataRequired()])
    contact = StringField('Contato: ',[validators.DataRequired()])
    address = StringField('Endereço: ',[validators.DataRequired()])
    zipcode = StringField('Cep: ',[validators.DataRequired()])
    profile = FileField('Perfil', validators=[FileAllowed(['jpg','png','gif','jpeg'])])

    submit = SubmitField('Cadastrar')