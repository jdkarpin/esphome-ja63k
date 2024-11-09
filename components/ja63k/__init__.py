import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart

from esphome.const import CONF_ID

CODEOWNERS = ["@jdkarpin"]
MULTI_CONF = True
DEPENDENCIES = ["uart"]

CONF_JA63K_ID = "ja63k_id"

ja63k_ns = cg.esphome_ns.namespace("ja63k")
ja63kComponent = ja63k_ns.class_("ja63kComponent", cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(ja63kComponent)            
        }
    )
    .extend(uart.UART_DEVICE_SCHEMA)
    .extend(cv.COMPONENT_SCHEMA)
)

FINAL_VALIDATE_SCHEMA = uart.final_validate_device_schema(
    "ja63k",
    baud_rate=9600,
    require_tx=True,
    require_rx=True,
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)