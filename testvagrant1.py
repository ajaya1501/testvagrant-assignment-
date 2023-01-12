class Newspaper:
    def __init__(self, name, daily_prices):
        self.name = name
        self.daily_prices = daily_prices
    
    @property
    def weekly_price(self):
        return sum(self.daily_prices)

def find_combinations(newspapers, budget, combination=[]):
    if budget < min(newspaper.weekly_price for newspaper in newspapers):
        return

    for newspaper in newspapers:
        if budget >= newspaper.weekly_price:
            find_combinations(newspapers, budget - newspaper.weekly_price, combination + [newspaper])
    
    if combination:
        print(combination)

newspapers = [
    Newspaper("TOI", [3, 3, 3, 3, 3, 5, 6]),
    Newspaper("Hindu", [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4]),
    Newspaper("ET", [4, 4, 4, 4, 4, 4, 10]),
    Newspaper("BM", [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]),
    Newspaper("HT", [2, 2, 2, 2, 2, 4, 4]),
]

find_combinations(newspapers, 40)
