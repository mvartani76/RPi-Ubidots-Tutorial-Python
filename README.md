RPi-Ubidots-Tutorial-Python
===========================

Simple tutorial showing how to interface with Ubidots Cloud Platform<br>

Tutorial taken mainly from http://ubidots.com/docs/devices/raspberrypi.html. Verified that this works with Python2.7 but not Python3.2.

Configure RPi to use Python API Client
======================================
Let’s make sure your device is up to date so that it has the latest python tools (be aware that this will take a while):<br>
Remember that I was only able to get it to work with Python 2.7<br>
<ol>
<li>Update and upgrade to latest packages</li>
<pre class="code-text-only" style="display: none;">
<code>sudo apt-get update
sudo apt-get upgrade</code></pre>

<li>Download the pip installer and install Ubidots’ Python library</li>
<pre class="code-text-only" style="display: none;">
<code>sudo apt-get install python-setuptools
sudo easy_install pip
pip install ubidots==0.1.3-alpha</code></pre>
</ol>

Git the Code
============
From your /home/pi directory, get the Ubidots tutorial code checked into GitHub
<pre class="code-text-only" style="display: none;">
<code>sudo git clone https://github.com/mvartani76/RPi-Ubidots-Tutorial-Python/
</code></pre>

Setup a test Variable in Ubidots
================================
As a logged in user navigate to the “Data” tab.<br>
Create a Data Source by clicking on the orange icon on the right. Then create a variable within that Data Source.<br>
Take note of the variable’s ID to which you want to send data. For this example we’ll use a variable with the ID: “521d792df91b2816f35c8587”
Take note of your API key.<br>
