from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

def calcola_offensivita(frase):
    parole_chiave = ["no", "don't", "thanks", "thank you", "i prefer", "like", "i rather"]
    analyzer = SentimentIntensityAnalyzer()
    punteggio = analyzer.polarity_scores(frase)['compound']*-3
    parole_presenti = sum(1 for parola in parole_chiave if parola in frase)
    if parole_presenti >= 3:
        punteggio += 1
    else:
        punteggio += 0
    lunghezza_frase = len(re.findall(r'\w+', frase))
    if lunghezza_frase >= 4:
        punteggio += 0.4
    else:
        punteggio += 0
    return punteggio

frase_da_valutare = "I don't like discounts"

valore_offensivita = calcola_offensivita(frase_da_valutare.lower())

print(f'La frase "{frase_da_valutare}" ha un valore di offensività pari a: {valore_offensivita}')


