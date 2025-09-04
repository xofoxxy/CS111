"""
Pizza Size 	Price 	Diameter 	People Fed
Large 	$14.68 	20 inches 	7 people
Medium 	$11.48 	16 inches 	3 people
Small 	$7.28 	12 inches 	1 person
"""
DIAMETER_LARGE = 20
DIAMETER_MEDIUM = 16
DIAMETER_SMALL = 12

PEOPLE_PER_LARGE = 7
PEOPLE_PER_MEDIUM = 3
PEOPLE_PER_SMALL = 1

PIZZA_PRICE_LARGE = 14.68
PIZZA_PRICE_MEDIUM = 11.48
PIZZA_PRICE_SMALL = 7.28


## CONSTANTS SHOULD GO BELOW THIS COMMENT ##
PI = 3.14159265


def compute_pizza_count(people_to_feed, PIZZA_STATS):
    large, medium, small = 0, 0, 0
    for pizza_size, pizza_stats in PIZZA_STATS.items():
        if pizza_stats["people_fed"] <= people_to_feed:
            numberToBuy = people_to_feed // pizza_stats["people_fed"] # Figure out how many to buy
            people_to_feed = people_to_feed % pizza_stats["people_fed"] # Update the number of people left to feed

            pizza_stats["number_to_buy"] = numberToBuy # Store the number of pizzas to buy in the dictionary itself

            # Below this we just update the counters
            if pizza_size == "Large":
                large += numberToBuy
            elif pizza_size == "Medium":
                medium += numberToBuy
            elif pizza_size == "Small":
                small += numberToBuy

    return large, medium, small

def compute_useless_serving_size_info(people_to_feed, PIZZA_STATS):
    area = 0
    for pizza_size, pizza_stats in PIZZA_STATS.items():
        area += pizza_stats["number_to_buy"]*(pizza_stats["diameter"]/2)**2*PI

    return area

def figure_out_cost(PIZZA_STATS):
    cost = 0
    for pizza_size, pizza_stats in PIZZA_STATS.items():
        cost += pizza_stats["number_to_buy"]*pizza_stats["price"]
    tip_amount = float(input())
    cost = cost*(1+tip_amount/100)
    return cost

def main():

    PIZZA_STATS = {
    "Large": {"price": PIZZA_PRICE_LARGE, "diameter": DIAMETER_LARGE, "people_fed": PEOPLE_PER_LARGE, "number_to_buy": 0},
    "Medium": {"price": PIZZA_PRICE_MEDIUM, "diameter": DIAMETER_MEDIUM, "people_fed": PEOPLE_PER_MEDIUM, "number_to_buy": 0},
    "Small": {"price": PIZZA_PRICE_SMALL, "diameter": DIAMETER_SMALL, "people_fed": PEOPLE_PER_SMALL, "number_to_buy": 0}
    }

    hungry_humans = int(input())

    large, medium, small = compute_pizza_count(hungry_humans, PIZZA_STATS)
    print(f"{large} large pizzas, {medium} medium pizzas, and {small} small pizzas will be needed.")

    pizza_area = compute_useless_serving_size_info(hungry_humans, PIZZA_STATS)
    print(f"A total of {pizza_area:.2f} square inches of pizza will be ordered ({pizza_area/hungry_humans:.2f} per guest).")

    cost = figure_out_cost(PIZZA_STATS)
    print(f"The total cost of the event will be: ${cost:.2f}.")

if __name__ == "__main__":
    main()
