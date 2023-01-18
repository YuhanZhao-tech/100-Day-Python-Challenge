class Bidder:
    def __init__(self, name, bid) -> None:
        self._name = name
        self._bid = bid

    def get_name(self) -> str:
        return self._name

    def get_bid(self) -> float:
        return float(self._bid)

    def __eq__(self, other) -> bool:
        return self._bid == other.get_bid()

    def __lt__(self, other) -> bool:
        return self._bid < other.get_bid()