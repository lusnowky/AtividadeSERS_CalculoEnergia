# Lista de Aparelhos e os seus gastos em kWh

metodos = [1, 2, 3]

gelad = 55
tv = 15
lamp = 2
chuv = 50
fogao = 60
mqnLava = 15

print("""
==================================================================================================
                    Bem-vindo ao seu cálculo de demanda energética da sua casa
==================================================================================================

Métodos disponíveis para cálculo de gastos:

[ 1 ] Estimativa de gasto mensal baseada em valores aproximados dos gastos mensais dos aparelhos
[ 2 ] Informar gastos individuais dos aparelhos e obter média mensal precisa
[ 3 ] Informar gastos de mêses passados e obter uma média entre eles e mês com maior gasto

""")

metodo = int(input("Insira o método escolhido: "))

if metodo not in metodos:
    print("Método inválido")

while metodo == 1:

    qtdGelad = int(input("Quantas geladeiras tem em sua casa?: "))
    qtdTv = int(input("Quantas TV tem em sua casa?: "))
    qtdLamp = int(input("Quantas lâmpadas tem em sua casa?: "))
    qtdChuv = int(input("Quantos chuveiros tem em sua casa?: "))
    qtdFogao = int(input("Quantos fogões tem em sua casa?: "))
    qtdMqnLava = int(input("Quantas máquinas de lavar tem em sua casa?: "))

    totalEnergia = (gelad * qtdGelad) + (tv * qtdTv) + (lamp * qtdLamp) + (chuv * qtdChuv) + (fogao * qtdFogao) + (
                mqnLava * qtdMqnLava)
    totalItens = qtdGelad + qtdTv + qtdLamp + qtdChuv + qtdFogao + qtdMqnLava

    media = (totalEnergia / totalItens)

    print()

    print(f"""
    ===========================================================
    A média da sua demanda energética é {media:.2f}kWh por mês
    ===========================================================""")

# ---------------------------------------------------




