class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        len_p = len(players)
        len_t = len(trainers)

        p = 0
        t = 0
        output = 0
        while p < len_p and t < len_t:
            print(players[p], trainers[t])
            if players[p] <= trainers[t]:
                output += 1
                p += 1
            t += 1
        
        return output
