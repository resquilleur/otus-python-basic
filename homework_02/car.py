from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    engine: None

    def set_engine(self, new_engine: Engine):
        self.engine = new_engine
