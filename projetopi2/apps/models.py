from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user, get_user_model


# Create your models here.


class login(models.Model):
    id = models.AutoField(primary_key=True),
    nome = models.CharField(max_length=255),
    login = models.CharField(max_length=255),
    senha = models.CharField(max_length=15)


#try:
#    con = mysql.connector.conect(host='localhost', database='bdpi2', 
#    user='root', password='1234')
#
#    consulta_sql = "select * from login"
#    cursor = con.cursor()
#    cursor.execute(consulta_sql)
#    linhas = cursor.fetchall()
#    print("Numero total de registror retornados: ", cursor.rowcount)

#    print("\n Mostrando os usuarios cadastrados")
#    for linha in linhas:
#        print("ID", linha[0])
#        print("Nome", linha[1])
#        print("Login", linha[2])
#        print("Senha", linha[3])

#except Error as e:
#    print("Erro ao acessar tabela MySql", e)

#finally:
#    if (con.is_connected()):
#        con.close()
#        cursor.close()
#        print("Conexão ao MySql encerrada")