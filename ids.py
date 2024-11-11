"""


PROCEDURE:
Prerequisites: Snort should be installed on a Linux machine. If it's not
installed, you can do so with:
```bash
sudo apt-get update
sudo apt-get install snort
```
Step 1: Configure Snort in promiscuous mode
Make sure your network interface is set to promiscuous mode to capture all
network traffic. For example:
```bash
sudo ip link set eth0 promisc on
```
Replace `eth0` with the appropriate network interface on your machine.
Step 2: Writing a basic Snort rule
Create a custom Snort rule to detect specific malicious activity. Let's say you
want to detect ICMP Ping (Echo Requests):
1. Open the rules file, usually located at `/etc/snort/rules/local.rules`:
```bash
sudo nano /etc/snort/rules/local.rules
```
2. Add the following rule to detect an ICMP ping request (commonly
used in ping sweeps):
```plaintext
alert icmp any any -> any any (msg:"ICMP Ping detected";
itype:8; sid:1000001; rev:1;)
```
Explanation:
- `alert` – defines the action to be taken when the rule matches.
- `icmp` – protocol type.
- `any any -> any any` – matches traffic from any IP and port to any IP and
port.
- `msg:"ICMP Ping detected"` – the alert message that will be logged.
- `itype:8` – filters for ICMP echo requests (ping).
- `sid:1000001` – unique Snort rule ID. 




- `rev:1` – rule revision number.
 Step 3: Run Snort in NIDS mode
```bash
sudo snort -A console -q -c /etc/snort/snort.conf -i eth0
```
- `-A console` – outputs alerts to the console.
- `-q` – runs Snort in quiet mode to reduce non-essential output.
- `-c` – specifies the configuration file.
- `-i eth0` – sets the interface Snort will listen to (replace `eth0` with your
network interface).`
 Step 4: Test the IDS
```bash
ping <target-ip>
```
If Snort detects the ICMP ping request, it will generate an alert in the console
that matches the rule you defined.
 Example Output:
If the ping is detected, Snort will output something like:
```plaintext
[**] [1:1000001:1] ICMP Ping detected [**] 
"""