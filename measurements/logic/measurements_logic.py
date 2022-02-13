from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def create_measurement(meas):
    measurement = Measurement(variable=meas["variable"], value=meas["value"], unit=meas["unit"], place=meas["place"])
    measurement.save()
    return measurement

def update_measurement(var_pk, new_meas):
    measurement = get_measurement(var_pk)
    measurement.variable = new_meas["variable"]
    measurement.value = new_meas["value"]
    measurement.unit = new_meas["unit"]
    measurement.place = new_meas["place"]
    measurement.save()
    return measurement

