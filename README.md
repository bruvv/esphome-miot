## ESPHome components for MIoT devices

These [ESPHome](https://esphome.io/) components are designed for [MIoT devices](https://home.miot-spec.com/) which adhere to the [Xiaomi MIoT Serial Communication](https://github.com/blakadder/miot) protocol.

Such devices contain two microcontrollers, one actually controls the hardware (MCU), and the other acts as a LAN/cloud gateway.

These components allow you to replace the firmware on the latter, hence liberating your devices from the vendor cloud.

Since this uses [ESPHome](https://esphome.io/), adding your liberated devices to [Home Assistant](https://www.home-assistant.io/) becomes a breeze with the [official integration](https://www.home-assistant.io/integrations/esphome/):

![fan](screenshots/purifier-fan.png)
![sensors](screenshots/purifier-sensors.png)
![configuration](screenshots/purifier-configuration.png)
![diagnostic](screenshots/purifier-diagnostic.png)

## Supported devices

There are probably many more devices that could be supported, currently there are ESPHome configs for the following:

Device | Model Version | Wiki | ESPHome Config | MIoT Specification
---|---|---|---|---
Mi Air Purifier 3/3H | zhimi.airpurifier.mb3 | [link](../../wiki/Xiaomi-Mi-Air-Purifier-3H) | [zhimi.airpurifier.mb3](config/zhimi.airpurifier.mb3.yaml) | [link](https://home.miot-spec.com/spec/zhimi.airpurifier.mb3)
Mi Air Purifier 3C | zhimi.airp.mb4a <br> zhimi.airpurifier.mb4 |[link](../../wiki/Xiaomi-Mi-Air-Purifier-3C) | [zhimi.airp.mb4a](config/zhimi.airp.mb4a.yaml) | [link](https://home.miot-spec.com/spec/zhimi.airp.mb4a) <br> [link](https://home.miot-spec.com/spec/zhimi.airpurifier.mb4)
Xiaomi Air Purifier Pro H | zhimi.airpurifier.va1 | [link](../../issues/89) | [zhimi.airpurifier.va1](config/zhimi.airpurifier.va1.yaml) | [link](https://home.miot-spec.com/spec/zhimi.airpurifier.va1)
Xiaomi Smart Air Purifier 4 | zhimi.airp.mb5 <br> zhimi.airp.mb5a | [link](../../wiki/Xiaomi-Smart-Air-Purifier-4) | [zhimi.airp.mb5](config/zhimi.airp.mb5.yaml) | [link](https://home.miot-spec.com/spec/zhimi.airp.mb5) <br> [link](https://home.miot-spec.com/spec/zhimi.airp.mb5a)
Xiaomi Smart Air Purifier 4 Lite | zhimi.airp.rmb1 | [link](../../wiki/Xiaomi-Smart-Air-Purifier-4-Lite-(zhimi.airp.rmb1)) | [zhimi.airp.rmb1](config/zhimi.airp.rmb1.yaml) | [link](https://home.miot-spec.com/spec/zhimi.airp.rmb1)
Xiaomi Smart Air Purifier 4 Pro | zhimi.airp.vb4 |  | [zhimi.airp.vb4](config/zhimi.airp.vb4.yaml) | [link](https://home.miot-spec.com/spec?type=urn:miot-spec-v2:device:air-purifier:0000A007:zhimi-vb4:1)
Xiaomi Smart Air Purifier Elite | zhimi.airp.meb1 | [link](../../wiki/Xiaomi-Smart-Air-Purifier-Elite) | [zhimi.airp.meb1](config/zhimi.airp.meb1.yaml) | [link](https://miot-spec.org/miot-spec-v2/instance?type=urn:miot-spec-v2:device:air-purifier:0000A007:zhimi-meb1:1)
Mi Smart Antibacterial Humidifier | deerma.humidifier.jsq5 | | [deerma.humidifier.jsq5](config/deerma.humidifier.jsq5.yaml) | [link](https://home.miot-spec.com/spec/deerma.humidifier.jsq5)
Smartmi Evaporative Humidifier 2 | zhimi.humidifier.ca4 | [link](../../wiki/Smartmi-Evaporative-Humidifier-2) | [zhimi.humidifier.ca4](config/zhimi.humidifier.ca4.yaml) | [link](https://home.miot-spec.com/spec/zhimi.humidifier.ca4)
Smartmi Air Purifier | zhimi.airpurifier.za1 |  | [zhimi.airpurifier.za1](config/zhimi.airpurifier.za1.yaml) | [link](https://home.miot-spec.com/spec/zhimi.airpurifier.za1)
Mi Smart Standing Fan 2 | dmaker.fan.p18 |  | [dmaker.fan.p18](config/dmaker.fan.p18.yaml) | [link](https://home.miot-spec.com/spec/dmaker.fan.p18)
Mi Smart Standing Fan 2 Lite | dmaker.fan.1c | [link](../../wiki/Smart-Standing-Fan-2-Lite) | [dmaker.fan.1c](config/dmaker.fan.1c.yaml) | [link](https://home.miot-spec.com/spec/dmaker.fan.1c)
Mi Smart Standing Fan 2 Pro | dmaker.fan.p33 |  | [dmaker.fan.p33](config/dmaker.fan.p33.yaml) | [link](https://home.miot-spec.com/spec/dmaker.fan.p33)
Xiaomi Smart Pet Food Feeder | mmgg.feeder.fi1 | [link](../../wiki/Xiaomi-Smart-Pet-Food-Feeder) | [mmgg.feeder.fi1](config/mmgg.feeder.fi1.yaml) | [link](https://home.miot-spec.com/spec/mmgg.feeder.fi1)

Some of the devices have more than one model (like Mi Air Purifier 3C). If their MIoT specifications are compatible, the ESPHome config will be usable with all of them.

## Unsupported devices

- Devices without a dedicated MCU, using only the ESP chip to directly control the hardware.

  As these components are designed around the communication protocol between the two microcontrollers they're of no use for such devices.
- Devices using a proprietary Xiaomi WiFi microcontroller.

  That hardware is currently unsupported by PlatformIO and hence ESPHome.
- Devices that use the legacy `miio` protocol.

  Such devices may have an ESP chip and a separate microcontroller, but the communication protocol is unsupported by these components.

  If the device has the `miio2miot` tag on the [Xiaomi MIoT Spec](https://home.miot-spec.com/) site, or if you see messages like `props power "on"` on the serial bus, this is the case.

Known unsupported devices:

Device | Model Version | Reason | Link | MIoT Specification
---|---|---|---|---
Mi Air Purifier 2S | zhimi.airpurifier.mc1 | Proprietary chip _MHCW02P_ | [link](../../wiki/Xiaomi-Mi-Air-Purifier-2H-2S) | [link](https://home.miot-spec.com/spec/zhimi.airpurifier.mc1)
Mi Air Purifier 2H | zhimi.airpurifier.mc2 | Proprietary chip _MHCW02P_ | [link](../../wiki/Xiaomi-Mi-Air-Purifier-2H-2S) | [link](https://home.miot-spec.com/spec/zhimi.airpurifier.mc2)
Xiaomi Air Purifier 4 Lite (CN Model) | zhimi.airp.rma3 | No dedicated MCU | [link](../../issues/34) | [link](https://home.miot-spec.com/spec/zhimi.airp.rma3)
Xiaomi Smart Air Purifier 4 Compact | zhimi.airp.cpa4 | No dedicated MCU | [link](../../issues/22#issuecomment-2137163103) | [link](https://home.miot-spec.com/spec/zhimi.airp.cpa4)
Smartmi Evaporative Humidifier | zhimi.humidifier.cb1 | Proprietary chip _MHCWB2P_ | [link](../../issues/26#issuecomment-2417148320) | [link](https://home.miot-spec.com/spec/zhimi.humidifier.cb1)
Smartmi Evaporative Humidifier 3 | zhimi.humidifier.ca6 | No dedicated MCU | [link](../../issues/102) | [link](https://home.miot-spec.com/spec/zhimi.humidifier.ca6)
Xiaomi Smart Tower Fan | dmaker.fan.p39 | Proprietary chip _MHCWB4P-B_ | [link](../../pull/52) | [link](https://home.miot-spec.com/spec/dmaker.fan.p39)
Xiaomi Smart Tower Fan 2 | xiaomi.fan.p45 | Proprietary chip _MHCWB5G-B_ | [link](../../issues/78) | [link](https://home.miot-spec.com/spec/xiaomi.fan.p45)
Xiaomi Smart Pet Food Feeder 2 | xiaomi.feeder.iv2001 | Proprietary chip _MHCW05P-B_ | [link](../../pull/72) | [link](https://home.miot-spec.com/spec/xiaomi.feeder.iv2001)
Xiaomi Smart Graphene Heater | xiaomi.heater.ma8 | No dedicated MCU | [link](../../issues/98) | [link](https://home.miot-spec.com/spec/xiaomi.heater.ma8)
Xiaomi Smart Evaporative Humidifier | xiaomi.humidifier.3lite | Proprietary chip _MHCWB5G-B_ | [link](../../pull/105) | [link](https://home.miot-spec.com/spec/xiaomi.humidifier.3lite)

## Building a firmware

Either download an [ESPHome config](config/) or create your own (see below) and feed it to ESPHome to build the firmware.

There's no need to clone this repo, unless you plan to contribute - which would be very welcome!

## Adding devices

First, look up the desired device on the [Xiaomi MIoT Spec](https://home.miot-spec.com/) site.

Each device defines its service (`SIID`) and property (`PIID`) IDs. You just have to add all the desired properties with their according IDs to your ESPHome yaml config.

For examples, see the [supported devices](#supported-devices) table above and compare a config against its specification.

Once your newly added device is working, please open a PR to add its config here!

## Home assistant UI Cards

You can use this card to control the Xiaomi humidifier 2 (ca4)
![CA4 home assistant esphome card](screenshots/image.png)

```
type: vertical-stack
cards:
  - type: custom:mushroom-title-card
    title: Humidifier
    subtitle: Smartmi Evaporative 2

  - type: horizontal-stack
    cards:
      - type: custom:mushroom-entity-card
        entity: sensor.air_humidifier_relative_humidity
        name: Humidity
        icon: mdi:water-percent
        icon_color: blue
        primary_info: state
        secondary_info: name
      - type: custom:mushroom-entity-card
        entity: sensor.air_humidifier_temperature
        name: Temperature
        icon: mdi:thermometer
        icon_color: orange
        primary_info: state
        secondary_info: name
      - type: custom:mushroom-entity-card
        entity: sensor.air_humidifier_water_level
        name: Water
        icon: mdi:cup-water
        icon_color: cyan
        primary_info: state
        secondary_info: name

  - type: custom:mushroom-fan-card
    entity: fan.air_humidifier_fan
    name: Fan
    icon_animation: true
    show_percentage_control: true
    show_oscillate_control: false
    collapsible_controls: false
    fill_container: false

  - type: custom:mushroom-select-card
    entity: select.air_humidifier_display_brightness
    name: Display
    icon: mdi:brightness-6

  - type: custom:mushroom-number-card
    entity: number.air_humidifier_target_humidity
    name: Target humidity
    icon: mdi:target
    icon_color: teal
    display_mode: slider

  - type: conditional
    conditions:
      - entity: fan.air_humidifier_fan
        attribute: preset_mode
        state: Auto
    card:
      type: custom:mushroom-template-card
      primary: Auto mode active
      secondary: >-
        Target {{ states('number.air_humidifier_target_humidity') }}% - now {{
        states('sensor.air_humidifier_relative_humidity') }}%
      icon: mdi:auto-mode
      icon_color: green
      fill_container: true

  - type: horizontal-stack
    cards:
      - type: custom:mushroom-entity-card
        entity: switch.air_humidifier_dry
        name: Dry
        icon: mdi:water-minus
        icon_color: amber
        tap_action:
          action: toggle
      - type: custom:mushroom-entity-card
        entity: switch.air_humidifier_child_lock
        name: Lock
        icon: mdi:lock
        icon_color: red
        tap_action:
          action: toggle
      - type: custom:mushroom-entity-card
        entity: switch.air_humidifier_notification_sounds
        name: Sound
        icon: mdi:volume-high
        icon_color: purple
        tap_action:
          action: toggle
      - type: custom:mushroom-entity-card
        entity: switch.air_humidifier_clean_mode
        name: Clean
        icon: mdi:spray-bottle
        icon_color: pink
        tap_action:
          action: toggle

  - type: custom:mini-graph-card
    entities:
      - entity: sensor.air_humidifier_relative_humidity
        name: Humidity
        color: '#03a9f4'
      - entity: number.air_humidifier_target_humidity
        name: Target
        color: '#4caf50'
        show_state: true
        y_axis: secondary
    name: Humidity trend
    hours_to_show: 24
    points_per_hour: 6
    line_width: 2
    smoothing: true
    show:
      labels: true
      labels_secondary: false
      legend: true

  - type: entities
    title: Diagnostics
    show_header_toggle: false
    entities:
      - entity: sensor.air_humidifier_motor_speed
        name: Motor RPM
        icon: mdi:fan
      - entity: sensor.air_humidifier_actual_speed
        name: Actual RPM
        icon: mdi:fan-clock
      - entity: sensor.air_humidifier_device_fault_code
        name: Fault code
      - entity: sensor.air_humidifier_mcu_temperature
        name: MCU temp
```

## Feedback

Please feel free to open [issues](../../issues) and/or [pull requests](../../pulls) here.

Alternatively, there's a [thread](https://community.home-assistant.io/t/esphome-components-for-miot-devices/686646) on the official ESPHome forums.

## Inspired by
https://github.com/jaromeyer/mipurifier-esphome
https://github.com/dhewg/esphome-miot
