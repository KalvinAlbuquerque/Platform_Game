""" from autoplayer import AutoPlayer

boneco = AutoPlayer()

boneco.andar_direita()
boneco.andar_direita()

print('ANTES DO IF')
if boneco.tem_bloco_na_frente():
    boneco.pular_direita()

print(boneco.listaMovimentos)
 """