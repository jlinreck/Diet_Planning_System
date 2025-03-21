import uuid

class Meal:
    def __init__(self, foods):
        self.id = str(uuid.uuid4())
        self.foods = foods if foods is not None else []
        self.totalCalories = self.getTotalCalories(foods)
        self.totalProtein = self.getTotalProtein(foods)
        self.totalCarbs = self.getTotalCarbs(foods)
        self.totalFats = self.getTotalFats(foods)

    def to_dict(self):
        return {
            "foods": [food.to_dict() for food in self.foods if hasattr(food, 'to_dict')],
            "totalCalories": self.totalCalories,
            "totalProtein": self.totalProtein,
            "totalCarbs": self.totalCarbs,
            "totalFats": self.totalFats
        }

    def get_id(self):
        return self.id

    def getTotalCalories(self, foods):
        total = 0
        for food in foods:
            total += food.get_calories()
        return total

    def getTotalProtein(self, foods):
        total = 0
        for food in foods:
            total += food.get_protein()
        return total

    def getTotalCarbs(self, foods):
        total = 0
        for food in foods:
            total += food.get_carbs()
        return total

    def getTotalFats(self, foods):
        total = 0
        for food in foods:
            total += food.get_fats()
        return total

    def add_food(self, food):
        self.foods.append(food)
        self.totalCalories += food.get_calories()
        self.totalProtein += food.get_protein()
        self.totalCarbs += food.get_carbs()
        self.totalFats += food.get_fats()

    def remove_food(self, index):
        if 0 <= index < len(self.foods):
            food = self.foods[index]
            self.foods.pop(index)
            self.totalCalories -= food.get_calories()
            self.totalProtein -= food.get_protein()
            self.totalCarbs -= food.get_carbs()
            self.totalFats -= food.get_fats()
            return True
        return False
    
    @classmethod
    def from_dict(cls, meal_dict, food_class):
        foods = []
        for food_dict in meal_dict.get("foods", []):
            foods.append(food_class.from_dict(food_dict))
        return cls(foods)