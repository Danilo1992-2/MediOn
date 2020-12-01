from flask import Blueprint, redirect, render_template, url_for,request,flash
from werkzeug.security import generate_password_hash,check_password_hash
from app.app import db


admin = Blueprint('admin',__name__)

@admin.route("/loginAdmin",methods=['GET','POST'])
def login():
    Erro = None
    if request.method == 'POST':
        try:
            login = request.form['login']
            senha = request.form['senha']
            senhaInBd = [i for i in db.engine.execute(f"select password from adminlogin   where cpf ='{login}'")]
            if senhaInBd[0][0] == senha:
                return redirect('/consultarDados')
            else:
                Erro = "Verifique suas credenciais"
                return render_template('loginAdmin.html',Erro =Erro)
        except:
            pass
    return render_template('loginAdmin.html')

@admin.route('/consultarDados',methods=['GET','POST'])
def opcoes():
    #try:
        if request.method == 'POST':
            cpf = request.form['cpf']
            opcao = request.form['user']
            if opcao != 'farmacia':
                dados = [i for i in  db.engine.execute(f'''
                    select * 
                    from {opcao}
                    where cpf = '{cpf}'
                ''')]
            else:
                dados = [i for i in  db.engine.execute(f'''
                    select * 
                    from {opcao}
                    where cnpj = '{cpf}'
                ''')]
            return render_template('editarDados.html',op =opcao, dados =dados[0])
    #except:
    #    pass
        return render_template('selecionarOpcaoEdicao.html')

@admin.route('/atualizar',methods=['GET','POST'])
def AtualizarDados():
    if request.method == 'POST':
        tabela = request.form['opcao']
        if tabela == 'paciente':
            cpf = request.form['cpfAtual']
            nome = request.form['nome']
            senha = request.form['senha']
            telefone = request.form['telefone']
            email = request.form['email']

            if len(nome) > 0 and nome != None:
                db.engine.execute(f'''
                update paciente
                set nome = '{nome}'
                where cpf = '{cpf}'
                ''')

            elif len(email) > 0 and email != None:
                db.engine.execute(f'''
                update paciente
                set email = '{email}'
                where cpf = '{cpf}'
                ''')

            elif len(senha) > 0 and senha != None:
                db.engine.execute(f'''
                update paciente
                set senha = '{generate_password_hash(senha)}'
                where cpf = '{cpf}'
                ''')

            elif len(telefone) > 0 and telefone != None:
                    db.engine.execute(f'''
                update paciente
                set telefone = '{telefone}'
                where cpf = {cpf}''')

            else:
                return redirect('/consultarDados')
                
        elif tabela == 'medico':
            cpf = request.form['cpfAtual']
            nome = request.form['nome']
            senha = request.form['senha']
            telefone = request.form['telefone']
            
            if len(nome) > 0 and nome != None:
                db.engine.execute(f'''
                    update medico
                    set nome = '{nome}'
                    where cpf= '{cpf}'
                ''')
            
            elif len(senha) > 0 and senha != None:
                db.engine.execute(f'''
                    update medico
                    set senha = '{generate_password_hash(senha)}'
                    where cpf= '{cpf}'
                ''')
            
            elif len(telefone) > 0 and telefone != None:
                db.engine.execute(f'''
                    update medico
                    set telefone = '{telefone}'
                    where cpf= '{cpf}'
                ''')
            else:
                return redirect('/consultarDados')    
        

        elif tabela == 'farmacia':
            cnpjAtual = request.form['cnpjAtual']
            razaoSocial= request.form['razao']
            cnpj =request.form['cnpj']
            senha = request.form['senha']
            telefone = request.form['telefone']
            
            if len(razaoSocial) > 0 and razaoSocial != None:
                db.engine.execute(f'''
                    update farmacia
                    set nomeFantasia = '{razaoSocial}'
                    where cnpj = '{cnpjAtual}'
                ''')
            
            elif len(cnpj) > 0 and cnpj != None:
                db.engine.execute(f'''
                    update farmacia
                    set cnpj = '{cnpj}'
                    where cnpj = '{cnpjAtual}'
                ''')
            
            elif len(senha) > 0 and senha != None:
                    db.engine.execute(f'''
                    update farmacia
                    set senha = '{generate_password_hash(senha)}'
                    where cnpj = '{cnpjAtual}'
                ''')
            
            elif len(telefone) > 0 and telefone != None:
                db.engine.execute(f'''
                    update farmacia
                    set telefone = '{telefone}'
                    where cnpj = '{cnpjAtual}'
                ''')
            else:
                return redirect('/consultarDados')
        else:
            return redirect('/consultarDados')


    return redirect('/consultarDados')