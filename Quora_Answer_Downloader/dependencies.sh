notify-send "Attention!" "This will take 2 minutes, please relax, and let it finish installing dependencies!!!"

apt-get install -y python-pip

pip install selenium

# webdriver for linux 
## http://chromedriver.storage.googleapis.com/2.9/chromedriver_linux64.zip

wget -nc http://chromedriver.storage.googleapis.com/2.9/chromedriver_linux64.zip

unzip /home/lavee_singh/Downloads/chromedriver_linux64.zip

mv /home/lavee_singh/Downloads/chromedriver /usr/bin

apt-get install -y xvfb
apt-get install -y wkhtmltopdf

pip install pyvirtualdisplay
pip install pdfkit
