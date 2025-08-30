from named_tuples import Device, Sensor, IndexedSensor

MQTT_PREFIX = "collectd"
DEVICE_HOSTNAME = "WRT7800"
# Set as needed for your system use MQTT Explorer if necessary to identify topics and these fields.
TOPIC_ROOT = f"{MQTT_PREFIX}/{DEVICE_HOSTNAME}"

config = {
    # Any of these can be ommited and the jinja2 template should ignore it, simply delete or comment out any sensors you don't want.
    "device": Device(
        identifiers="WRT7800",
        name="Router Netgear R7800",
        model="R7800",
        manufacturer="Netgear",
    ),
    "device_prefix": "openwrt",  # this should match the device.identifiers so "My OpenWrt"->"my_openwrt"
    "router_host": "192.168.1.1",
    "uptime": Sensor(
        name="Uptime", unique_id="ap_uptime", topic=f"{TOPIC_ROOT}/uptime/uptime"
    ),
    "connections": Sensor(
        name="Connections",
        unique_id="ap_connections",
        topic=f"{TOPIC_ROOT}/conntrack/conntrack",
    ),
    "ping": Sensor(
        name="Google ping", unique_id="ap_ping", topic=f"{TOPIC_ROOT}/ping/ping-8.8.8.8"
    ),
    "dhcp_leases": Sensor(
        name="DHCP Active Leases",
        unique_id="dhcp_clients",
        topic=f"{TOPIC_ROOT}/dhcpleases/count",
    ),
    "ram_sensors": [
        Sensor(
            name="RAM buffered",
            unique_id="ram_buffered",
            topic=f"{TOPIC_ROOT}/memory/memory-buffered",
        ),
        Sensor(
            name="RAM free",
            unique_id="ram_free",
            topic=f"{TOPIC_ROOT}/memory/memory-free",
        ),
        Sensor(
            name="RAM cached",
            unique_id="ram_cached",
            topic=f"{TOPIC_ROOT}/memory/memory-cached",
        ),
        Sensor(
            name="RAM used",
            unique_id="ram_used",
            topic=f"{TOPIC_ROOT}/memory/memory-used",
        ),
    ],
    "load_sensors": [
        IndexedSensor(
            name="L1", unique_id="l1", topic=f"{TOPIC_ROOT}/load/load", index=1
        ),
        IndexedSensor(
            name="L5", unique_id="l5", topic=f"{TOPIC_ROOT}/load/load", index=2
        ),
        IndexedSensor(
            name="L15", unique_id="l15", topic=f"{TOPIC_ROOT}/load/load", index=3
        ),
    ],
    "interfaces": [
        Sensor(name="WAN", unique_id="wan", topic=f"{TOPIC_ROOT}/interface-eth1"),
        Sensor(
            name="Br-Lan", unique_id="br-lan", topic=f"{TOPIC_ROOT}/interface-br-lan"
        ),
        Sensor(
            name="Br-Guest",
            unique_id="br-guest",
            topic=f"{TOPIC_ROOT}/interface-br-guest",
        ),
        Sensor(
            name="Br-IoT", unique_id="br-iot", topic=f"{TOPIC_ROOT}/interface-br-iot"
        ),
    ],
    "wifis": [
        Sensor(
            name="Clients 2.4Ghz IoT",
            unique_id="ap_clients_24_iot",
            topic=f"{TOPIC_ROOT}/iwinfo-wl0-ap0/stations",
        ),
        Sensor(
            name="Clients 2.4Ghz Main",
            unique_id="ap_clients_24_main",
            topic=f"{TOPIC_ROOT}/iwinfo-wl0-ap1/stations",
        ),
        Sensor(
            name="Clients 2.4Ghz Guest",
            unique_id="ap_clients_24_guest",
            topic=f"{TOPIC_ROOT}/iwinfo-wl0-ap2/stations",
        ),
        Sensor(
            name="Clients 5Ghz IoT",
            unique_id="ap_clients_5_iot",
            topic=f"{TOPIC_ROOT}/iwinfo-wl1-ap0/stations",
        ),
        Sensor(
            name="Clients 5Ghz Guest",
            unique_id="ap_clients_5_guest",
            topic=f"{TOPIC_ROOT}/iwinfo-wl1-ap1/stations",
        ),
        Sensor(
            name="Clients 5Ghz Main",
            unique_id="ap_clients_5_main",
            topic=f"{TOPIC_ROOT}/iwinfo-wl1-ap0/stations",
        ),
    ],
    "temp_sensors": [
        Sensor(
            name="Temperature",
            unique_id="ap_temp",
            topic=f"{TOPIC_ROOT}/thermal-thermal_zone0/temperature",
        ),
    ],
    "ip_addr_sensors": [
        Sensor(
            name="WAN IPv4", unique_id="wan_ip4", topic=f"{TOPIC_ROOT}/wan-info/wan-ip"
        ),
        Sensor(
            name="WAN IPv6(Global 1)",
            unique_id="wan_ip6_global0",
            topic=f"{TOPIC_ROOT}/wan-info/wan-ip6-global-0",
        ),
        Sensor(
            name="WAN IPv6(Global 2)",
            unique_id="lan_ip6_global1",
            topic=f"{TOPIC_ROOT}/wan-info/wan-ip6-global-1",
        ),
        Sensor(
            name="WAN IPv6(Link Local)",
            unique_id="lan_ip6_link_local",
            topic=f"{TOPIC_ROOT}/wan-info/wan-ip6-link",
        ),
    ],
    "link_status_sensor": [
        Sensor(
            name="WAN Status", unique_id="wan_status", topic=f"{TOPIC_ROOT}/pppoe-wan"
        ),
    ],
}
