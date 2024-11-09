#pragma once


#include "esphome/components/text_sensor/text_sensor.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/button/button.h"
#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"

namespace esphome {
namespace ja63k {

static const std::map<std::string, uint8_t> KEY_MAP_STRING_TO_INT {
  { "1", 0x81 }, { "2", 0x82 }, { "3", 0x83 },
  { "4", 0x84 }, { "5", 0x85 }, { "6", 0x86 },
  { "7", 0x87 }, { "8", 0x88 }, { "9", 0x89 },
  { "F", 0x8F }, { "0", 0x80 }, { "N", 0x8E },
};

static const std::map<uint8_t, std::string> DISPLAY_MAP_INT_TO_STRING {
  // 0             19            2A            3B            4C            5D            6E            7F
                {0x01, " 1"}, {0x02, " 2"}, {0x03, " 3"}, {0x04, " 4"}, {0x05, " 5"}, {0x06, " 6"}, {0x07, " 7"}, // 8
  {0x08, " 8"}, {0x09, " 9"}, {0x0A, "10"}, {0x0B, "11"}, {0x0C, "12"}, {0x0D, "13"}, {0x0E, "14"}, {0x0F, "15"}, // 
  {0x10, "16"}, {0x11, " A"},               {0x13, " C"}, {0x14, " d"},                             {0x17, " U"},  
                {0x19, "  "}, {0x1A, " P"}, {0x1B, " -"}, {0x1C, " L"}, {0x1D, " J"}, {0x1E, "| "}, {0x1F, " |"}, 
                {0x21, "c1"}, {0x22, "c2"}, {0x23, "c3"}, {0x24, "c4"}, {0x25, "c5"}, {0x26, "c6"}, {0x27, "c7"}, 
  {0x28, "c8"}, 
                {0x41, "1*"}, 
                                            {0x53, "C*"},  
                {0x59, "  "},               {0x5b, " -"},                             {0x5e, ", "}, {0x5f, " ,"},
                {0x61, "c1 Tempered blinking"},
};


static const std::map<uint8_t, std::string> STATUS_MAP_INT_TO_STRING {
  {0x00, "Service Mode"},
  {0x20, "User Mode"},
  {0x40, "Disarmed"},
  {0x41, "Armed"},
  {0x44, "Tamper alarm"},
  {0x45, "Tamper alarm"},
  {0x49, "Entry delay"},
  {0x51, "Arming"},
  {0x61, "ArmedA"},
  {0x63, "ArmedB"},
  {0x69, "Entry delay B"},
  {0x71, "ArmingA"},
  {0x73, "ArmingB"},
};

class ja63kComponent : public Component, public uart::UARTDevice {
  SUB_SENSOR(mode)
  SUB_SENSOR(power_led)
  SUB_SENSOR(alarm_led)
  SUB_SENSOR(tamper_led)
  SUB_SENSOR(malfunction_led)
  SUB_SENSOR(lock_led)
  SUB_SENSOR(wireless_led)
  SUB_SENSOR(beep)
  SUB_BUTTON(query)
  SUB_TEXT_SENSOR(status)
  SUB_TEXT_SENSOR(display)
 public:
  // Nothing really public.

  // ========== INTERNAL METHODS ==========
  void loop() override;
  void dump_config() override;
  void read_all_info(const std::string &name);

 protected:
  void readline_(int readch, uint8_t *buffer, int len);
  void sendline_(uint8_t *buffer, int len);
  void print_buffer(uint8_t *buffer, int len);
};

}  // namespace ja63k
}  // namespace esphome