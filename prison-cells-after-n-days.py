class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        
        iterate through and keep adding to hashtable using tuples
        once one is already detected that is in the hashtable
        
        
        """
        hm = []
        hmset = set()
        # if not (cells[0] == 1 or cells[len(cells)-1] == 1):
        #     hm.append(cells)
        #     hmset.add(tuple(cells))
        for day in xrange(N):
            print(day)
            newCell = []
            for cellIdx in range(1, len(cells)-1):
                if (cells[cellIdx-1] == 0 and cells[cellIdx+1] == 0) or (cells[cellIdx-1] == 1 and cells[cellIdx+1] == 1):
                    newCell.append(1)
                else:
                    newCell.append(0)
            newCell.insert(0, 0)
            newCell.append(0)
            cells = newCell
            if tuple(newCell) not in hmset:
                hm.append(newCell)
                hmset.add(tuple(newCell))
            else:
                break
        idx = (N - 1) % len(hm)
        return hm[idx]
            
        
