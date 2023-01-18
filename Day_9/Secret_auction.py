# Secret Auction
from Bidder import Bidder

class SecretAuction:
    def __init__(self) -> None:
        self._bidders = []

    def add_bidder(self, name, bid) -> None:
        self._bidders.append(Bidder(name, bid))

    def _sort_by_bid(self) -> None:
        self._bidders.sort(reverse=True)

    def highest_bidder(self) -> Bidder:
        self._sort_by_bid()
        return self._bidders[0]
