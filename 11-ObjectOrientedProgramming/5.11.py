from stadium import C
def main():
    oldtrafford = C({"A":120,"D":150,"G":90,"K":110})
    oldtrafford.m1("G",130)
    print(oldtrafford.m2("GD"))
    print(oldtrafford.m2("KEJ"))
   

if __name__ == "__main__":
    main()