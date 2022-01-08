num = int(input('digite um número inteiro :'))
print('''escolha uma das bases para a conversão 
1 converter para binarrio 
2 converter para octal
3 converter para hexadecimal''')
opcao = int(input('sua opção :'))
if opcao == 1:
    print(f'o valor em binario é {num,bin(num)[2:]}')
elif opcao == 2:
    print(f'o valor em octal é {num,oct(num)[2:]}')
elif opcao == 3:
    print(f'o valor em hexadecimal é {num,hex(num)[2:]}')
else:
    print('porfavo coloque um número valido')