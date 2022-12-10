import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('mengontil.cfg')
HOST = config['mengontil']['server']
PORT = config['mengontil']['port']

meth = input('Select method (GET, POST, PATCH, PUT, DELETE): ')
head = head = {'Content-Type': 'application/json', 'Authorization': 'Token 76623fe5619557948fdc2190b82198e538760d75'}

if meth == 'get' or meth == 'GET':
  num = input('Masukan ID atau all: ')

  if num != 'all':
    link = 'http://' + HOST + ':' + PORT + '/api/ngaran/' + num
    r = requests.get(link, headers=head)
    data = r.json()

    if data['response'] == 'ok':
      data = data['result']
      print('---------------------------')
      print('ID: ' + str(data['id']))
      print('Nama: ' + data['nama'])
      print('Pekerjaan: ' + data['pekerjaan'])
      print('Kota asal: ' + data['kota'])
      print('---------------------------')
    else:
      print('No data found.')

  else:
    link = 'http://' + HOST + ':' + PORT + '/api/ngaran/'
    r = requests.get(link, headers=head)
    data = r.json()

    print('---------------------------')
    for res in data['result']:
      print('ID: ' + str(res['id']))
      print('Nama: ' + res['nama'])
      print('Pekerjaan: ' + res['pekerjaan'])
      print('Kota asal: ' + res['kota'])
      print('---------------------------')

elif meth == 'post' or meth == 'POST':
  print('---------------------------')
  print('Masukan data baru')
  print('---------------------------')

  link = 'http://' + HOST + ':' + PORT + '/api/ngaran/'
  nama = input('Masukan nama lengkap: ')
  pekerjaan = input('Masukan pekerjaan: ')
  kota = input('Masukan kota: ')

  data = {'nama': nama, 'pekerjaan': pekerjaan, 'kota': kota}
  r = requests.post(link, headers=head, json=data)

  re_r = r.json()
  if re_r['response'] == 'ok':
    print('Data berhasil ditambahkan')
  else:
    print('Data gagal ditambahkan')

elif meth == 'put' or meth == 'PUT':
  num = input('Masukan ID: ')
  link = 'http://' + HOST + ':' + PORT + '/api/ngaran/' + num

  r = requests.get(link, headers=head)
  data = r.json()

  if data['response'] == 'ok':
    data = data['result']
    nama = input('Masukan nama (' + data['nama'] + '): ') or data['nama']
    pekerjaan = input('Masukan nama (' + data['pekerjaan'] + '): ') or data['pekerjaan']
    kota = input('Masukan nama (' + data['kota'] + '): ') or data['kota']

    data = {'nama': nama, 'pekerjaan': pekerjaan, 'kota': kota}
    r = requests.put(link, headers=head, json=data)
    re_r = r.json()

    if re_r['response'] == 'ok':
      print('Data berhasil diedit')
    else:
      print('Data gagal diedit')
  else:
    print('Data tidak ditemukan')

elif meth == 'patch' or meth == 'PATCH':
  num = input('Masukan ID: ')
  link = 'http://' + HOST + ':' + PORT + '/api/ngaran/' + num
  r = requests.get(link, headers=head)
  data = r.json()

  if data['response'] == 'ok':
    data = data['result']
    nama = input('Masukan nama (' + data['nama'] + '): ') or data['nama']
    pekerjaan = input('Masukan nama (' + data['pekerjaan'] + '): ') or data['pekerjaan']
    kota = input('Masukan nama (' + data['kota'] + '): ') or data['kota']

    data = {'nama': nama, 'pekerjaan': pekerjaan, 'kota': kota}
    r = requests.patch(link, headers=head, json=data)
    re_r = r.json()

    if re_r['response'] == 'ok':
      print('Data berhasil diubah')
    else:
      print('Data gagal diubah')
  else:
    print('Data tidak ditemukan')

elif meth == 'delete' or meth == 'DELETE':
  num = input('Masukan ID: ')
  link = 'http://' + HOST + ':' + PORT + '/api/ngaran/' + num

  r = requests.delete(link, headers=head)

  re_r = r.json()
  if re_r['response'] == 'ok':
    print('Data berhasil dihapus')
  else:
    print('Data gagal dihapus')

else:
  print('Please input valid method')
