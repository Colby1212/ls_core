class Watercraft(FueledVehicleMixin):
    def __init__(self, number_propellers,
                number_hulls, 
                fuel_efficiecny,
                fuel_capacity):
        self.propellers = number_propellers
        self.hulls = number_hulls
        self.set_fuel_efficiency(fuel_efficiency)
        self.set_fuel_capacity(fuel_capacity)


class MotorBoat(Watercraft):
    def __init__(self, kilometers_per_liter, liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter, liters_of_fuel_capacity)


class Catamaran(Watercraft):
    def __init__(self,
                 number_propellers,
                 number_hulls,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        super().__init__(number_propellers,
                         number_hulls,
                         kilometers_per_liter,
                         liters_of_fuel_capacity)