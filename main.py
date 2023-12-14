import random
import re

print('''
Para rolar os dados use o seguinte formato: MdN+A (OdP+B)
M       = Número de dados (opcional [1-99])
N       = Número de faces do dado
A       = Aditivo (opcional)
OdP+B   = Dados adcionais (opcional)
''')
texto = input('Digite o seu dado: ')

p = re.compile(r'([0-9]?[0-9]?[dD][0-9]+([+-]?[0-9]+)?)')
correspondencias = p.finditer(texto)
verifica = re.search(p, texto)

e = re.compile(r'[a-cA-Ce-zE-Z!@#$%&*()_{}§´`¨^~ºª|<>?/.,:;°]+')
verificaErro = re.search(e, texto)

if verificaErro:
  print('Erro: Dado inválido')
else:
  if verifica:
    for c in correspondencias:  
      g = 0
      print(f"\n{c.group(g)}")
    
      m = re.compile(r'([0-9]?[0-9]?[dD])')
      mstr = c.group(g)
      mstr = str(m.findall(mstr)) 
    
      d = re.compile(r'[dD][0-9]+')
      dado = c.group(g)
      dado = str(d.findall(dado))
    
      a = re.compile(r'[+-][0-9]+')
      aditivo = c.group(g)
      aditivo = str(a.findall(aditivo))
      
      mstr = str(mstr[0:-3])
      mstr = mstr[2:]
    
      dado = str(dado[0:-2])
      dado = dado[2:]
    
      aditivo = str(aditivo[0:-2])
      aditivo = aditivo[2:]
    
      try:
        mstr = int(mstr)
      except:
        mstr = 1
      
      try:
        dado = int(dado)
      except:
        try:
          dado = dado[1:]
          dado = int(dado)
        except:
          dado = int(0)
    
      try:
        aditivo = int(aditivo)
      except:
        aditivo = int(0)
    
      print(f"Nº de dados:   {mstr}")
      print(f"Valor do dado: {dado}")
      print(f"Aditivo:       {aditivo}\n")
    
      for i in range(mstr):
        resultado = random.randint(1, dado)
        resultado = resultado + aditivo
        print(f"Resultado {i+1}:   {resultado}")
      
      g += 1
  else:
    print('''
  Dado inválido, tente usar o seguinte formato: MdN+A (OdP+B)
  M       = Número de dados (opcional [1-99])
  N       = Número de faces do dado
  A       = Aditivo (opcional)
  OdP+B   = Dados adcionais (opcional)
    ''')