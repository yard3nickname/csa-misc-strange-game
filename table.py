from has_cards import HasCards


class MoveUnavailableError(Exception):
    pass


class Table(HasCards):
    def __init__(self, cards):
        super().__init__(cards)

        self.init = cards.copy()

    def pop_card(self, card):
        try:
            return self.cards.pop(self.cards.index(card))
        except ValueError as e:
            raise MoveUnavailableError('MoveUnavailableError')

    def reset_cards(self):
        self.cards = self.init.copy()
