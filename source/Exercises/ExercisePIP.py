# Instalar lib com PIP
# install requests
# pip install requests
# install numpy
# pip install numpy
# install pandas
# pip install pandas
# install matplotlib
# pip install matplotlib
# install seaborn
# pip install seaborn
# para desinstalar uma lib
# pip uninstall nome_da_lib
# para listar todas as libs instaladas
# pip list

import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))