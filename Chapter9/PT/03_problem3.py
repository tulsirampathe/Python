
for i in range(2, 21):
    f = open(f"13-year-old/table_{i}.txt", "a")
    
    for j in range(1, 11):
        t = f"{i} X {j} : {i*j} \n"
        f.write(t)
        
    f.close()