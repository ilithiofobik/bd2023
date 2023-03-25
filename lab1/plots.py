import matplotlib.pyplot as plt

def bloom_plot(x, y):
    plt.clf()
    plt.xlabel('number of words added to filter')
    plt.ylabel('number of words represented by filter')
    plt.title("False positive experiment")
    plt.plot(x, y, 'r', label='TP + FP')
    plt.plot(x, x, 'b', label='TP')
    plt.legend()
    plt.savefig('data/bloom_exp.png')