import datetime
from jours_feries_france import JoursFeries


class Ferie:
    def __init__(self):
        self.today = datetime.date.today()
        self.month = str(self.today.month)
        if self.today.month < 10:
            self.month = '0' + self.month
        self.year = str(self.today.year)
        self.ym = self.year + '-' + self.month

    def get_feries(self):
        res = JoursFeries.for_year(int(self.year))
        feries = [(i, str(res[i])) for i in res]
        feries_du_mois = []
        for i in feries:
            if self.ym in i[1]:
                feries_du_mois.append(i)
        return feries_du_mois
