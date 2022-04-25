from wtforms import Form, BooleanField, StringField, PasswordField, validators



    # """CLASS para VALIDAR O REGISTRO DE USUSARIO da loja"""

class RegistrationForm(Form):
    name = StringField("Nome", [validators.length(min=4, max=25)])
    username = StringField("usuario", [validators.length(min=4, max=25)])
    email = StringField("Email",[validators.length(min=6, max=35)])
    password = PasswordField("Digite Sua Senha", [validators.DataRequired(), validators.EqualTo("confirm", message="Sua senha não coferem")])
    confirm = PasswordField("Repeta a senha")


    # """CLASS para VALIDAR O LOGIN DE USUSARIO da loja"""

class LoginFormulario(Form):
    email = StringField('Email:', [validators.length(min=6, max=35)])
    password = PasswordField('Senha:', [validators.DataRequired()])
