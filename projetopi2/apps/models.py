from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user, get_user_model
from stdimage.models import StdImageField


# Create your models here.


class Login(models.Model):
    id = models.AutoField(primary_key=True),
    nome = models.CharField(max_length=255),
    login = models.CharField(max_length=255),
    senha = models.CharField(max_length=15)


class LoginPrestador(models.Model):
    profissao = (
        ('Assistencia Tecnica','assistencia tecnica'),
        ('Professor','professor'),
        ('Mecanico', 'mecanico'),
        ('Consultoria','consultoria'),
        ('Tecnologia','tecnologia'),
        ('Eventos','eventos'),
        ('Beleza','beleza'),
        ('Reparos','reparos'),
        ('Saude','saude'),
        ('Domestico','domestico'),
        ('Motociclista','motociclista')
    )
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=16,null=True, blank=True)
    email = models.CharField(max_length=100,null=True, blank=True)
    senha = models.CharField(max_length=15)
    cep = models.CharField(max_length=10)
    numero = models.CharField(max_length=10)
    complemento  = models.CharField(max_length=100,null=True, blank=True)
    profissional= models.CharField(
        max_length=25,
        choices=profissao,
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class imagemPerfil(models.Model):
    id= models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    imagem= StdImageField('Imagem', upload_to='usuario', variations={'thumb': (124, 124)},null=True)


#try:
#    con = mysql.connector.conect(host='localhost', database='bdpi2', 
#   user='root', password='1234')

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