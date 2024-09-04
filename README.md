
# OpenWRT-collectd-MQTT-HA
Collect OpenWRT statistics from your Router using this MQTT Template.

## Setup
### Home Assistant MQTT setup
Let's prepare Home Assistant first.

If you don't have it yet, get Mosquitto Broker up and running. Read ![the official docs](https://github.com/home-assistant/addons/blob/174f8e66d0eaa26f01f528beacbde0bd111b711c/mosquitto/DOCS.md) to get started. Don't forget to configure the MQTT Integration as well!

### OpenWRT

Install the following packages:

    luci-app-statistics 
    collectd-mod-mqtt

The first package will install `collectd` and most of the essential dependencies.

Optional `collectd-mod-*` packages can provide more data. These are recommended:

    collectd-mod-thermal
    collectd-mod-uptime
    collectd-mod-dhcpleases

Navigate to *Statistics > Setup*. If you installed optional mod packages, enable them in the *General Plugin* tab.

If you're running OpenWRT snapshots from the master branch (24.x and above), the luci-app-statistics [has the ability](https://github.com/openwrt/luci/commit/8bf5646459e229c1d01736f7c45f3b1c9bf3058f) to configure MQTT via GUI. If you're running a previous version up to OpenWRT 23.05, you'll have to follow the CLI steps. The next major release will have this built in.
<details>
     <summary>GUI configuration - OpenWRT snapshots</summary>
    
In the *Output Plugins* Tab, enable *Mqtt* and click on Configure. Then click Add, and enter the following Details:
- Name - `OpenWRT` or what you like
- Host - this is your Home Assistant IP
- Port - `1883` if you're using the default port
- User - your MQTT User
- Password - your MQTT password
- Prefix - `collectd`

Save and apply changes.  

</details>


<details>
     <summary>CLI configuration - up to OpenWRT 23.05</summary>
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
</details>

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

To quickly check that you're receiving data from your OpenWRT router, open HA and Navigate to the MQTT Integration, then click *Configure*. In the section Listen to a topic, add `collectd/#`, then click *Start Listening*. You should see many messages coming from OpenWRT.

Check received data on MQTT server using  [MQTT Explorer](https://community.home-assistant.io/t/addon-mqtt-explorer-new-version/603739)  or use this code if you prefer:

    mosquitto_sub -h localhost -p 1883 -u user -P Password -t collectd/# -d

 



