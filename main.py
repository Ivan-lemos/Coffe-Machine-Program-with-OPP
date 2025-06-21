from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Inicializa as instâncias das classes
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# Loop principal da máquina de café
while is_on:
    # Obtém as opções de bebidas disponíveis no menu
    options = menu.get_items()
    # Solicita a escolha do usuário
    choice = input(f"What would you like? ({options}): ")

    # Verifica a escolha do usuário
    if choice == "off":
        # Desliga a máquina se a escolha for "off"
        is_on = False
    elif choice == "report":
        # Imprime os relatórios de recursos e dinheiro se a escolha for "report"
        coffee_maker.report()
        money_machine.report()
    else:
        # Encontra a bebida escolhida no menu
        drink = menu.find_drink(choice)

        # Se a bebida for encontrada e houver recursos suficientes e o pagamento for bem-sucedido
        if drink and coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Prepara o café
            coffee_maker.make_coffee(drink)


