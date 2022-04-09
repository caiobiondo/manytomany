#!/bin/sh
if [ "$1" == "" ]; then
    echo "Please enter version"
    exit 1
fi

echo "upgrading demo to v-${1}"

# for private repos you can use wget with GithubToken in header
# example --header "Authorization: token ${GITHUB_TOKEN}"

wget https://github.com/caiobiondo/manytomany/archive/refs/heads/master.zip

# unzip
cd /home/ubuntu
unzip master.zip
rm master.zip
cd manytomany-master/
pip install -r requiriments.txt
pip install drf-spectacular
pip install allauth
pip install django-allauth
pip install django-filter
pip install django-cors-headers
pip install pandas
python manage.py makemigrations
python manage.py migrate


# Copy service file, incase if there are any changes
sudo cp demo.service /etc/systemd/system/demo.service
# reload configurations incase if service file has changed
sudo systemctl daemon-reload
# restart the service
sudo systemctl restart demo.service
# start of VM restart
sudo systemctl enable demo.service
