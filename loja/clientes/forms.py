from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, SubmitField, IntegerField, StringField, BooleanField, TextAreaField, validators,DecimalField, PasswordField,ValidationError
from flask_wtf import FlaskForm
from .models import Cadastrar





class CadastroClienteForm(FlaskForm):
    name = StringField('Nome: ')
    username = StringField('Usuario: ',[validators.DataRequired()])
    email = StringField('Email: ',[validators.DataRequired()])
    password = PasswordField('Senha: ',[validators.DataRequired(), validators.EqualTo('confirm',message='AS DUAS SENHA DEVEM SER IGUAIS')])
    confirm = PasswordField('Confirme: ',[validators.DataRequired()])
    country = StringField('Pais: ',[validators.DataRequired()])
    city = StringField('Cidade: ',[validators.DataRequired()])
    contact = StringField('Contato: ',[validators.DataRequired()])
    address = StringField('Endereço: ',[validators.DataRequired()])
    zipcode = StringField('Cep: ',[validators.DataRequired()])


    profile = FileField('Perfil', validators=[FileAllowed(['jpg','png','gif','jpeg'])])
    submit = SubmitField('Cadastrar')

    def validate_user(self, username):
        if Cadastrar.query.filter_by(username=username.data).first():
            raise ValidationError('Este usuario já existe!')

    def validate_email(self, email):
        if Cadastrar.query.filter_by(email=email.data).first():
            raise ValidationError('Este usuario já existe!')


class Clientelogin(FlaskForm):
    email = StringField('Email: ',[validators.DataRequired()])
    password = PasswordField('Senha: ',[validators.DataRequired(),
                                         validators.EqualTo('confirm')])
