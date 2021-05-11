from .. import Solver
from ...simulator.Craft import Craft


class JustDoIt(Solver):
    @staticmethod
<<<<<<< HEAD
    def suitable(craft):
        return craft.player.lv >= 80 and craft.recipe.recipe_row["RecipeLevelTable"]["ClassJobLevel"] + 10 <= craft.player.lv

    def __init__(self, craft, logger):
        super().__init__(craft, logger)
        self.can_hq = craft.recipe.recipe_row["CanHq"]

    def process(self, craft, used_skill=None) -> str:
        if used_skill is None and self.can_hq:
            return '工匠的神速技巧'
        if craft is None:
            craft = Craft(self.recipe, self.player)
=======
    def suitable(recipe, player):
        return player.lv >= 80 and recipe.recipe_row["RecipeLevelTable"]["ClassJobLevel"] + 10 <= player.lv

    def __init__(self, recipe, player, logger):
        super().__init__(recipe, player, logger)
        self.recipe = recipe
        self.player = player
        self.can_hq = recipe.recipe_row["CanHq"]

    def process(self, craft=None, used_skill=None) -> str:
        if craft is None and self.can_hq:
            return '工匠的神速技巧'
        if craft is None:
            craft = Craft(self.recipe,self.player)
>>>>>>> 950e35837d27fe95958ce7b6a012c0e0bda6e41c
        temp = craft.clone().use_skill("坯料制作")
        if temp.is_finished():
            return "坯料制作"
        elif temp.current_durability <= 0:
            return '精修'
        elif '崇敬' in craft.effects:
            return "坯料制作"
        else:
            return '崇敬'
