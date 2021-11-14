from has_cards import HasCards


class Player(HasCards):
    def __init__(self, name, cards=False):
        if not cards:
            cards = []
        super().__init__(cards)

        self.name = name

    def choose_move(self):
        try:
            return int(input(f'Choose {self.name} move: '))
        except ValueError as e:
            print(e)
            return self.choose_move()

    def append_card(self, card):
        self.cards.append(card)

    def reset_cards(self):
        self.cards = []


