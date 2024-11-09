import esphome.codegen as cg
from esphome.components import button
import esphome.config_validation as cv

from esphome.const import (
    ENTITY_CATEGORY_DIAGNOSTIC,
    ICON_DATABASE,
    CONF_NAME
)

from .. import CONF_JA63K_ID, ja63kComponent, ja63k_ns

KEY_NAMES = (
    "Key_1", "Key_2", "Key_3", 
    "Key_4", "Key_5", "Key_6", 
    "Key_7", "Key_8", "Key_9",
    "Key_F", "Key_0", "Key_N",    
)

KeyPad_Key = ja63k_ns.class_("QueryButton", button.Button)

CONF_QUERY_PARAMS = "query_params"

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_JA63K_ID): cv.use_id(ja63kComponent)
    }
)

CONFIG_SCHEMA = CONFIG_SCHEMA.extend(
    {
        cv.Required(f"{x}"): button.button_schema(
            KeyPad_Key,
            entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
            icon=ICON_DATABASE,
        )
        for x in KEY_NAMES
    }
)

async def to_code(config):
    var = await cg.get_variable(config[CONF_JA63K_ID])
    # if query_params_config  := config.get(CONF_QUERY_PARAMS):
    #     b = await button.new_button(query_params_config)
    #     await cg.register_parented(b, config[CONF_JA63K_ID])
    #     cg.add(var.set_query_button(b))
    for x in KEY_NAMES:
        if conf := config.get(x):
            b = await button.new_button(conf)
            await cg.register_parented(b, config[CONF_JA63K_ID])
            cg.add(var.set_query_button(b))
        