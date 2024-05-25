import winrm

usuarios = [
    {"usuario": "user1", "senha": "senha1"},
    {"usuario": "user2", "senha": "senha2"}
]

hosts= [
    {'host': 'aaa', "usuario_auth": "atacama", "senha_auth": "atacama"},
    {'host': 'aaaaa', "usuario_auth": "franca", "senha_auth": "franca"}
]

for host in hosts:
    host_auth = host["host"]
    nome_auth = host["usuario_auth"]
    senha_auth = host["senha_auth"]

    try:
        print(f"Iniciando conexão com: {nome_auth}")
        sessao = winrm.Session(f'http://{host_auth}/wsman', auth=(nome_auth, senha_auth))
    
        for usuario in usuarios:
            nome_usuario = usuario["usuario"]
            senha_usuario = usuario["senha"]
            check_usuario = sessao.run_cmd(f'net user {nome_usuario}')
            if check_usuario.status_code == 2:
                comando1 = sessao.run_cmd(f'net user {nome_usuario} {senha_usuario}', ['/add'])
                comando2 = sessao.run_cmd(f'net localgroup Administradores {nome_usuario}', ['/add'])
                print(comando1.std_out)
                print(comando2.std_out)
            else:
                print(f'O usuário {nome_usuario} já existe, pulando para o proximo....')

    except Exception as e:
        print(f"Ocorreu um erro inesperado ao tentar conectar ao host {host_auth}: {e}")
