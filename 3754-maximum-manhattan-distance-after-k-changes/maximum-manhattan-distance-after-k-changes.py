class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        class Direction:
            def __init__(self, hash_map, k):
                self.hash_map = hash_map
                self.k = k
                self.max_distance = self.get_max_distance(s, 0)

            def get_max_distance(self, s, max_distance):
                total = 0
                right = 0 
                wrong = 0
                for letter in s:
                    if letter in self.hash_map:
                        total += 1
                    else:
                        if self.k > 0:
                            total += 1
                            self.k -= 1
                        else:
                            total -= 1

                    max_distance = max(max_distance, total)
                
                print(total, max_distance, self.k)

                return max_distance

        def assign_hash_map(dir_1, dir_2):
            return { dir_1, dir_2 }


        NE = Direction(assign_hash_map('N', 'E'), k)
        NW = Direction(assign_hash_map('N', 'W'), k)
        SE = Direction(assign_hash_map('S', 'E'), k)
        SW = Direction(assign_hash_map('S', 'W'), k)

        return max(
            NE.max_distance, NW.max_distance, SE.max_distance, SW.max_distance
        )
