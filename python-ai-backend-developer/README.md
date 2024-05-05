<img src="https://hermes.dio.me/lab_projects/badges/04769934-e77a-4b20-a779-1e6f7a7ab1c8.png" alt="Trabalhando com Visão Computacional" width="200">

---
# Sistema Bancário

Este é um programa simples em Python para controle de sistema bancario. Ele permite que o usuário deposite e saque valores, visualize o extrato das operações realizadas e encerre a sessão quando desejar.

## Funcionalidades

O programa oferece as seguintes funcionalidades:

- **Depositar (d)**: Permite ao usuário depositar um valor na sua conta bancária.
- **Sacar (s)**: Permite ao usuário sacar um valor da sua conta bancária, respeitando o saldo disponível e um limite diário de saques.
- **Extrato (e)**: Permite ao usuário visualizar o extrato das operações realizadas, incluindo depósitos e saques, juntamente com o saldo atual e o número de saques realizados no dia.
- **Sair (q)**: Encerra a sessão do usuário e fecha o programa.

## Como usar

1. Execute o programa em um ambiente Python.
2. Use o menu interativo para selecionar a operação desejada.
3. Siga as instruções para realizar depósitos, saques ou visualizar o extrato.
4. Encerre a sessão quando desejar selecionando a opção "Sair".

## Regras e Validações

- O programa valida os valores inseridos pelo usuário, garantindo que sejam números válidos e positivos.
- Para saques, o programa verifica se o valor não excede o saldo disponível na conta bancária.
- Além disso, há um limite diário de saques, definido como 3 saques por dia, e um limite de R$ 500,00 por saque.
- O programa exibe mensagens de erro adequadas em caso de operações inválidas ou falhas.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

