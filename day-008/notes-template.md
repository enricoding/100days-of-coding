# Tag 001 – Variablen & Strings

**Datum:** [03.06.2026]
**Dauer:** [3 Stunden]

---

## Was ich heute gelernt habe

Heute habe ich gelernt wie man inputs mit Funktionen Kombiniert und wie man im allgemeienn Funktionen definiert
Das vermittelte wissen wurde gleich angewendete und eine Caesar Cipher zum verschsclüsseln und entschlüsseln zu bauen 

---

## Code des Tages
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")


---

## Was war schwierig?

Dieser Tag war schon ziemlich anspruchsvoll, das bereits gelernte wissen hiuer anzuwenden da musst ich ziemlich ioft anchschauen und habe viele Fehler gemacht
---

## Meine eigene Abwandlung

Ich muss erst noch mehr lernen um eigene Abwandlungen zu erstellen

## Morgen lerne ich

- [ ] Tag 9: Dictonaries, Nesting and Secret Auction
