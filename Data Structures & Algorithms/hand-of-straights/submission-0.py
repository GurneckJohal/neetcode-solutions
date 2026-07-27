class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        counts = {}
        lowest = float("inf")
    

        for card in hand:
            curr = counts.get(card, 0)
            counts[card] = curr + 1
            lowest = min(lowest, card)

        next_card = lowest
        group_count = 0
        while len(counts) > 0:
            if group_count == groupSize:
                group_count = 0
                new_lowest = float("inf")
                for card in counts.keys():
                    new_lowest = min(new_lowest, card)
                next_card = new_lowest
            if next_card in counts:
                counts[next_card] -= 1
                if counts[next_card] == 0:
                    del counts[next_card]
                next_card += 1
                group_count += 1
            else:
                return False
        
        return True


        