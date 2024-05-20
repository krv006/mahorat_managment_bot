from aiogram.fsm.state import State, StatesGroup


class Register(StatesGroup):
    full_name = State()
    email_address = State()
    phone_number = State()  # +example
    nationality = State()
    current_country_of_residence = State()
    highest_degree_attained = State()  # inline keyboard
    name_of_institution = State()
    field_of_study = State()  # Field of Study/Major
    academic_achivements_or_awards = State()  # Academic Achievements or Awards (if any):
    current_job = State()  # Current Job Title/Occupation
    current_workplace = State()  # Current Workplace/Employer/Institution (if applicable)
    detailed_information = State()
    detailed_information1 = State()
    detailed_information2 = State()
    detailed_information3 = State()
    detailed_information4 = State()
    detailed_information5 = State()