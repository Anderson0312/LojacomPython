from flask import redirect, render_template, url_for, flash, request, session, current_app
from flask_bcrypt import Bcrypt
from loja import db, app, photos, bcrypt, login_manager
from .forms import CadastroClienteForm, ClienteloginForm
import secrets, os
from .models import Cadastrar, ClientePedido
from flask_login import login_required, current_user, login_user, logout_user 

@app.route("/cliente/cadastrar", methods=['GET', 'POST'])
def cadastrar_clientes():
    form = CadastroClienteForm(request.form)
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        cadatrar = Cadastrar(name=form.name.data, username=form.username.data, email=form.email.data,
                             password=hash_password, country=form.country.data, city=form.city.data, contact=form.contact.data, address=form.address.data,
                             zipcode=form.zipcode.data)
        db.session.add(cadatrar)
        flash(f'Obrigado {form.name.data} por cadastrar','success')
        db.session.commit()
        return redirect(url_for('clienteLogin'))
    return render_template('cliente/cliente.html', form=form)


@app.route("/cliente/login", methods=['GET', 'POST'])
def clienteLogin():
    form = ClienteloginForm(request.form)
    if request.method == "POST" and form.validate():
        user = Cadastrar.query.filter_by(email=form.email.data).first()
        print(user)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user) 
            flash(f'Você está logado','success')
            next = request.args.get('next')
            return redirect(next or url_for('home'))
        flash('Senha ou email incorretas','danger')
        return redirect(url_for('clienteLogin'))  
 
    return render_template('cliente/login.html', form=form)


@app.route("/cliente/logout")
def cliente_logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/pedido_order")
@login_required
def pedido_order():
    if current_user.is_authenticated:
        cliente_id = current_user.id
        notafiscal = secrets.token_hex(5)
        try:
            p_order = ClientePedido(notafiscal=notafiscal, cliente_id=cliente_id, pedido=session['LojainCarrinho'])
            db.session.add(p_order)
            db.session.commit()
            session.pop('LojainCarrinho')
            flash(f'Seu pedido foi salvo com sucesso','success')
            return redirect(url_for('home'))
        except Exception as e:
            print(e)
            flash(f'Não foi possivel processar seu pedido','danger')
            return redirect(url_for('getCart'))



@app.route("/pedidos/<notafiscal>")
@login_required
def pedidos(notafiscal):
    if current_user.is_authenticated:
        gTotal = 0
        subTotal = 0
        
        cliente_id = current_user.id
        cliente = Cadastrar.query.filter_by(id=cliente_id).first()
        pedidos = ClientePedido.query.filter_by(cliente_id=cliente_id, notafiscal=notafiscal).order_by(ClientePedido.id.desc()).first()
        for _key, produto in pedidos.pedido.items():
            disconto = (produto['discount']/100)  * float(produto['price'])
            subTotal += float(produto['price']) * int(produto['quantidade'])
            subTotal -= disconto
            imposto = ('%.2f' % (.06* float(subTotal)))  
            gTotal = float('%.2f' % (1.06 * subTotal))
    else:
        return redirect(url_for('clienteLogin'))
    return render_template('cliente/pedidos.html', notafiscal=notafiscal, imposto=imposto, subTotal=subTotal,gTotal=gTotal,cliente=cliente, pedidos=pedidos)