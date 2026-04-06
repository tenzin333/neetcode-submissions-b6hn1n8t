from collections import Counter


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize !=0:
            return False
        
        counter = Counter(hand)

        for num in sorted(counter):
            while counter[num] > 0:
                for i in range(groupSize):
                    if counter[num + i] == 0:
                        return False
                    counter[num + i] -=1 
        return True
