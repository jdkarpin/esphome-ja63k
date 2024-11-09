import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, text_sensor, uart
from esphome.const import (
    CONF_STATUS,
    ICON_CHIP,
    ENTITY_CATEGORY_DIAGNOSTIC,
    CONF_DISPLAY
)
from esphome.const import CONF_ID

from . import ja63kComponent, CONF_JA63K_ID

# DEPENDENCIES = ["uart"]

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_JA63K_ID): cv.use_id(ja63kComponent),
            cv.Required(CONF_STATUS): text_sensor.text_sensor_schema(
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC, icon=ICON_CHIP
            ),
            cv.Required(CONF_DISPLAY): text_sensor.text_sensor_schema(
                entity_category=ENTITY_CATEGORY_DIAGNOSTIC, icon=ICON_CHIP
            )
        }
    ).extend(cv.COMPONENT_SCHEMA)
)

async def to_code(config):
    var = await cg.get_variable(config[CONF_JA63K_ID])
    if status_config := config.get(CONF_STATUS):
        sens = await text_sensor.new_text_sensor(status_config)
        cg.add(var.set_status_text_sensor(sens))
    if display_config := config.get(CONF_DISPLAY):
        sens = await text_sensor.new_text_sensor(display_config)
        cg.add(var.set_display_text_sensor(sens))
        
        