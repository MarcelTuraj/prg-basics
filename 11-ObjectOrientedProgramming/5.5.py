from thermo import Thermo 
def main():
    mythermo = Thermo()
    mythermo.turnon()
    mythermo.measure()
    mythermo.display()
    mythermo.turnoff()

if __name__ == "__main__":
    main()