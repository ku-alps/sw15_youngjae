optuzio = []
puta_optuzen = []
rijesen = []

br_mafija = 0

def rijesi (x, mafija) :
    if (rijesen[x]): return
    rijesen[x] = 1
    br_mafija += mafija
    y = optuzio[x]
    temp = puta_optuzen[y] - 1
    if temp == 0 or mafija :
        rijesi(y, not mafija)

people_num = int(sys.stdin.readline())
for i in range(0,people_num):
    scanf("%d", optuzio + i)
    input_number = int(sys.stdin.readline())
    optuzio[i] -=1
    puta_optuzen[optuzio[i]]+=1

for (int i = 0; i < n; ++i) {
    scanf("%d", optuzio + i);
    optuzio[i] -=1;
    puta_optuzen[optuzio[i]]+=1;
}
for (int i = 0; i < n; ++i)
    if (puta_optuzen[i] == 0)
        rijesi(i, true);

for (int i = 0; i < n; ++i)
    rijesi(i, false);

printf("%d\n", br_mafija);

