

apt-get install -y python-pip

pip install selenium

# webdriver for linux 
## http://chromedriver.storage.googleapis.com/2.9/chromedriver_linux64.zip

wget http://chromedriver.storage.googleapis.com/2.9/chromedriver_linux64.zip

unzip /home/lavee_singh/Downloads/chromedriver_linux64.zip

mv /home/lavee_singh/Downloads/chromedriver /usr/bin

apt-get install -y xvfb

pip install pyvirtualdisplay