import uuid 


class Food:
    def __init__(self, 
                 name,
                 calories,
                 proteins,
                 carbs,
                 fats,
                 serving_unit,
                 tags=None):
        self.id = str(uuid.uuid4())
        self.name = name                
        self.calories = calories       
        self.proteins = proteins     
        self.carbs = carbs           
        self.fats = fats                
        self.serving_unit = serving_unit 
    
    def to_dict(self):
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
            }
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
            serving_unit=data["serving"]["unit"]
        )
    
    def get_id(self):
        return self.id

    def get_calories(self):
        return self.calories
    
    def get_protiens(self):
        return self.proteins
    
    def get_carbs(self):
        return self.carbs
    
    def get_fats(self):
        return self.fats