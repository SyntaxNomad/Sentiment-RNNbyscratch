from data_preprocessing import initialize_data
from RNN import RNN

def main():
    epochs=100
    data , datacopy = initialize_data()
    myrnn= RNN(data,epochs)


main()