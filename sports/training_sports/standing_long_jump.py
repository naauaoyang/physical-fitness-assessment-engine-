from sports.training_sports.training_sport import TrainingSport


class StandingLongJump(TrainingSport):

    def __init__(self):
        TrainingSport.__init__(self,
                               number='FY-M001',
                               name='standing long jump',
                               minimum_age=6,
                               equipment=None,
                               is_independent=True,
                               training_muscle_group='leg',
                               novelty=1,
                               difficulty=1,
                               strength=4,
                               speed=1,
                               endurance=1,
                               coordination=2,
                               flexibility=2)
