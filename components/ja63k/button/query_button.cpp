#include "query_button.h"

namespace esphome {
namespace ja63k {

void QueryButton::press_action() { 
    this->parent_->read_all_info(
        this->get_name()); 
    }
}  // namespace ld2410
}  // namespace esphome