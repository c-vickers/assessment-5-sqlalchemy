"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()


#Hi Anne! The below query kept failing with ascii error for me. I dropped my database, changed the .sql file to remove special character from Citroen and re-created the database and the query worked. Sorry if that was not the correct solution!
# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()


# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded>1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter_by(founded=1903, discontinued = None).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter((Brand.discontinued != None) | (Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()


# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    return db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter(Model.year == year).all()

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

     brands = db.session.query(Model.brand_name, Model.name).order_by(Model.brand_name).all()

     brand_dict = {}

     for brand, model in brands:
     	if brand not in brand_dict:
     		brand_dict[brand] = [model]
     	else:
     		brand_dict[brand].append(model)

     for brand, model in brand_dict.items():
     	print '\n' + brand
     	print '\n'.join(model)


     # for brand, model in brands:
     # 	print brand, model


# ---------------------Part 2 Discussion Questions----------------------------
#Question 1: What is the returned value and datatype of Brand.query.filter_by(name='Ford')?

#Answer 1: Returned value is <flask_sqlalchemy.BaseQuery object at 0x11040e390>. Type is BaseQuery Object.


#Question 2: In your own words, what is an association table, and what type of relationship (many to one, many to many, one to one, etc.) does an association table manage?

#Answer 2: An association table is a table that acts as a link for many-to-many relationship tables utilizing foreign keys to establish the relationships.


# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    return Brand.query.filter(Brand.name.like('%'+mystr+'%')).all


def get_models_between(start_year, end_year):
    return Model.query.filter(Model.year > start_year, Model.year < end_year).all()

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
