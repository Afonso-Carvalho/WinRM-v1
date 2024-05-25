import winrm


s = winrm.Session('http://aaaaa:5985/wsman', auth=('franca', 'franca'))
r = s.run_cmd('net user afonso')
print(r.status_code)
