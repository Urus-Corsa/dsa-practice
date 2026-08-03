class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        n houses
        3 colors, each cost different -> red: 0, green: 1, blue:2 
        constraint all houses to be painted, no adjcent houses to be painted the same color
        costs matrix representing cost to paint each house
        return minimum cost to paint all houses while not violating the constraint
        
        len(costs) = number of houses

        it looks like for each house we are given a choice to make, and that is to decide what color should I paint this house with. This choice has 3 possible options however, we can only choose 2 depending on what the prev house colored was. Our goal is to minimize cost + paint all houses + not paint two adjcent houses the same color.

        We have n houses that we need to make this decision for, this means that our decision needs to be repeated n times.
        Our decision has a dependency on our prev decisions made.
        I have a decision tree that has n level (aka height n) and at each level we have 2 options to go with (this is with us knowing that the root node has 3 children either paint red or blue or green but for every later house paint the color that was not the previous) -> 3^n decisions, and for us to get min we need to traverse all and get min at the end. So time would be O(3^n) and space would have to do with recursion call stack growth which we know has direct relationship to the height of decision tree and we can say O(n) for space.

        state -> house_index, prev_color_used, cost_occured; this means that when each house is being considered (house_index) if we knew the min(cost of coloring this house onwards if not painted this house prev_color_used) we could calculate the final result -> top down, and we are using answer to future subproblems.

        Here we have overlapping subproblems that have optimal substructre, for instance we can possibly arrive at the house_index 1 (second house), with having painted the previous house green and occured cost of 2 multiple times which makes this qualified for it being a dp problem where we can cache the results of this once and return early once reached this state again through another path.

        Using top down we should be able to lower our time from having have to traverse the entire decision tree to traversing each decision at most once. So that is O(n*3), and space with caching all that so O(n*3) + O(n) ~ O(n)
        
        dry run = [[17,2,17],[16,16,5],[14,3,19]]
        paintHouse(0,None,0)
            paintHouse(1,0,17)
                paintHouse(2,1,33)
                    paintHouse(3,0,47)
                        cache and return (3,0) = 47
                    cache and return (2,1) 



                    paintHouse(3,2,52)
                paintHouse(2,2,22)
                    paintHouse(3,0,36)
                    paintHouse(3,1,41)
            paintHouse(1,1,2)
                paintHouse(2,0,18)
                    paintHouse(3,1,21)
                    paintHouse(3,2,37)
                paintHouse(2,2,7)
                    paintHouse(3,0,21)
                    paintHouse(3,1,10)
            paintHouse(1,2,17)
                paintHouse(2,0,33)
                    paintHouse(3,1,36)
                    paintHouse(3,2,52)
                paintHouse(2,1,33)
                    paintHouse(3,0,47)
                    paintHouse(3,2,52)
        """
        cache = {}
        houses_count = len(costs)
        
        def paintHouse(house_index, prev_house_color_index):
            if house_index == houses_count:
                return 0
            if (house_index, prev_house_color_index) in cache:
                    return cache[(house_index, prev_house_color_index)]
            min_cost_painting_next_houses = float('inf')
            for i, cost in enumerate(costs[house_index]):
                if i == prev_house_color_index:
                    continue
                min_cost_painting_next_houses = min(min_cost_painting_next_houses, cost + paintHouse(house_index+1, i))
            cache[(house_index, prev_house_color_index)] = min_cost_painting_next_houses
            return cache[(house_index, prev_house_color_index)]
        
        return paintHouse(0,None)
