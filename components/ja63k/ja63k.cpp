#include "ja63k.h"
#include "esphome/core/helpers.h"
#include "esphome/core/log.h"
#include "esp_log.h"

namespace esphome {
namespace ja63k {

static const char *const TAG = "ja63k.sensor";

void ja63kComponent::loop() {
  const int max_line_length = 80;
  static uint8_t buffer[max_line_length];
  static int count = 0;
  while (available()) {
    this->readline_(read(), buffer, max_line_length);
  }
}

void ja63kComponent::readline_(int readch, uint8_t *buffer, int len) {
  static int pos = 0;

  if (readch >= 0) {
    if (pos < len - 1) {
      buffer[pos++] = readch;
      buffer[pos] = 0;
    } else {
      pos = 0;
    }
    if (readch == 0xFF) {
      this->print_buffer(buffer, pos);
      switch(buffer[0]) {
        case 0xA0:
        case 0xA1:
        case 0xA2:
        case 0xA4:
        case 0xA8:
        case 0xAA:
          this->beep_sensor_->publish_state(buffer[0]);
          break;
        case 0xE0: {
          this->beep_sensor_->publish_state(0);
          this->mode_sensor_->publish_state(buffer[1]);
          uint8_t led = buffer[2];

          // 0b0100 0101 = \x45 // power on, wireless on, temper blinking
          // 0b0000 0111 = \x07 // power on, Wrench blinking
          // 0b0000 0001 = \x01 // power on
          // 0b0010 0111 = \x27 // power on, lock blinking, wrench blinkign
          // 0b0001 0111 = \x17 // power on, lock on, wrench blinkign
          // 0b0101 0101 = \x55 // power on, lock on, wrench off, temper on, wifi on

          this->power_led_sensor_->publish_state((led & 1<<1) > 0);
          this->alarm_led_sensor_->publish_state((led & 1<<2) > 0);
          this->tamper_led_sensor_->publish_state((led & 1<<3) > 0);
          this->malfunction_led_sensor_->publish_state((led & 1<<4) > 0);
          this->lock_led_sensor_->publish_state((led & 1<<5) > 0);
          this->wireless_led_sensor_->publish_state((led & 1<<6) > 0);

          if (DISPLAY_MAP_INT_TO_STRING.find(buffer[3]) != DISPLAY_MAP_INT_TO_STRING.end() )
          {
            std::string s  = DISPLAY_MAP_INT_TO_STRING.at(buffer[3]);
            if (s != this->display_text_sensor_->raw_state) {
              this->display_text_sensor_->publish_state(s);
            }
          } else {
            char buf[5];
            sprintf(buf, "\\x%02X", buffer[3]);
            if (this->display_text_sensor_->raw_state != buf) {
              this->display_text_sensor_->publish_state(buf);
            }
          }

          if (STATUS_MAP_INT_TO_STRING.find(buffer[1]) != STATUS_MAP_INT_TO_STRING.end() )
          {
            std::string s  = STATUS_MAP_INT_TO_STRING.at(buffer[1]);
            if (this->status_text_sensor_->raw_state != s) {
              this->status_text_sensor_->publish_state(s);
            }
          } else {
            char buf[5];
            sprintf(buf, "\\x%02X", buffer[3]);
            if (this->status_text_sensor_->raw_state != buf) {
              this->status_text_sensor_->publish_state(buf);
            }
          }
          break;
        }
      }
      buffer[pos] = 0;
      pos = 0;
    }
  }
}

void ja63kComponent::sendline_(uint8_t *buffer, int len) {

}

void ja63kComponent::print_buffer(uint8_t *buffer, int pos) {
  std::string res;
  char buf[5];
  for (size_t i = 0; i < pos; i++) {
      sprintf(buf, "\\x%02X", buffer[i]);
      res += buf;
  }
  res += '"';
  ESP_LOGD(TAG, "%s", res.c_str());
  delay(10);
}

void ja63kComponent::read_all_info(const std::string &name) {
  ESP_LOGD(TAG, "JA63K: %s", name.c_str());

  if (KEY_MAP_STRING_TO_INT.find(name.c_str()) != KEY_MAP_STRING_TO_INT.end() )
  {
    uint8_t key_int = KEY_MAP_STRING_TO_INT.at(name.c_str());
    this->write_byte(key_int);
    this->write_byte(0xFF);
  } else {
    //?
  }
}

void ja63kComponent::dump_config() { 
  ESP_LOGCONFIG(TAG, "JA63K:");
  LOG_SENSOR("  ", "Mode", this->mode_sensor_);
  LOG_TEXT_SENSOR("  ", "Status", this->status_text_sensor_);
}
  

}  // namespace ja63k
}  // namespace esphome