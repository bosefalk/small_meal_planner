# Randomly selects 4 meals from meals.db, weighted by their weight column (higher = more chance)

def random():
    import sqlite3
    import numpy

    conn = sqlite3.connect("meals.db")

    c = conn.cursor()

    c.execute("SELECT * FROM meal_list")
    meals = c.fetchall()

    meals = meals[1:] # Drop column headers
    elements = [i[0] for i in meals] # Split out meals only
    probs = [i[1] for i in meals] # Split their probabilities

    # Calculate probability distibution, weight / total sum of weights
    prob_sum = sum(probs)
    prob_dist = [i/prob_sum for i in probs]

    # Sample without replacement, weighted by probability distribution
    result = numpy.random.choice(elements, size = 4, p = prob_dist, replace = False)

    return(result)


    conn.commit()
    conn.close()

# Given a list of meals and an index, adds 1 to its weight in the database
def update(meal_list, position):
    import sqlite3
    conn = sqlite3.connect("meals.db")
    c = conn.cursor()

    to_update = [meal_list[position - 1]]

    c.execute("""UPDATE meal_list SET weight = (weight + 1) WHERE meal = ?""", to_update)

    conn.commit()
    conn.close()