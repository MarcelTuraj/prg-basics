class TaxiRide:

    def __init__(self, rate_per_km, distance):

        self.rate_per_km = rate_per_km  # value in € (e.g. €2)

        self.distance = 0

        self.fare = 0


    def calculate_fare(self, distance):

        self.distance = distance

        self.fare = self.distance * self.rate_per_km


    def print_receipt(self):

        print("RECEIPT")

        print("=======")

        print(f"distance: {self.distance}")

        print(f"rate: {self.rate_per_km}")

        print(f"fare: {self.fare}")



def main():

    taxi1 = TaxiRide(2, 20)

    taxi1.calculate_fare(20)  # Provide the distance here

    taxi1.print_receipt()  # No arguments needed since it uses instance variables

    taxi2 = TaxiRide(4, 40)

    taxi2.calculate_fare(40)  # Provide the distance here

    taxi2.print_receipt()  # No arguments needed since it uses instance variables


if __name__ == "__main__":

    main()