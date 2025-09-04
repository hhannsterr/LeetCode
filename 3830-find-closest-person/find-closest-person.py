class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:       
        displacement_x = abs(z - x)
        displacement_y = abs(z - y)

        if displacement_x < displacement_y:
            return 1
        elif displacement_x == displacement_y:
            return 0
        else:
            return 2
