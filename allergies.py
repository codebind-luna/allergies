from operator import and_


class Allergies(object):
    
    allergen_scores = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128,
        }

    def __init__(self, score):
        self.score = score
        
    def is_allergic_to(self, item):
        return and_(self.score, Allergies.allergen_scores[item]) != 0

    def lst(self):
        return [item for item in Allergies.allergen_scores.keys() if self.is_allergic_to(item)]
        
    
