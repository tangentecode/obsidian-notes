
- Benutzt man um den **Größter Gemeinsamer Teiler** berechnen
- Vollständiger code in [Python](contents-python.md):

```python
# Nutzer Eingabe
zahl_a = int(input("Erste Zahl: "))
zahl_b = int(input("Zweite Zahl: "))

while zahl_b > 0:    # Oder: zahl_b != 0
    rest = zahl_a % zahl_b
    zahl_a = zahl_b
    zahl_b = rest

# Ausgabe

print(zahl_b) # Oder: rest
```

 - Vollständiger code in [C](contents-c.md):
```c 
#include <stdio.h>

int zahl_a;
int zahl_b;

printf("Erste Zahl: ");
scanf("%i\n", &zahl_a);

printf("Zweite Zahl: ");
scanf("%i\n", &zahl_b);
```