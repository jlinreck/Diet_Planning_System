# data/models/food.py
class Food:
    def __init__(self, 
                 name,
                 calories,
                 proteins,
                 carbs,
                 fats,
                 serving_unit,
                 tags=None):
        self.name = name                  # Display name
        self.calories = calories          # kcal per serving
        self.proteins = proteins          # grams per serving
        self.carbs = carbs                # grams per serving
        self.fats = fats                  # grams per serving
        self.serving_unit = serving_unit  # g, ml, oz, etc.
        self.tags = tags or []            # list of tags (vegan, gluten-free, etc.)
    
    def to_dict(self):
        """Convert food object to dictionary"""
        return {
            "name": self.name,
            "calories": self.calories,
            "macros": {
                "proteins": self.proteins,
                "carbs": self.carbs,
                "fats": self.fats
            },
            "serving": {
                "unit": self.serving_unit
            },
            "tags": self.tags
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create food object from dictionary"""
        return cls(
            name=data["name"],
            calories=data["calories"],
            proteins=data["macros"]["proteins"],
            carbs=data["macros"]["carbs"],
            fats=data["macros"]["fats"],
            serving_unit=data["serving"]["unit"],
            tags=data.get("tags")
        )