class Student:
    def __init__(self, name, gender, grade, height, weight,
                 vital_capacity=None,
                 fifty_m_run=None,
                 sit_and_reach=None,
                 one_minute_rope_skipping=None,
                 sit_up=None,
                 fifty_m_run_eight_shuffle=None):
        """

        :param name:
        :param gender:
        :param grade:
        :param height: in meter
        :param weight: in kilogram
        :param vital_capacity: in milliliter
        :param fifty_m_run: in seconds
        :param sit_and_reach: in centimeter
        :param one_minute_rope_skipping: counts
        :param sit_up: counts
        :param fifty_m_run_eight_shuffle:
        """
        self.name = name
        self.gender = gender
        self.grade = grade
        self.height = height
        self.weight = weight
        self.vital_capacity = vital_capacity
        self.fifty_m_run = fifty_m_run
        self.sit_and_reach = sit_and_reach
        self.one_minute_rope_skipping = one_minute_rope_skipping
        self.sit_up = sit_up
        self.fifty_m_run_eight_shuffle = fifty_m_run_eight_shuffle

    def get_speed(self):
        pass

    def get_strength(self):
        pass

    def get_endurance(self):
        pass

    def get_coordination(self):
        pass

    def get_flexibility(self):
        pass

    def get_bmi(self):
        pass


