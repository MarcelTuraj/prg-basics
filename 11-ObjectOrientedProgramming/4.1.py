from tv import Television
def main():
    tv_set = Television(False)
    tv_set.show_status()
    tv_set.turn_on()
    tv_set.show_status()
    tv_set.turn_off()
    tv_set.show_status()

if __name__ == "__main__":
    main()