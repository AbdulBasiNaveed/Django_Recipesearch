from faker import Faker as fk
import random
from .models import Recipe

the_fake = fk()

def fakedata(n=10) -> None:
        for _ in range(n):
                    
            recipe_name= the_fake.name()
            recipe_details=the_fake.sentence()
            recipe_count=random.randint(0,100)

            r=Recipe.objects.create(
                  
                  recipe_name=recipe_name,
                  recipe_details=recipe_details,
                  recipe_image =" ",
                  recipe_count=recipe_count
            )


            