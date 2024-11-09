import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    ICON_POWER,
    DEVICE_CLASS_FREQUENCY,
    UNIT_EMPTY,
    ENTITY_CATEGORY_DIAGNOSTIC
)

from . import ja63kComponent, CONF_JA63K_ID

CONF_MODE = "mode"
CONF_POWER_LED = "power"
CONF_ALARM_LED = "alarm"
CONF_TAMPER_LED = "tamper"
CONF_MALFUNCTION_LED = "malfunction"
CONF_LOCK_LED = "lock"
CONF_WIRELESS_LED = "wireless"
CONF_BEEP = "beep"

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_JA63K_ID): cv.use_id(ja63kComponent),
            cv.Required(CONF_MODE): sensor.sensor_schema(
                icon=ICON_POWER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_FREQUENCY,
                unit_of_measurement=UNIT_EMPTY
            ),
            cv.Required(CONF_POWER_LED): sensor.sensor_schema(
                icon=ICON_POWER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_FREQUENCY,
                unit_of_measurement=UNIT_EMPTY
            ),
            cv.Required(CONF_ALARM_LED): sensor.sensor_schema(
                icon=ICON_POWER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_FREQUENCY,
                unit_of_measurement=UNIT_EMPTY
            ),
            cv.Required(CONF_TAMPER_LED): sensor.sensor_schema(
                icon=ICON_POWER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_FREQUENCY,
                unit_of_measurement=UNIT_EMPTY
            ),
            cv.Required(CONF_MALFUNCTION_LED): sensor.sensor_schema(
                icon=ICON_POWER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_FREQUENCY,
                unit_of_measurement=UNIT_EMPTY
            ),
            cv.Required(CONF_LOCK_LED): sensor.sensor_schema(
                icon=ICON_POWER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_FREQUENCY,
                unit_of_measurement=UNIT_EMPTY
            ),
            cv.Required(CONF_WIRELESS_LED): sensor.sensor_schema(
                icon=ICON_POWER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_FREQUENCY,
                unit_of_measurement=UNIT_EMPTY
            ),
            cv.Required(CONF_BEEP): sensor.sensor_schema(
                icon=ICON_POWER,
                accuracy_decimals=0,
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
                unit_of_measurement=UNIT_EMPTY
            )
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
)

async def to_code(config):
    var = await cg.get_variable(config[CONF_JA63K_ID])

    if mode_config := config.get(CONF_MODE):
        sens = await sensor.new_sensor(mode_config)
        cg.add(var.set_mode_sensor(sens))
    if power_led_config := config.get(CONF_POWER_LED):
        sens = await sensor.new_sensor(power_led_config)
        cg.add(var.set_power_led_sensor(sens))
    if alarm_led_config := config.get(CONF_ALARM_LED):
        sens = await sensor.new_sensor(alarm_led_config)
        cg.add(var.set_alarm_led_sensor(sens))
    if tamper_led_config := config.get(CONF_TAMPER_LED):
        sens = await sensor.new_sensor(tamper_led_config)
        cg.add(var.set_tamper_led_sensor(sens))
    if malfunction_led_config := config.get(CONF_MALFUNCTION_LED):
        sens = await sensor.new_sensor(malfunction_led_config)
        cg.add(var.set_malfunction_led_sensor(sens))
    if lock_led_config := config.get(CONF_LOCK_LED):
        sens = await sensor.new_sensor(lock_led_config)
        cg.add(var.set_lock_led_sensor(sens))
    if wireless_led_config := config.get(CONF_WIRELESS_LED):
        sens = await sensor.new_sensor(wireless_led_config)
        cg.add(var.set_wireless_led_sensor(sens))
    if beep_config := config.get(CONF_BEEP):
        sens = await sensor.new_sensor(beep_config)
        cg.add(var.set_beep_sensor(sens))