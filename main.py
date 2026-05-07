class Arxitektor:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya

    def salom_ber(self):
        print(f"Salom, men {self.ism} {self.familiya}man.")

    def salom_ber(self, ism):
        print(f"Salom, {ism}!")

    def salom_ber(self, ism, familiya):
        print(f"Salom, {ism} {familiya}!")

arxitektor = Arxitektor("Ali", "Valiyev")
arxitektor.salom_ber()  # Salom, men Ali Valiyevman.
arxitektor.salom_ber("Vali")  # Salom, Vali!
arxitektor.salom_ber("Vali", "Valiyev")  # Salom, Vali Valiyev!
```

```python
class Arxitektor:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya

    def salom_ber(self, *args):
        if len(args) == 0:
            print(f"Salom, men {self.ism} {self.familiya}man.")
        elif len(args) == 1:
            print(f"Salom, {args[0]}!")
        elif len(args) == 2:
            print(f"Salom, {args[0]} {args[1]}!")

arxitektor = Arxitektor("Ali", "Valiyev")
arxitektor.salom_ber()  # Salom, men Ali Valiyevman.
arxitektor.salom_ber("Vali")  # Salom, Vali!
arxitektor.salom_ber("Vali", "Valiyev")  # Salom, Vali Valiyev!
