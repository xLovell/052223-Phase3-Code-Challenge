from classes.concert import Concert

class Venue:

    def __init__(self, title, city):
        self.title = title
        self.city = city

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 1 <= len(title):
            self._title = title
        else:
            raise Exception
        
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        if isinstance(city, str) and 1 <= len(city):
            self._city = city
        else:
            raise Exception
        
    def concerts(self):
        return [concert for concert in Concert.all if concert.venue == self]
    
    def bands(self):
        return [concert.band for concert in Concert.all if concert.venue == self]
    
    def concert_on(self, date):
        ac = [concert for concert in Concert.all if concert.date == date]
        if len(ac) == 0:
            return None
        else:
            fc = ac[0]
            return fc