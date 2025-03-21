import uuid
from typing import List, Dict, Optional, Any

class User:
    def __init__(self,age: int,weight: float,height: float,gender: str,weight_goal: float,name: Optional[str] = None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.weight_goal = weight_goal
        
        self.favorite_foods = []
        self.favorite_meals = []

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "weight": self.weight,
            "height": self.height,
            "gender": self.gender,
            "weight_goal": self.weight_goal,
            "favorite_foods": self.favorite_foods,
            "favorite_meals": self.favorite_meals,
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        user = cls(
            age=data.get("age"),
            weight=data.get("weight"),
            height=data.get("height"),
            gender=data.get("gender"),
            weight_goal=data.get("weight_goal"),
            name=data.get("name")
        )
        user.id = data.get("id", user.id) 
        user.favorite_foods = data.get("favorite_foods", [])
        user.favorite_meals = data.get("favorite_meals", [])
        return user

    def add_favorite_foods(self, food_id: str) -> None:
        if food_id not in self.favorite_foods:
            self.favorite_foods.append(food_id)
    
    def remove_favorite_foods(self, food_id: str) -> None:
        if food_id in self.favorite_foods:
            self.favorite_foods.remove(food_id)

    def add_favorite_meal(self, meal_id: str) -> None:
        if meal_id not in self.favorite_meals:
            self.favorite_meals.append(meal_id)
    
    def remove_favorite_meal(self, meal_id: str) -> None:
        if meal_id in self.favorite_meals:
            self.favorite_meals.remove(meal_id)
