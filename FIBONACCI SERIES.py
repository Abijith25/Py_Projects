print("\n \n THE PROGRAM TO GENERATE FIBONACCI SERIES")
series=[0,1]
terms=int(input("ENTER THE NO.OF.TERMS FOR FIBONACCI SERIES"))
for i in range(2,terms):
    inc=series[i-1]+series[i-2]
    series.append(inc)
print("THE FIBONACCI SERIES UPTO",terms," IS ",series)
