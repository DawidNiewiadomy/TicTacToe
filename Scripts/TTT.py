class KolkoKrzyzyk:
    def __init__(self):
        self.aktualny_gracz='X '
        self._run=True
    @staticmethod
    def plansza_gry(lista): #wyswietli aktualna plansze gry
        print(f'| {lista[0]} | {lista[1]} | {lista[2]} |')
        print("|----|----|----|")
        print(f'| {lista[3]} | {lista[4]} | {lista[5]} |')
        print("|----|----|----|")
        print(f'| {lista[6]} | {lista[7]} | {lista[8]} |')
    @staticmethod
    def wygrana(gracz): #sprawdzi czy ktos wygral

        lista_wygranych= [[0,1,2],[3,4,5],[6,7,8], #poziomo
                          [0,3,6],[1,4,7],[2,5,8], #pionowo
                          [0,4,8],[2,4,6] #skos
                          ]

        for uklad in lista_wygranych:
            lista_gracza = []
            for i in uklad:
                if i in gracz:
                    lista_gracza.append(True)
                else:
                    lista_gracza.append(False)
            if all(lista_gracza):
                return True
        return False

    @staticmethod
    def remis(zajete): #sprawdzi czy nastapil remis
        if len(zajete)==9:
            return True
        return False
    def system_close(self):
        print("Do widzenia!")
        self._run=False


    def gra(self):
        if self.aktualny_gracz == 'X ':
            self.aktualny_gracz = 'O '
        else:
            self.aktualny_gracz = 'X '
        wyjscie=True
        graczx=[]
        graczo=[]
        lista_miejsc_zajetych=[]
        plansza=[[],[],[],[],[],[],[],[],[]]
        #glowna petla
        while not self.wygrana(graczx) and not self.wygrana(graczo) and not self.remis(lista_miejsc_zajetych):
            self.plansza_gry(plansza) #wyswietl plansze gry
            try:
                ruch=int(input("Wybierz miejsce na planszy graczu: "f'{self.aktualny_gracz} ' "lub wpisz liczbę 100 aby zakończyć grę"))
            except ValueError:
                print("Podana wartość musi być liczbą!")
                continue
            ruch=ruch-1
            if ruch==99:
                wyjscie=False
                self.system_close()
                self.run()
                break
            if ruch<0 or ruch>8:
                print("Niedozwolone!")
                continue
            if ruch in lista_miejsc_zajetych:
                print("To miejsce jest zajete")
                continue

            else:
                lista_miejsc_zajetych.append(ruch)
                if self.aktualny_gracz=='X ':
                    graczx.append(ruch)

                else:
                    graczo.append(ruch)

            plansza[ruch]=self.aktualny_gracz
            if self.aktualny_gracz == 'O ':
                self.aktualny_gracz='X '
            else:
                self.aktualny_gracz='O '

        if self.remis(lista_miejsc_zajetych) and not(self.wygrana(graczo) or self.wygrana(graczx)):
            self.plansza_gry(plansza)
            print("REMIS!!!")
        elif self.wygrana(graczo) or self.wygrana(graczx):
            self.plansza_gry(plansza)
            if self.aktualny_gracz == 'X ':
                self.aktualny_gracz='O '
            else:
                self.aktualny_gracz='X '
            print("Zwycieżył gracz: ",self.aktualny_gracz)
        if wyjscie:
            stan_gry=int(input("1-Graj dalej, 100-zakoncz"))
            if stan_gry==1:
                self.run()
            elif stan_gry==100:
                self.system_close()
                self.run()


    def run(self):
        if self._run:
            self.gra()
        else:
            print("!!!Zakonczono!!!")


if __name__ == '__main__':
    kolko=KolkoKrzyzyk()
    kolko.run()






