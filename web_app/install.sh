#!/bin/bash 

sudo yum install -y python-pip gcc epel-release python-devel

sudo yum install postgresql-server postgresql-contrib postgresql-devel -y 

sudo postgresql-setup initdb

sudo sed -i -e 's/ident/trust/g' /var/lib/pgsql/data/pg_hba.conf

sudo systemctl start postgresql
sudo systemctl enable postgresql

sudo pip install virtualenv 

virtualenv /web_app 


source /web_app/bin/activate && python /web_app/setup.py install 
