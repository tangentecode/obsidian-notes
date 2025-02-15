# Fehler-in-programmes

### [Inf-Schule](https://inf-schule.de/imperative-programmierung/python/konzepte/fehler)

## Arten Von Fehlern:

### Syntaxfehler

- Bei einem Syntaxfehler hat man eine Regel der gewählten Programmiersprache nicht beachtet.
- Syntaxfehler werden in Python vom Compiler erkannt. Ein Compiler ist eine Verarbeitungseinheit, die u.a. ein gegebenes Programm auf die Einhaltung der Syntaxregeln der Programmiersprache überprüft.
- Der Python-Compiler liefert auch Information über die Art des Fehlers und die Stelle im Programm, an der der Fehler auftritt. Diese Rückmeldung sollte man bei der Fehlersuche genau beachten

### Laufzeitfehler

- Laufzeitfehler treten während der Abarbeitung des Programs (zur Laufzeit) auf.
- [Python](contents-python.md) liefert (wie viele andere Programmiersysteme) bei Laufzeitfehlern genauere Informationen über die Art des Fehlers. Mit diesen Informationen kann man in der Regel den Fehler lokalisieren und genauer bestimmen.

### Logische Fehler

- Logische Fehler liegen vor, wenn das System nicht die beabsichtigten Ausgaben erzeugt.
- Logische Fehler sind manchmal schwer zu finden. Das Programmiersystem liefert erst einmal keine Hinweise, wo sie sich befinden. Hier muss der Programmentwickler selbst auf die Fehlersuche gehen.
