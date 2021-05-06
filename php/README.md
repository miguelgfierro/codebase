# PHP

## Installation

### Apache 

Install Apache:

    sudo apt install apache2

To start Apache:

    sudo systemctl start apache2

You can enable Apache to start automatically on server boot:

    sudo systemctl enable apache2

To check the status of the Apache web server and make sure it is up and running, you can use the following command:

    sudo systemctl status apache2

To check that it is working, open your web browser and enter your server IP address, (e.g. http://your_server_ip_address). If Apache is successfully installed, you should see the Apache default welcome page.

### PHP

Install PHP:

    sudo apt-get install php libapache2-mod-php sendmail.

To test your installation and check that Apache, PHP and PHP extensions are working properly, create a new php info file:

    vim /var/www/html/phpinfo.php

Add `<?php phpinfo(); ?>` and open the file file using a web browser: `http://<ip-address>/phpinfo.php`.


