from tv import Television
def main():
    tv_set = Television()
    tv_set.is_on = False
    tv_set.show_status()
    tv_set.turn_on()
    tv_set.add_channels()
    tv_set.set_channel(5)
    tv_set.show_status()
    tv_set.turn_off()
    tv_set.show_status()
    tv_set.decrease_volume()
    tv_set.show_status()
    tv_set.decrease_volume()
    tv_set.show_status()
    tv_set.increase_volume()
    tv_set.increase_volume()
    tv_set.increase_volume()
    tv_set.show_status()
    tv_set.show_channels()
    tv_set.turn_on()
    tv_set.show_status()

if __name__ == "__main__":
    main()