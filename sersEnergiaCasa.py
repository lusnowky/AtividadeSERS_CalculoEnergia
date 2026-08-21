# Lista de Aparelhos e seu gastos em kWh

gelad = 55
tv = 15
lamp = 2
chuv = 50
fogao = 60
mqnLava = 15

# ---------------------------------------------------

print("""
===========================================================
Bem-vindo ao seu cálculo de demanda energética da sua casa
===========================================================""")

qtdGelad = int(input("Quantas geladeiras tem em sua casa?: "))
qtdTv = int(input("Quantas TV tem em sua casa?: "))
qtdLamp = int(input("Quantas lâmpadas tem em sua casa?: "))
qtdChuv = int(input("Quantos chuveiros tem em sua casa?: "))
qtdFogao = int(input("Quantos fogões tem em sua casa?: "))
qtdMqnLava = int(input("Quantas máquinas de lavar tem em sua casa?: "))

totalEnergia = (gelad * qtdGelad) + (tv * qtdTv) + (lamp * qtdLamp) + (chuv * qtdChuv) + (fogao * qtdFogao) + (mqnLava * qtdMqnLava)
totalItens = qtdGelad + qtdTv + qtdLamp + qtdChuv + qtdFogao + qtdMqnLava

media = (totalEnergia / totalItens)

print()

print(f"""
===========================================================
A média da sua demanda energética é {media:.2f}kWh por mês
===========================================================""")
