changes = 47200

won_10000 = divmod(changes, 10000)
won_5000 = divmod(won_10000[1], 5000)
won_1000 = divmod(won_5000[1], 1000)
won_500 = divmod(won_1000[1], 500)
won_100 = divmod(won_500[1], 100)

print(f"""
잔돈: {changes}
10000원권: {won_10000[0]}
5000원권: {won_5000[0]}
1000원권: {won_1000[0]}
500원권: {won_500[0]}
100원권: {won_100[0]}
""")