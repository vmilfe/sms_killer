#!/bin/bash
testfunction(){
   apt update -y
   apt upgrade -y
   apt install python -y
   pip3 install colorama
   pip3 install requests
   pip3 install fake_headers
   python3 sms_killer.py
}
testfunction