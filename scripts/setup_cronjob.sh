#!/bin/bash
(crontab -l ; echo "0 * * * * /bin/bash /path-to-script/upload_logs.sh") | crontab -

