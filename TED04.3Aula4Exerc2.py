num_macas_compradas = int(float(input("Entre o numero de maças compradas: ")))
if num_macas_compradas >= 12:
    custo_total = num_macas_compradas * 1.00
    print("custo_total da compra de maças é R$: ", custo_total)
else:
    custo_total = num_macas_compradas * 1.20
    print("custo_total da compra de maças é R$: ", custo_total)