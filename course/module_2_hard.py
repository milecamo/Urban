# Задание "Слишком древний шифр"

check_list = {3: 12,
              4: 13,
              5: 1423,
              6: 121524,
              7: 162534,
              8: 13172635,
              9: 1218273645,
              10: 141923283746,
              11: 11029384756,
              12: 12131511124210394857,
              13: 112211310495867,
              14: 1611325212343114105968,
              15: 1214114232133124115106978,
              16: 1317115262143531341251161079,
              17: 11621531441351261171089,
              18: 12151811724272163631545414513612711810,
              19: 118217316415514613712811910,
              20: 13141911923282183731746416515614713812911}


def password(key):
    result = ""
    # first number is in range from 1 to key//2 (and one less if it's an even number)
    for i in range(1, key // 2 + key % 2):
        # sum of 2 numbers can't be greater than key
        for j in range(i + 1, key - i + 1 ):
            # add numbers to result
            if key % (i + j) == 0:
                result += f"{i}{j}"
    return result

# lets check result with check_list
for k in range(3, 21):
    pas = password(k)
    print(k, pas, pas == f"{check_list[k]}")
