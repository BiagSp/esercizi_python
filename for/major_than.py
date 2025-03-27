#scrivi un programma che conta quanti numeri, presenti in una lista, sono maggiori del precedente

num_list = [5, 6, 2, 67, 7, 8, 32, 7, 87, 71]

count = 0

for i in num_list:
    if i > num_list[num_list.index(i) - 1]:
        count += 1
        print(f"i numeri maggiore al precedente sono: {i}")



    
print(f"i numeri che sono maggiori del precendete sono {count}")

