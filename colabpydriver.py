#Instalando o PyDrive wrapper & importando bibliotecas.
!pip install -U -q PyDrive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Autenticação e criação do PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# Cópia/Download do arquivo
fid = drive.ListFile({'q':"title='AliciaLC.ipynb'"}).GetList()[0]['id']
f = drive.CreateFile({'id': fid})
f.GetContentFile('AliciaLC.ipynb')

#esse passo é para acrescentar a AliciaLC no path do Colab. path: /content
