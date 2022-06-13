import pyodbc

#Functions return conection

def retornar_conexao_sql():
    server = "ip-server ,1433"
    database = "Template"
    username = "sa"
    password = "sa123"
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    #string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    return pyodbc.connect(string_conexao)


conexao = retornar_conexao_sql()
cursor = conexao.cursor()

