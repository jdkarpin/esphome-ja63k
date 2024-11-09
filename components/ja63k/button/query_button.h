#pragma once

#include "esphome/components/button/button.h"
#include "../ja63k.h"

namespace esphome {
namespace ja63k {

class QueryButton : public button::Button, public Parented<ja63kComponent> {
 public:
  QueryButton() = default;

 protected:
  void press_action() override;
};

}  // namespace ja63k
}  // namespace esphome