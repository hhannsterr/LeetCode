class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def split_dot(string):
            return string.split('.')


        ver1 = split_dot(version1)
        ver2 = split_dot(version2)

        length1, length2 = len(ver1), len(ver2)
        if length1 > length2:
            ver2 += ['0'] * (length1 - length2)
        elif length1 < length2:
            ver1 += ['0'] * (length2 - length1)

        for v1, v2 in zip(ver1, ver2):
            temp1 = v1.lstrip('0')
            temp2 = v2.lstrip('0')

            if temp1 == '':
                if temp2 == '':
                    continue
                else:
                    return -1
            else:
                if temp2 == '':
                    return 1
                else:
                    temp1, temp2 = int(temp1), int(temp2)
                    if temp1 > temp2:
                        return 1
                    elif temp1 == temp2:
                        continue
                    else:
                        return -1

        return 0

