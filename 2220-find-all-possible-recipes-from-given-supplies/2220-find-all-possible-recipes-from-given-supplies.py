class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        id_counter = 0
        name_to_id = {}
        for recipe in recipes:
            name_to_id[recipe] = id_counter
            id_counter += 1
        for ingredient_list in ingredients:
            for ingredient in ingredient_list:
                if ingredient not in name_to_id:
                    name_to_id[ingredient] = id_counter
                    id_counter += 1
        G = defaultdict(list)
        indegree = [0] * id_counter
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                G[name_to_id[ingredient]].append(name_to_id[recipe])
                indegree[name_to_id[recipe]] += 1
        q = deque([name_to_id[supply] for supply in supplies if supply in name_to_id])
        result = []
        while q:
            u = q.popleft()
            for v in G[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
                    if v in [name_to_id[recipe] for recipe in recipes]:
                        result.append(recipes[[name_to_id[recipe] for recipe in recipes].index(v)])
        return result
