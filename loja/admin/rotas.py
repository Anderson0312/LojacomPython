from flask import render_template, session, request, url_for, redirect, flash

from loja import app, db, bcrypt
from loja.produtos.models import Addproduto, Marca, Categoria

from .formulario import RegistrationForm, LoginFormulario
from .models import User

import os



    # """Função para ENTRAR Na parte ADMIN da loja"""

@app.route("/admin")
def admin():
    if 'email' not in session:
        flash('Favor fazer seu login no sistema primeiro', 'danger')
        return redirect(url_for('login'))
    produtos = Addproduto.query.all()
    return render_template('admin/index.html', title="Pagina ADM", produtos=produtos)


    # """Função para ENTRAR Na parte MARCAS da loja"""

@app.route("/marcas")
def marcas():
    if 'email' not in session:
        flash('Favor fazer seu login no sistema primeiro', 'danger')
        return redirect(url_for('login'))
    marcas = Marca.query.order_by(Marca.id.desc()).all()
    return render_template('admin/marca.html', title="Pagina Fabricantes", marcas=marcas)


    # """Função para ENTRAR Na parte CATEGORIAS da loja"""

@app.route("/categorias")
def categorias():
    if 'email' not in session:
        flash('Favor fazer seu login no sistema primeiro', 'danger')
        return redirect(url_for('login'))
    categorias = Categoria.query.order_by(Categoria.id.desc()).all()
    return render_template('admin/marca.html', title="Pagina Categorias", categorias=categorias)


    # """Função para ENTRAR Na parte REGISTRAR da loja E CRIAR o REGISTRO DE CONTAS"""

@app.route("/registrar", methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Obrigado {form.name.data} pelo Registro', 'success')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title='Registrar user')


    # """Função para ENTRAR Na parte de LOGIN da loja e efetuar o LOGIN"""

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginFormulario(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            flash(f'Olá {form.email.data} Você está logado', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Não foi possivel entrar.', 'danger')
    return render_template('admin/login.html', form=form, title="Pagina Login")