def calculate_energy(mass):

    speed_of_light = 300000000  # Speed of light in meters per second
    energy = mass * speed_of_light ** 2
    return energy

def main():

    mass= int(input("m: "))
    energy = calculate_energy(mass)
    print("E: {} Joules".format(energy))

if __name__ == "__main__":
    main()