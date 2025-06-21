class MoneyMachine:
    """Gerencia o processamento de dinheiro para a máquina de café.

    Esta classe é responsável por receber moedas, calcular o total, verificar
    se o pagamento é suficiente e gerenciar o lucro da máquina.
    """

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        """Inicializa a MoneyMachine com lucro zero e dinheiro recebido zero."""
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Imprime o lucro atual da máquina.
        """
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self) -> float:
        """Solicita ao usuário a inserção de moedas e calcula o total recebido.

        Este método interage com o usuário para coletar a quantidade de cada tipo de moeda
        e retorna o valor total em dinheiro inserido.

        Returns:
            float: O valor total em dinheiro inserido pelo usuário.
        """
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            # Solicita a quantidade de cada moeda e adiciona ao total
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost: float) -> bool:
        """Verifica se o pagamento é suficiente e processa a transação.

        Se o dinheiro recebido for suficiente, calcula o troco, adiciona o custo ao lucro
        e redefine o dinheiro recebido. Caso contrário, informa que o dinheiro é insuficiente.

        Args:
            cost (float): O custo do item a ser pago.

        Returns:
            bool: True se o pagamento for aceito, False se for insuficiente.
        """
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False


