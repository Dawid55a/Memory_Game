# Memomry_Game

Memory_game jest to prosta gra w której musimy odkryć pary znaków.

## Technologie
* [Kivy 11.1.1](https://kivy.org/#download)
* [Python 3.7](https://www.python.org/) 

# Instalacja
```
git clone https://github.com/Dawid55a/Memory_Game.git
cd Memory_Game
pip install -r requirements.txt
```
Aby uruchomić aplikację należy wpisać
```
python main.py
```

# Działanie
 ![Main_Screen_Small](https://user-images.githubusercontent.com/21986555/76655833-862b1600-656e-11ea-87ca-961b07c42283.png) 

Na ekranie gry klikamy w pola które pokazują nam ukryty znak. Po wybraniu dwóch jest sprawdzana ich poprawność i wykonywane są dwie opcje:
- Wybrane pola są różne: Pola się resetują
- Wybrane pola są takie same: Pola się wyszarzają

![Winner_Screen](https://user-images.githubusercontent.com/21986555/76657089-516c8e00-6571-11ea-8a82-f282ed5a9ccf.png)
Po eliminacji wszystkich pól pojawia się napis `Winner!!!`

![Settings_Screen_Small](https://user-images.githubusercontent.com/21986555/76655829-85927f80-656e-11ea-9d7b-66ee34dac68a.png)
Na ekranie ustawień mamy Widget służący wyborowi koloru kart (aktualnie wypisujący tylko w logach wybrany kolor)

# Dlaczego Kivy i Python?
Pomimo że, python nie jest językiem który ma powszechne zastosowanie w aplikacjach mobilnych postanowiłem wykorzystać wieloplatformowośc Kivy i podjąć wyzwanie stworzenia takiej aplikacji.

Przy pomocy [buildozera](github.com/kivy/buildozer) skompilowałem program do pliku .apk
Sprawił mi wiele problemów, jednak udało mi się przy jego pomocy kompilować swoją grę.

Niestety i tu natrafiłem na problem, bo po instalacji aplikacji widzimy tylko czarny ekran. 
Jest to problem z którym aktualnie się zmagam.

# Do zrobienia
- Skompilowanie w pełni działającego pliku .apk
- Inicjalizacja gry przy uruchomieniu
- Dodanie czasu ukończenia gry

~~- Usuwanie Widgetu `Winner!!!` przy tworzeniu nowej gry~~
- Zmiana koloru kart
- Możliwość wyboru rozmiaru pola gry
