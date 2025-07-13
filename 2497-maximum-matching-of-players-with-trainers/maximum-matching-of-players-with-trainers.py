class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        len_p = len(players)

        p = 0
        output = 0
        for trainer in trainers:
            if players[p] <= trainer:
                output += 1
                p += 1
            if p >= len_p:
                break
        
        return output
