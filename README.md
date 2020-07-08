# Projeto Cadastro de Endereço ultilizando 
Tecnologias Utilizadas: Python Django, Sqlite3 + Javascript + Html5 + Css + Bootstrap 4

### ## Python Django:
Desenvolvimento do back-end, rotas e urls.

### Sqlite3:
Desenvolvimento do banco de dados simples.


	class usuario(models.Model):
	from django.db import models
	
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    number = models.CharField(max_length=9)
    complement = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=8)
    description = models.TextField()
    begin_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.id)

    class meta:
        db_table = 'Address'
### HTML5:
Montagem da páginas.

### CSS3:
Montagem básica do estilo do site.

### JavaScript:
Script de funcionamento do relógio e da transição de temas de acordo com o horário do dia.

### Bootstrap 4
Foi utilizado formularios a  layouts ultilizando a tecnologia.
