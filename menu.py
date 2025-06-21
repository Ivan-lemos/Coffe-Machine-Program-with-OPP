class MenuItem:
    """Representa um item individual do menu da máquina de café.

    Atributos:
        name (str): O nome da bebida.
        cost (float): O custo da bebida.
        ingredients (dict): Um dicionário contendo os ingredientes e suas quantidades necessárias.
    """
    def __init__(self, name: str, water: int, milk: int, coffee: int, cost: float):
        """Inicializa um novo item de menu.

        Args:
            name: O nome da bebida.
            water: A quantidade de água necessária (em ml).
            milk: A quantidade de leite necessária (em ml).
            coffee: A quantidade de café necessária (em gramas).
            cost: O custo da bebida (em USD).
        """
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Modela o menu de bebidas disponíveis na máquina de café.

    Atributos:
        menu (list[MenuItem]): Uma lista de objetos MenuItem representando as bebidas disponíveis.
    """
    def __init__(self):
        """Inicializa o Menu com as bebidas predefinidas.
        """
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self) -> str:
        """Retorna uma string formatada com os nomes de todos os itens do menu disponíveis.

        Returns:
            Uma string contendo os nomes das bebidas separados por uma barra.
        """
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options.strip("/") # Remove a barra extra no final

    def find_drink(self, order_name: str) -> MenuItem | None:
        """Procura um item do menu pelo nome.

        Args:
            order_name: O nome da bebida a ser encontrada.

        Returns:
            O objeto MenuItem se encontrado, caso contrário, None.
        """
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Desculpe, esse item não está disponível.")
        return None


