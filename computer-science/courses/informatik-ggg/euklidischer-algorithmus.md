# Euklidischer-algorithmus

- Benutzt man um den **Größter Gemeinsamer Teiler** zu berechnen
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

print("Größter Gemeinsamer Teiler: ", zahl_a)
```

 - Vollständiger code in [C](contents-c.md):

```c 
#include <stdio.h>

int main (void)
{
	int zahl_a;
	int zahl_b;

	printf("Erste Zahl: ");
	scanf("%i\n", &zahl_a);

	printf("Zweite Zahl: ");
	scanf("%i\n", &zahl_b);


	while (zahl_b > 0) // Oder: zahl_b != 0
	{
		rest = zahl_a % zahl_b;
		zahl_a = zahl_b;
		zahl_b = rest;		
	}

	printf("Größter Gemeinsamer Teiler: %i", zahl_a);
}
```
