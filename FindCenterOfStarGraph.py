class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Check if e[0][0] == e[1][0] or e[0][0] == e[1][1]
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1] :
            return edges[0][0]
        else:
            return edges[0][1]

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][edges[0][1] in edges[1]]
            
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()