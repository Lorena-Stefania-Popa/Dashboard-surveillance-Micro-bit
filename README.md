# Dashboard-surveillance-Micro-bit
Python with Ubidots

I created an account on Ubidots, after I entered a Linux, more precisely on DEBIAN where I gave a "sudo apt-get install screen". Then because I didn't have any pip3 or python 
on this virtual machine, I installed the commands on this site: "https://linuxize.com/post/how-to-install-python-3-9-on-debian -10 / "to work + I gave another sudo apt-get -y 
install python3-pip. I looked at the documentation and took the code from "Send multiple dots" and added it to start.py.
I looked and understood that I call the main code of the payload of variables 1 and 2, a url, a device and so on in post_var because it is of JSON type, it practically recognizes
what I call from main.
I created a new dashboard on ubidots called "Dashboard surveillance Micro: bit".
In fact, in main.py I created in an infinite loop a msg and a msg2 to read my temperature and light level values, just like in lab 11, and because it was not asked not to send 
or date at 30s. Values from the two sensors I added at the end a utime.sleep (30).
I went back to ubidots and created a new device, I called it "Microbit", and in it I added 2 raw variables. The first "temperature" and the second "light". Then I went to 
Data ---> Dashboards and added a "thermometer" (I added the temperature variable) and a "gauge" (I added the light variable). But I had problems with Vmware because I can't 
read the microbit on "removable devices", so I turned off the debian and went to settings to protect all my USB ports. Only then did I connect to the microbit on Vmware and enter 
python3 start.py in the sudo terminal. Everything went well and without light and with the light from the phone flash, so for the token, I had to delete the token I entered from 
the dashboards and add "<token>" as required to load the project.
