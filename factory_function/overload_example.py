from typing import Optional, Union
from Card import Card
from typing import List, overload
class Hand3:
    @overload 
    def __init__(self, args: "Hand3") -> None:
        pass
    @overload 
    def __init__(self, args1: Card, args2: Card, args3: Card) -> None:
        pass    
    def __init__(
            self,
            arg1: Union[Card, "Hand3"],
            arg2: Optional[Card] = None,
            arg3: Optional[Card] = None
    ) -> None:
        self.dealer_card: Card
        self.cards: List[Card]
        if instance(arg1, Hand3):
            