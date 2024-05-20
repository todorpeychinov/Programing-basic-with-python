price_skumriq_per_kg = float(input())
price_caca_per_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

price_palamud_per_kg = price_skumriq_per_kg + price_skumriq_per_kg * 0.6
price_safrid_per_kg = price_caca_per_kg + price_caca_per_kg * 0.8
PRICE_MIDI_PER_KG = 7.50

total_price = (palamud_kg * price_palamud_per_kg) + \
              (price_safrid_per_kg * safrid_kg) + \
              (midi_kg * PRICE_MIDI_PER_KG)

print(f"{total_price:.2f}")