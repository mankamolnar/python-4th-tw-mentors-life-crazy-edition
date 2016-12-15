from codecool_class import CodecoolClass
from mentor import Mentor
from student import Student
from hot import HeadsOrTails
from coffee_machine import *
from presentation import Presentation
from yoga_session import YogaSession
import time
from datetime import date
from lama import *


def main():
    codecool_bp = CodecoolClass.generate_local()
    codecool_bp.print_welcome_message()
    time.sleep(5)

    tivadar = Coffee_machine()
    today_presentation = Presentation("Advanced Github")
    hot_game = HeadsOrTails(1, 2)
    macilaci = codecool_bp.find_mentor_by_full_name("Laci Maci")
    macilaci.introduce_mentor()
    macilaci.print_status()
    time.sleep(5)

    macilaci.drink_coffee(tivadar)
    time.sleep(5)

    today_presentation.fill_m(codecool_bp.mentors)
    today_presentation.fill_s(codecool_bp.students)
    today_presentation.hold_presentation()
    time.sleep(5)

    today_yoga = YogaSession(str(date.today()) + " : 14:00", "Yin")
    today_yoga.print_status()
    today_yoga.add_to_session(codecool_bp.students, codecool_bp.mentors)
    today_yoga.do_yoga()
    time.sleep(5)

    fanni = codecool_bp.find_student_by_full_name("Fanni Skoda")
    fanni.introduce_student()
    fanni.print_status()
    fanni.play_HOT(hot_game)
    fanni.print_status()
    time.sleep(5)

    sanyi = Lama("Sanyi", "red")
    sanyi.introduce_lama()
    time.sleep(5)
    fanni.print_status()
    fanni.pet_lama(sanyi)
    time.sleep(5)
    fk = codecool_bp.find_student_by_full_name("Kukisz Fikusz")
    fk.introduce_student()
    fk.print_status()
    time.sleep(5)
    fk.ride_lama(sanyi)
    time.sleep(5)
    fk.massage_lama(sanyi)
    time.sleep(5)

    codecool_bp.print_goodbye_message()

if __name__ == '__main__':
    main()
