from app.app import db
from flask import Blueprint, redirect, render_template, url_for,request


Receita = Blueprint('Receita',__name__)

@Receita.route('/')
@Receita.route('/index')
def index():
    return render_template('index.html')

class receita:
    
    @staticmethod
    def consultaReceita(documento):
        queryDeBuscaReceita = [i for  i in db.engine.execute(f'''
            select distinct pa.nome,r.idReceita,concat(DAY(r.dataReceita),'/',MONTH(r.dataReceita),'/',YEAR(r.dataReceita)),pa.cpf,r.prescricao,m.nome,m.crm
            from possui p
            inner join paciente pa on pa.cpf = p.fk_Paciente_cpf
            inner join receita r on r.idReceita = p.fk_Receita_idReceita
            inner join medico m on m.crm = p.fk_Medico_crm
            where p.fk_Paciente_cpf = '{documento}'
        ''')]
        return queryDeBuscaReceita
    
    @staticmethod
    def consultaReceitaFarm(documento):
        queryDeBuscaReceita = [i for  i in db.engine.execute(f'''
            select distinct pa.nome,r.idReceita,concat(DAY(r.dataReceita),'/',MONTH(r.dataReceita),'/',YEAR(r.dataReceita)),pa.cpf,r.prescricao,m.nome,m.crm
            from possui p
            inner join paciente pa on pa.cpf = p.fk_Paciente_cpf
            inner join receita r on r.idReceita = p.fk_Receita_idReceita
            inner join medico m on m.crm = p.fk_Medico_crm
            where p.fk_Paciente_cpf = '{documento}' and r.statusReceita = 'd'
        ''')]
        return queryDeBuscaReceita
    
    @staticmethod
    def consultaReceitaPac(documento):
        queryDeBuscaReceita = [i for  i in db.engine.execute(f'''
            select distinct pa.nome,r.idReceita,concat(DAY(r.dataReceita),'/',MONTH(r.dataReceita),'/',YEAR(r.dataReceita)),pa.cpf,r.prescricao,m.nome,m.crm
            from possui p
            inner join paciente pa on pa.cpf = p.fk_Paciente_cpf
            inner join receita r on r.idReceita = p.fk_Receita_idReceita
            inner join medico m on m.crm = p.fk_Medico_crm
            where p.fk_Paciente_cpf = '{documento}'
        ''')]
        return queryDeBuscaReceita

    @staticmethod
    def vender(id):
        db.engine.execute(f'''
            update receita
            set statusReceita = 'v'
            where idReceita = '{id}'
        ''')