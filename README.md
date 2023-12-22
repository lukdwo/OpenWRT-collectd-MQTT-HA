
# OpenWRT-collectd-MQTT-HA
Collect OpenWRT statistics from your Router using this MQTT Template.

## Setup
### Home Assistant MQTT setup
Let's prepare Home Assistant first.

If you don't have it yet, get Mosquitto Broker up and running. Read ![the official docs](https://github.com/home-assistant/addons/blob/174f8e66d0eaa26f01f528beacbde0bd111b711c/mosquitto/DOCS.md) to get started. Don't forget to configure the MQTT Integration as well!

Navigate to the MQTT Integration, then click *Configure*. In the section Listen to a topic, add `collectd/#`, then click *Start Listening*. 
Reload the MQTT integration to apply the changes.


### OpenWRT

Install the following packages:

    luci-app-statistics 
    collectd-mod-mqtt

The first package will install `collectd` and most of the essential dependencies.

Optional `collectd-mod-*` packages can provide more data. These are recommended:

    collectd-mod-thermal
    collectd-mod-uptime

Navigate to *Statistics > Setup*. If you installed optional mod packages, enable them in the *General Plugin* tab.

Connect to your OpenWRT router via SSH, create a new folder called `conf.d` in `/etc/collectd/`

Using your favourite editor, create a new file in conf.d called `mqtt.conf`

Add this configuration to the file, and edit the lines:
* `Host` replace this with your Home Assistant IP
* `User` replace this with your MQTT User
* `Password` replace this with your MQTT password
   
```shell
LoadPlugin mqtt
<Plugin "mqtt">
  <Publish "OpenWRT">
    Host "192.168.1.101"
    Port "1883"
    User "mqtt_openwrt"
    Password "MySuperSafePW2!@"
    ClientId "OpenWRT"
    Prefix "collectd"
    Retain true
  </Publish>
</Plugin>
```

Restart collectd on OpenWRT by executing `service collectd restart`.

OpenWRT will start sending data to Home Assistant, but you won't be able to see it (yet).

### Home Assistant Entities setup

Go back to Home Assistant for the final setup.
Some text replacements are required, on Windows you can use Notepad++.

Open this sample [configuration.yaml](configuration.yaml).

Replace occurrencies of `<Open-WRT-Hostname>` with the value you see in *OpenWRT > System > System > General Settings > Hostname*

Each sensor has a section like the following:

```yaml
    device:
            identifiers: WRT7800
            name: Router Netgear R7800
            model: R7800
            manufacturer: Netgear
```

It allows to create a MQTT device, so all entities are grouped nicely. Replace these example values for **each sensor** entering what you like, these are just informational labels. Use the same values for each entity!

When you are done with text editing, paste the code in your configuration.yaml on Home Assistant.

Save the file and restart Home Assistant.

When finished, you will have a new MQTT device named after the name you have chosen above, and the entities will be populated.

Please note that some entities require additional OpenWRT mod packages.

## Dashboard and card setup

To use this card, you must install `multiple-entity-row` and `mini-graph-card` from HACS.

Edit the dashboard, add a new YAML card and paste the code you find in [lovelace.yaml](lovelace.yaml).

## Troubleshooting

Check received data on MQTT server using  [MQTT Explorer](https://community.home-assistant.io/t/addon-mqtt-explorer-new-version/603739)  or use this code if you prefer:

    mosquitto_sub -h localhost -p 1883 -u user -P Password -t collectd/# -d

 



