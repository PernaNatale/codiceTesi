from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

def calcola_offensivita(frase):
    negazione_ringraziamento = ["no", "don't", "thanks", "thank you"]
    parole_chiave = ["i prefer", "like", "i rather"]
    analyzer = SentimentIntensityAnalyzer()
    punteggio = analyzer.polarity_scores(frase)['compound']*-1
    parole_presenti = sum(1 for parola in negazione_ringraziamento if parola in frase)
    key_words = sum(1 for parola in parole_chiave if parola in frase)
    if key_words >=1:
        punteggio +=0.7
    if parole_presenti >= 2:
        punteggio += 0.5
    lunghezza_frase = len(re.findall(r'\w+', frase))
    if lunghezza_frase >= 4:
        punteggio += 0.4
    return punteggio

frase_da_valutare = "No, i don't feel lucky"

valore_offensivita = calcola_offensivita(frase_da_valutare.lower())

print(f'La frase "{frase_da_valutare}" ha un valore di offensività pari a: {valore_offensivita}')


