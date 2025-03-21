class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = set()
        comb = set(supplies)
        n = len(recipes)
        i = 0
        while i < n:
            temp = ingredients[i]
            present = True
            for ing in temp:
                if ing not in comb:
                    present = False
                
            if present is True and recipes[i] not in ans:
                ans.add(recipes[i])
                comb.add(recipes[i])
                i = 0
            else:
                i += 1
        

        return list(ans)