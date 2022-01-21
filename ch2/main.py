import kNN


group, labels = kNN.createDataSet()
ret = kNN.classify0([0, 0], group, labels, 3)
print(f"Result is {ret}")
